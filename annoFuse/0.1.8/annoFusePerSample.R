install.packages("/opt/formatFusionCalls/annoFuse_0.1.8.tar.gz",repos = NULL)
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
tumor_id<-opt$tumorID
outputfile <- opt$outputfile

# read files
STARFusioninputfile<-read_tsv(STARFusioninputfile)
Arribainputfile<-read_tsv(Arribainputfile,col_types = readr::cols(breakpoint1 = readr::col_character(),breakpoint2 = readr::col_character()))

# if StarFusion and Arriba files empty execution stops
if(is_empty(STARFusioninputfile$FusionName) & is_empty(Arribainputfile$"gene1--gene2")){
stop("StarFusion and Arriba files empty")
  }

# if StarFusion and Arriba files are not empty
if(!is_empty(STARFusioninputfile$FusionName) & !is_empty(Arribainputfile$"gene1--gene2")){
colnames(Arribainputfile)[27]<-"annots"

# To have a general column with unique IDs associated with each sample
STARFusioninputfile$Sample <- STARFusioninputfile$tumor_id
Arribainputfile$Sample <- Arribainputfile$tumor_id
Arribainputfile$Caller <- "Arriba"
STARFusioninputfile$Caller <- "StarFusion"

# standardized fusion calls
standardizedSTARFusion<-fusion_standardization(fusion_calls = STARFusioninputfile,caller = "STARFUSION")
standardizedArriba<-fusion_standardization(fusion_calls = Arribainputfile,caller = "ARRIBA")

#merge standardized fusion calls
standardFusioncalls<-rbind(standardizedSTARFusion,standardizedArriba) %>% as.data.frame()
}

# if StarFusion file is empty only run standardization for Arriba calls
if(is_empty(STARFusioninputfile$FusionName) & !is_empty(Arribainputfile$"gene1--gene2")){
  warning(paste("No fusion calls in StarFusion : ",opt$fusionfileStarFusion))
  
  colnames(Arribainputfile)[27]<-"annots"
  # To have a general column with unique IDs associated with each sample
  Arribainputfile$Sample <- Arribainputfile$tumor_id
  Arribainputfile$Caller <- "Arriba"
  
  # standardized fusion calls
  standardizedArriba<-fusion_standardization(fusion_calls = Arribainputfile,caller = "ARRIBA")
  
  # standardized fusion calls
  standardFusioncalls<-standardizedArriba %>% as.data.frame()
}

# if Arriba file is empty only run standardization for StarFusion calls
if(!is_empty(STARFusioninputfile$FusionName) & is_empty(Arribainputfile$"gene1--gene2")){
  warning(paste("No fusion calls in StarFusion : ",opt$fusionfileStarFusion))
  
  # To have a general column with unique IDs associated with each sample
  STARFusioninputfile$Sample <- STARFusioninputfile$tumor_id
  STARFusioninputfile$Caller <- "StarFusion"
  
  # standardized fusion calls
  standardizedSTARFusion<-fusion_standardization(fusion_calls = STARFusioninputfile,caller = "STARFUSION")
  
  # standardized fusion calls
  standardFusioncalls<-standardizedSTARFusion %>% as.data.frame()
}




# General fusion QC for read support and red flags
fusionQCFiltered<-fusion_filtering_QC(standardFusioncalls=standardFusioncalls,readingFrameFilter="in-frame|frameshift|other",artifactFilter="GTEx_Recurrent|DGD_PARALOGS|Normal|BodyMap|ConjoinG",junctionReadCountFilter=1,spanningFragCountFilter=100,readthroughFilter=FALSE)

expressionMatrix<-read_tsv(expressionFile)

# split gene id and symbol
expressionMatrix <- expressionMatrix %>% 
  dplyr::mutate(gene_id = str_replace(gene_id, "_PAR_Y_", "_")) 


expressionMatrix <- cbind(expressionMatrix, colsplit(expressionMatrix$gene_id, pattern = '_', names = c("EnsembleID","GeneSymbol")))


# collapse to matrix of HUGO symbols x Sample identifiers
# take max expression per row and use the max value for duplicated gene symbols
expressionMatrix.collapsed <-expressionMatrix  %>% 
  arrange(desc(FPKM)) %>% # arrange decreasing by FPKM
  distinct(GeneSymbol, .keep_all = TRUE) %>% # keep the ones with greatest FPKM value. If ties occur, keep the first occurencce
  unique() %>%
  remove_rownames()  %>%
  dplyr::select(EnsembleID,GeneSymbol,FPKM,gene_id)

# rename columns
colnames(expressionMatrix.collapsed)[3]<-tumor_id

expressionFiltered<-expressionFilterFusion(standardFusioncalls = fusionQCFiltered,expressionFilter = 1,expressionMatrix = expressionMatrix.collapsed)

# write to outputfile
write.table(expressionFiltered,outputfile,sep="\t",quote=FALSE,row.names = FALSE)
