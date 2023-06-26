# D3B Docker Image Build Instruction Hub

This repo contains build instructions that we use at the Center for Data-Driven Discovery in Biomedicine (D3B) and in the Kids First Data Resource Center (KFDRC). The most updated production images are stored in the [SBG docker registry](https://cavatica.sbgenomics.com/developer/docker). This requires a Cavatica login and individual images may require separate permission to access.

Legacy versions of some images are stored in the [KFDRC Dockerhub](https://hub.docker.com/u/kfdrc/). The images on Dockerhub are deprecated and will not be updated.

# Current Dockers

[![Last Monthly Build](https://github.com/d3b-center/bixtools/actions/workflows/monthly_build_check_dockers.yml/badge.svg)](https://github.com/d3b-center/bixtools/actions/workflows/monthly_build_check_dockers.yml)

[![Last Monthly Pull](https://github.com/d3b-center/bixtools/actions/workflows/monthly_pull_check_dockers.yml/badge.svg)](https://github.com/d3b-center/bixtools/actions/workflows/monthly_pull_check_dockers.yml)

Below is a list of the current docker images the command to pull them.


image | version | pull command
------- | ------ | ------------
add-strelka2-fields|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/add-strelka2-fields:1.0.0
annoFuse|0.90.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/annofuse:0.90.0
annoFuse|0.91.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/annofuse:0.91.0
annoFuse|0.92.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/annofuse:0.92.0
annotsv|3.1.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/annotsv:3.1.1
annovar|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/annovar:latest
arriba|1.0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/arriba:1.0.1
arriba|1.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/arriba:1.1.0
arriba|2.2.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/arriba:2.2.1
arriba|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/arriba:latest
autopvs1|v1.0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/autopvs1:v1.0.1
bcbio|variation_recall-0.2.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/bcbio:variation_recall-0.2.4
bed_tools|bedopsv2.4.36_plus_bedtools|docker pull pgc-images.sbgenomics.com/d3b-bixu/bed_tools:bedopsv2.4.36_plus_bedtools
BIC-seq2|0.7.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/bic-seq2:0.7.2
bvcftools|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/bvcftools:latest
bwa-bundle|0.1.17|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa-bundle:0.1.17
bwa-picard|broad|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa-picard:broad
bwa-picard|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa-picard:latest
bwa-samtools|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa-samtools:latest
bwa|0.7.15-r1140|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa:0.7.15-r1140
bwa|0.7.17-r1188|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa:0.7.17-r1188
bwa|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/bwa:latest
canvas|1.11.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/canvas:1.11.0
cellranger|3.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/cellranger:3.1
cellranger|5.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/cellranger:5.0
cellranger|6.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/cellranger:6.0
cellranger|6.1.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/cellranger:6.1.2
cnvnator|v0.4.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/cnvnator:v0.4.1
codex2|3.8|docker pull pgc-images.sbgenomics.com/d3b-bixu/codex2:3.8
consensus-merge|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/consensus-merge:1.0.0
consensus-merge|1.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/consensus-merge:1.1.0
controlfreec|11.5|docker pull pgc-images.sbgenomics.com/d3b-bixu/controlfreec:11.5
cutadapt|3.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/cutadapt:3.4
cutadapt|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/cutadapt:latest
cutesv|1.0.13|docker pull pgc-images.sbgenomics.com/d3b-bixu/cutesv:1.0.13
cutesv|2.0.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/cutesv:2.0.3
fastqc|v0.11.9|docker pull pgc-images.sbgenomics.com/d3b-bixu/fastqc:v0.11.9
freebayes|v1.3.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/freebayes:v1.3.1
freebayes|v1.3.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/freebayes:v1.3.2
FusionAnnotator|0.1.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/fusionannotator:0.1.1
FusionCatcher|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/fusioncatcher:latest
gatk-picard|4.0.1.2-2.8.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk-picard:4.0.1.2-2.8.3
gatk-picard|4.beta.1-2.8.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk-picard:4.beta.1-2.8.3
gatk|3.5-0-g36282e4|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:3.5-0-g36282e4
gatk|3.6-0-g89b7209|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:3.6-0-g89b7209
gatk|3.8|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:3.8
gatk|3.8_ubuntu|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:3.8_ubuntu
gatk|4.0.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.0.1.0
gatk|4.0.1.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.0.1.2
gatk|4.0.12.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.0.12.0
gatk|4.0.5.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.0.5.2
gatk|4.1.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.1.1.0
gatk|4.1.7.0R|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.1.7.0R
gatk|4.2.0.0R|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.2.0.0R
gatk|4.beta.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.1
gatk|4.beta.1-3.5|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.1-3.5
gatk|4.beta.5|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.5
gatk|4.beta.5-tabix|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.5-tabix
gatk|4.beta.6|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.6
gatk|4.beta.6-tabix|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:4.beta.6-tabix
gatk|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/gatk:latest
gistic|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/gistic:latest
hisat2|2.2.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/hisat2:2.2.1
hotspots|0.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/hotspots:0.1.0
intervar|v2.2.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/intervar:v2.2.1
kf_vcf2maf|v1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/kf_vcf2maf:v1.0.0
kf_vcf2maf|v1.0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/kf_vcf2maf:v1.0.1
kf_vcf2maf|v1.0.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/kf_vcf2maf:v1.0.2
kf_vcf2maf|v1.0.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/kf_vcf2maf:v1.0.3
lancet|1.0.7|docker pull pgc-images.sbgenomics.com/d3b-bixu/lancet:1.0.7
lancet|1.1.x|docker pull pgc-images.sbgenomics.com/d3b-bixu/lancet:1.1.x
LinkedSV|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/linkedsv:latest
LOH|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/loh:1.0.0
LOH|1.0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/loh:1.0.1
loompy|2.0.16|docker pull pgc-images.sbgenomics.com/d3b-bixu/loompy:2.0.16
lumpy-sv|0.2.13|docker pull pgc-images.sbgenomics.com/d3b-bixu/lumpy-sv:0.2.13
lumpy-sv|0.3.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/lumpy-sv:0.3.0
manta|1.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/manta:1.4
manta|1.6.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/manta:1.6.0
mend_qc|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/mend_qc:latest
msisensor|1.1.a|docker pull pgc-images.sbgenomics.com/d3b-bixu/msisensor:1.1.a
ngscheckmate|1.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/ngscheckmate:1.3
octopus|0.6.3-beta|docker pull pgc-images.sbgenomics.com/d3b-bixu/octopus:0.6.3-beta
pbta-splicing|0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/pbta-splicing:0.1
peddy|v0.4.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/peddy:v0.4.2
peddy|v0.4.7|docker pull pgc-images.sbgenomics.com/d3b-bixu/peddy:v0.4.7
picard-r|picard2.15.0-r.3.3.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard-r:picard2.15.0-r.3.3.3
picard-r|picard2.8.3-r3.3.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard-r:picard2.8.3-r3.3.3
picard|2.14.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.14.0
picard|2.15.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.15.0
picard|2.17.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.17.4
picard|2.18.9|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.18.9
picard|2.18.9R|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.18.9R
picard|2.8.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:2.8.3
picard|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/picard:latest
pizzly|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/pizzly:latest
PureCN|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/purecn:latest
pypy|3|docker pull pgc-images.sbgenomics.com/d3b-bixu/pypy:3
pyspark|3.1.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/pyspark:3.1.2
python|2.7.13|docker pull pgc-images.sbgenomics.com/d3b-bixu/python:2.7.13
python|3.9-canine-util|docker pull pgc-images.sbgenomics.com/d3b-bixu/python:3.9-canine-util
sambamba|0.6.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/sambamba:0.6.3
sambamba|0.7.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/sambamba:0.7.1
samtools|1.15.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:1.15.1
samtools|1.3.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:1.3.1
samtools|1.6|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:1.6
samtools|1.7-11-g041220d|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:1.7-11-g041220d
samtools|1.9|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:1.9
samtools|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/samtools:latest
sanger|caveman-pindel|docker pull pgc-images.sbgenomics.com/d3b-bixu/sanger:caveman-pindel
scrublet|0.2.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/scrublet:0.2.3
sentieon|202112.01_hifi|docker pull pgc-images.sbgenomics.com/d3b-bixu/sentieon:202112.01_hifi
seqkit|2.3.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/seqkit:2.3.1
sequenza|3.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/sequenza:3.0.0
seurat|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/seurat:latest
smoove|0.2.5|docker pull pgc-images.sbgenomics.com/d3b-bixu/smoove:0.2.5
sniffles|2.0.3|docker pull pgc-images.sbgenomics.com/d3b-bixu/sniffles:2.0.3
sniffles|2.0.7|docker pull pgc-images.sbgenomics.com/d3b-bixu/sniffles:2.0.7
snpEff|4.3t|docker pull pgc-images.sbgenomics.com/d3b-bixu/snpeff:4.3t
snpEff|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/snpeff:latest
soupx_R|4.1.0_SoupX|docker pull pgc-images.sbgenomics.com/d3b-bixu/soupx_r:4.1.0_SoupX
speedseq|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/speedseq:latest
star|2.6.1d|docker pull pgc-images.sbgenomics.com/d3b-bixu/star:2.6.1d
star|2.7.10a|docker pull pgc-images.sbgenomics.com/d3b-bixu/star:2.7.10a
star|2.7.5a|docker pull pgc-images.sbgenomics.com/d3b-bixu/star:2.7.5a
star|fusion-1.10.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/star:fusion-1.10.1
star|fusion-1.5.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/star:fusion-1.5.0
stranded|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/stranded:1.0.0
strelka|v2.9.10|docker pull pgc-images.sbgenomics.com/d3b-bixu/strelka:v2.9.10
sv2|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/sv2:latest
svaba|1.1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/svaba:1.1.0
SVTyper|0.7.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/svtyper:0.7.1
THetA2|0.7.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/theta2:0.7.0
THetA2|0.7.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/theta2:0.7.1
tidyverse|3.6.1-canine-util|docker pull pgc-images.sbgenomics.com/d3b-bixu/tidyverse:3.6.1-canine-util
toolkit_immune_deconvolution|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_immune_deconvolution:1.0.0
toolkit_subtyping|4.1.0R|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_subtyping:4.1.0R
toolkit_subtyping|pyreader0.4.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_subtyping:pyreader0.4.4
toolkit_subtyping|subtyping_v1.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_subtyping:subtyping_v1.0
toolkit_subtyping|subtyping_v1.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_subtyping:subtyping_v1.1
toolkit_tmb|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/toolkit_tmb:1.0.0
tumor-only-benchmarking|1.0.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/tumor-only-benchmarking:1.0.0
VarDictJava|1.5.8|docker pull pgc-images.sbgenomics.com/d3b-bixu/vardictjava:1.5.8
VarDictJava|1.7.0|docker pull pgc-images.sbgenomics.com/d3b-bixu/vardictjava:1.7.0
VarDictJava|fp_filter|docker pull pgc-images.sbgenomics.com/d3b-bixu/vardictjava:fp_filter
vcf_utils|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/vcf_utils:latest
velocyto|0.17.17|docker pull pgc-images.sbgenomics.com/d3b-bixu/velocyto:0.17.17
VEP|r93|docker pull pgc-images.sbgenomics.com/d3b-bixu/vep:r93
VEP|r93.7|docker pull pgc-images.sbgenomics.com/d3b-bixu/vep:r93.7
VEP|r93_v2|docker pull pgc-images.sbgenomics.com/d3b-bixu/vep:r93_v2
VEP|r94|docker pull pgc-images.sbgenomics.com/d3b-bixu/vep:r94
VEP|r98|docker pull pgc-images.sbgenomics.com/d3b-bixu/vep:r98
verifybamid|1.0.1|docker pull pgc-images.sbgenomics.com/d3b-bixu/verifybamid:1.0.1
verifybamid|1.0.2|docker pull pgc-images.sbgenomics.com/d3b-bixu/verifybamid:1.0.2
verifybamid|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/verifybamid:latest
WGSA|latest|docker pull pgc-images.sbgenomics.com/d3b-bixu/wgsa:latest
zumis|2.9.4|docker pull pgc-images.sbgenomics.com/d3b-bixu/zumis:2.9.4
