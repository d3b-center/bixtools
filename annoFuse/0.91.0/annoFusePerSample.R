#install.packages("/opt/formatFusionCalls/annoFuse_0.90.0.tar.gz",repos = NULL)
library("annoFuse")

suppressPackageStartupMessages(library("readr"))
suppressPackageStartupMessages(library("tidyverse"))
suppressPackageStartupMessages(library("reshape2"))
suppressPackageStartupMessages(library("optparse"))

option_list <- list(
  make_option(c("-a", "--fusionfileArriba"),type="character",
              help="Formatted fusion calls from arriba"),
  make_option(c("-s", "--fusionfileStarFusion"),type="character",
              help="Formatted fusion calls from starfusion"),
  make_option(c("-e", "--expressionFile"),type="character",
              help="RSEM file for sample"),
  make_option(c("-t", "--tumorID"),type="character",
              help="Sample name to rename column in RSEM FPKM column"),
  make_option(c("-o","--outputfile"),type="character",
              help="Formatted and filtered fusion calls from [STARfusion | Arriba] (.TSV)")
)

#read in caller results
opt <- parse_args(OptionParser(option_list=option_list))
Arribainputfile <- opt$fusionfileArriba
STARFusioninputfile <- opt$fusionfileStarFusion
expressionFile<-opt$expressionFile
tumorID<-opt$tumorID
outputfile <- opt$outputfile

standardFusioncalls <- annoFuse::annoFuse_single_sample(
   # Example files are provided in extdata, at-least 1 fusionfile is required along 
   # with its rsem expression file
   fusionfileArriba = Arribainputfile,
   fusionfileStarFusion = STARFusioninputfile,
   expressionFile = expressionFile,
   tumorID = tumorID,
   # multiple read flag values for filtering using FusionAnnotator values
   artifactFilter = "GTEx_Recurrent|DGD_PARALOGS|Normal|BodyMap",
   # keep all in-frame , frameshift and other types of Fusion_Type
   readingFrameFilter = "in-frame|frameshift|other",
   # keep all fusions with atleast 1 junction read support
   junctionReadCountFilter = 1,
   # keep only fusions where spanningFragCount-junctionReadCountFilter less than equal to 100
   spanningFragCountFilter = 100,
   # filter read throughs
   readthroughFilter = FALSE
)


# write to outputfile
write.table(standardFusioncalls,outputfile,sep="\t",quote=FALSE,row.names = FALSE)
