import os
import sys
import re
import glob
from ruamel.yaml import YAML
import ruamel.yaml as yaml

header = """
version: 2.1
orbs:
  docker: circleci/docker@1.3.0
commands:
  run_if_modified:
    description: Run steps if files are modified
    parameters:
      always-run-on-branch:
        default: ''
        description: The branch to always run the steps on
        type: string
      base-branch:
        default: master
        description: The branch against which to check against. This can also be a
          commit SHA
        type: string
      check-last-commit-on-base-branch:
        default: false
        description: 'This will make the check run for the latest commit on the base
          branch.'
        type: boolean
      pattern:
        default: ".*"
        description: |
          The regex to match files against. The command uses grep to search file names.
          If you want to enforce starting with use ^. For checking if files in src/ or lib/ were modified,
          the pattern to use would be ^src.*|^lib.*
        type: string
      steps-to-run:
        default: []
        description: The steps to run if the files mentioned are modified
        type: steps
      use-divergence-point:
        default: false
        description: Find the divergence from the branch passed above, rather than
          the current HEAD
        type: boolean
    steps:
    - run:
        command: |
          if [ -z "$BASH" ]; then
            echo Bash not installed.
            exit 1
          fi
          git status >/dev/null 2>&1 || { echo >&2 "Not in a git directory or no git"; exit 1; }
          circleci-agent >/dev/null 2>&1 || { echo >&2 "No Circle CI agent. These are in all Circle CI containers"; exit 1; }

          if [ "$CIRCLE_BRANCH" == "<< parameters.always-run-on-branch >>" ]; then
            echo "Should always run on << parameters.always-run-on-branch >>. Exiting and continuing to run"
            exit 0;
          fi

          FILES_MODIFIED=""
          setcommit () {
            FILES_MODIFIED=$(git diff --name-only origin/<< parameters.base-branch >>..HEAD | grep -i -E '<< parameters.pattern >>')
            <<# parameters.use-divergence-point >>
            FILES_MODIFIED=$(git diff --name-only $(git merge-base HEAD origin/<< parameters.base-branch >>)..HEAD | grep -i -E '<< parameters.pattern >>')
            <</ parameters.use-divergence-point >>
            <<# parameters.check-last-commit-on-base-branch >>
            if [[ "$CIRCLE_BRANCH" == "<< parameters.base-branch >>" ]]; then
              FILES_MODIFIED=$(git diff --name-only HEAD~1 HEAD | grep -i -E '<< parameters.pattern >>')
            fi
            <</ parameters.check-last-commit-on-base-branch >>
          }

          setcommit || true
          if [ -z "$FILES_MODIFIED" ]
          then
            echo "Files not modified. Halting job"
            circleci-agent step halt
          else
            echo "Files modified, continuing steps"
          fi
        name: Only run if modified
    - steps: "<< parameters.steps-to-run >>"
"""

monthlyTrigger = {
  "schedule": {
    "cron": "57 0 1 * *",
    "filters": {
      "branches": {
        "only": ["master"]
      }
    }
  }
}

mergeFilter = {
  "branches": {
    "only": ["master"]
  }
}

diffFilter = {
  "branches": {
    "ignore": ["master"]
  }
}

# Grab the paths of validly structured Dockerfiles (git_dir/tool_dir/version_dir/Dockerfile)
validPaths = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../*/*/Dockerfile"))

# Build dictionary for monthly jobs
monthly_jobs = []
for path in validPaths:
  dat = {}
  workdir,tool,tag,dockerfile = path.split('/')[-4:]
  dat['docker/publish'] = {}
  dat['docker/publish']['name'] = "{}_{}_monthly".format(tool,tag)
  dat['docker/publish']['deploy'] = False
  dat['docker/publish']['registry'] = "pgc-images.sbgenomics.com"
  dat['docker/publish']['image'] = "d3b-bixu/{}".format(tool.lower())
  dat['docker/publish']['tag'] = "{}".format(tag)
  dat['docker/publish']['path'] = "{}/{}/".format(tool,tag)
  dat['docker/publish']['docker-context'] = "{}/{}/".format(tool,tag)
  monthly_jobs.append(dat)

# Build dictionary for diff based jobs
diff_jobs = []
for path in validPaths:
  dat = {}
  workdir,tool,tag,dockerfile = path.split('/')[-4:]
  dat['docker/publish'] = {}
  dat['docker/publish']['filters'] = diffFilter
  dat['docker/publish']['context'] = "dockerhub-vars"
  dat['docker/publish']['name'] = "{}_{}_diff".format(tool,tag)
  dat['docker/publish']['deploy'] = False
  dat['docker/publish']['registry'] = "pgc-images.sbgenomics.com"
  dat['docker/publish']['image'] = "d3b-bixu/{}".format(tool.lower())
  dat['docker/publish']['tag'] = "{}".format(tag)
  dat['docker/publish']['path'] = "{}/{}/".format(tool,tag)
  dat['docker/publish']['docker-context'] = "{}/{}/".format(tool,tag)
  dat['docker/publish']['before_build'] = [{'run_if_modified':{'pattern':"{}/{}/{}".format(tool,tag,dockerfile)}}]
  diff_jobs.append(dat)

# Build dictionary for merge builds
merge_jobs = []
for path in validPaths:
  dat = {}
  workdir,tool,tag,dockerfile = path.split('/')[-4:]
  dat['docker/publish'] = {}
  dat['docker/publish']['filters'] = mergeFilter
  dat['docker/publish']['name'] = "{}_{}_merge".format(tool,tag)
  dat['docker/publish']['context'] = "dockerhub-vars"
  dat['docker/publish']['deploy'] = True
  dat['docker/publish']['registry'] = "pgc-images.sbgenomics.com"
  dat['docker/publish']['image'] = "d3b-bixu/{}".format(tool.lower())
  dat['docker/publish']['tag'] = "{}".format(tag)
  dat['docker/publish']['path'] = "{}/{}/".format(tool,tag)
  dat['docker/publish']['docker-context'] = "{}/{}/".format(tool,tag)
  dat['docker/publish']['before_build'] = [{'run_if_modified':{'pattern':"{}/{}/{}".format(tool,tag,dockerfile), 'check-last-commit-on-base-branch':True}}]
  merge_jobs.append(dat)

# Build the output dictionary
output = yaml.load(header,Loader=yaml.RoundTripLoader)
output['workflows'] = {}
output['workflows']['monthly'] = {}
output['workflows']['monthly']['triggers'] = [monthlyTrigger]
output['workflows']['monthly']['jobs'] = monthly_jobs
output['workflows']['diff'] = {}
output['workflows']['diff']['jobs'] = diff_jobs
output['workflows']['merge'] = {}
output['workflows']['merge']['jobs'] = merge_jobs

# Output the output dictionary as YAML to stdout without aliases
yaml = YAML()
yaml.representer.ignore_aliases = lambda *data: True
yaml.dump(output, sys.stdout)
