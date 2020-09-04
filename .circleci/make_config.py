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
              FILES_MODIFIED=$(git diff --name-only HEAD HEAD~1 | grep -i -E '<< parameters.pattern >>')
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

# Grab the paths of validly structured Dockerfiles (git_dir/tool_dir/version_dir/Dockerfile)
validPaths = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../*/*/Dockerfile"))

# Build dictionary for monthly jobs
data = []
for path in validPaths:
  datum = {}
  workdir,tool,tag,dockerfile = path.split('/')[-4:]
  datum['docker/publish'] = {}
  datum['docker/publish']['name'] = "{}_{}_monthly".format(tool,tag)
  datum['docker/publish']['deploy'] = False
  datum['docker/publish']['image'] = "kfdrc/{}".format(tool.lower())
  datum['docker/publish']['tag'] = "{}".format(tag)
  datum['docker/publish']['path'] = "{}/{}/".format(tool,tag)
  datum['docker/publish']['docker-context'] = "{}/{}/".format(tool,tag)
  data.append(datum)

# Build dictionary for diff based jobs
diffs = []
for path in validPaths:
  diff = {}
  workdir,tool,tag,dockerfile = path.split('/')[-4:]
  diff['docker/publish'] = {}
  diff['docker/publish']['context'] = "dockerhub-vars"
  diff['docker/publish']['name'] = "{}_{}_diff".format(tool,tag)
  diff['docker/publish']['deploy'] = True
  diff['docker/publish']['image'] = "kfdrc/{}".format(tool.lower())
  diff['docker/publish']['tag'] = "{}".format(tag)
  diff['docker/publish']['path'] = "{}/{}/".format(tool,tag)
  diff['docker/publish']['docker-context'] = "{}/{}/".format(tool,tag)
  diff['docker/publish']['before_build'] = [{'run_if_modified':{'pattern':"{}/{}/{}".format(tool,tag,dockerfile)}}]
  diffs.append(diff)

# Build the output dictionary
output = yaml.load(header,Loader=yaml.RoundTripLoader)
output['workflows'] = {}
output['workflows']['monthly'] = {}
output['workflows']['monthly']['triggers'] = [monthlyTrigger]
output['workflows']['monthly']['jobs'] = data
output['workflows']['diff'] = {}
output['workflows']['diff']['jobs'] = diffs

# Output the output dictionary as YAML to stdout without aliases
yaml = YAML()
yaml.representer.ignore_aliases = lambda *data: True
yaml.dump(output, sys.stdout)
