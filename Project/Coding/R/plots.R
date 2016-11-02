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
if (!require("stargazer"))    install.packages("stargazer");    library(stargazer)


### Get auxilliary functions

### Reset wd to report 
setwd('TeX/Pictures/')

# Color Set
co <- 1/255 
pers.green      <- rgb( co *  14 ,  co * 105 , co *  90 )
pers.blue       <- rgb( co *  22 ,  co *  54 , co *  92 )
pers.red        <- rgb( co *  99 ,  co *  37 , co *  35 )
pers.gray       <- rgb( co * 150 ,  co * 150 , co * 150 )
pers.orange     <- rgb( co * 186 ,  co *  85 , co *  59 )
pers.beige      <- rgb( co * 196 ,  co * 189 , co * 151 )
full.color.set  <- list( pers.green , pers.blue, pers.red,
                         pers.gray, pers.orange, pers.beige 
) 

################################################################################

################################################################################

top   <- read.csv('top10.csv',header = TRUE)

N01   <- nrow(top)
M01   <- ncol(top) 
rownames(top) <- top[,1]
colnames(top) <- c('NONE','nothing','gold','platinum','rowsum') 
top5 <- t(as.matrix(tail(top)[,2:(M01-1)]))[1:3,]


top5
tikz("barchart.tex",width = 3.5, height = 3.5)

p <- barplot(top5, col=c(pers.gray,pers.blue,pers.green),beside=TRUE,legend=NULL,
             ylim=c(0,25),cex.lab=0.5,cex.axis=0.5,cex.lab=0.5,
             mgp=c(0.5,0.1,0),tck=-0.01,cex.names=0.5)
text(x = p, y = top5, label = top5, pos = 3, cex = 0.5, col = "black")
legend("topleft",legend = c("Not awarded", "Gold","Platinum"),pch = c(15, 15, 15),
       pt.bg="white",col=c(pers.gray,pers.blue,pers.green),bty="n",cex=0.7)
box()

dev.off()


################################################################################
# Artist award distribution
################################################################################

temp <- top[-2,2:4]

none <- temp[,1]
gold <- temp[,2]
plat <- temp[,3]


tikz("powerlaw.tex",width = 3.5, height = 3.5)

hist(none,breaks = 40,col=rgb(0,0,1,1/4),xlim=c(0,23),ylim=c(0,400),
     ylab='Artist Frequency',xlab='Number of arwards',main='',cex.lab=0.5,cex.axis=0.5,
     mgp=c(1,0.1,0),tck=-0.01)
hist(gold,width=0.33,offset=2,add=TRUE,breaks = 10,col=rgb(1,0,0,1/4))
hist(plat,width=0.33,offset=2,add=TRUE,breaks = 40,col=rgb(0,1,0,1/4))

legend("topright",legend = c("Not awarded", "Gold","Platinum"),pch = c(15, 15, 15),
       pt.bg="white",col=c(rgb(0,0,1,1/4),rgb(1,0,0,1/4),rgb(0,1,0,1/4)),bty="n",cex = 0.7,
       ncol = 1)
box()
dev.off()

################################################################################
# 
################################################################################

seq <- fromJSON(file='seq.txt', method='C')
nb  <- fromJSON(file='nb02.txt', method='C')
rf  <- fromJSON(file='rf02.txt', method='C')
svm <- fromJSON(file='svm02.txt', method='C')
ada <- fromJSON(file='ada02.txt', method='C')
knn <- fromJSON(file='knn02.txt', method='C')

df <- cbind(rbind(nb,knn,svm,ada,rf),0)
rnames <- c('Naive Bayes','K-NN','SVM','ADA-Boost','Random Forest')
cnames <- c(seq,"Full Model")
rownames(df) <- rnames
colnames(df) <- cnames
dim(df)
length(cnames)
stargazer(df,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=TRUE,colnames = TRUE)

df2 <- as.data.frame(df)[,-c(2,3,13:19,ncol(df))]
stargazer(df2,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=TRUE,colnames = TRUE)

sapply(1:nrow(df),function(i){which.max(  as.numeric(unlist(list(df2[i,])))) })

