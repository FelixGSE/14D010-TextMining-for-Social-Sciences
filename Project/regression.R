################################################################################
# Preamble
################################################################################

### Clear workspace
rm(list = ls())

### Set general file path
setwd('~/Documents/GSE/Term 3/14D010 Text Mining for Social Sciences/14D010-TextMining-for-Social-Sciences/Project/')

### Load Packages 
if (!require("RColorBrewer")) install.packages("RColorBrewer"); library(RColorBrewer)
if (!require("rjson"))        install.packages("rjson");        library(rjson)
if (!require("tikzDevice"))   install.packages("tikzDevice");   library(tikzDevice)
if (!require("nnet"))         install.packages("nnet");         library(nnet)

### Get auxilliary functions


### Get Data 
full.data <- read.csv('frame.csv')

### Reset wd to report 
setwd('TeX/Pictures/')

################################################################################

################################################################################






################################################################################

################################################################################