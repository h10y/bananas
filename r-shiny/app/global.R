library(shiny)
library(plotly)
library(e1071)

x <- read.csv("bananas.csv")
x$ripeness <- factor(x$ripeness, c("Under", "Ripe", "Very", "Over"))

m <- readRDS("bananas-svm.rds")
