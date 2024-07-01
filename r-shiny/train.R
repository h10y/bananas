library(e1071)

#' Read the bananas data
x <- read.csv("r-shiny/bananas.csv")
x$ripeness <- factor(x$ripeness, c("Under", "Ripe", "Very", "Over"))

#' Multinomial classification with Support Vector Machines
m <- svm(ripeness ~ green + yellow + brown,
  data = x,
  probability = TRUE
)

#' Two-way table to test prediction accuracy
table(x$ripeness, predict(m))
sum(diag(table(x$ripeness, predict(m)))) / nrow(x)

#' Predict ripeness class
predict(m, data.frame(green = 1, yellow = 0, brown = 0), probability = TRUE)
predict(m, data.frame(green = 0, yellow = 1, brown = 0), probability = TRUE)
predict(m, data.frame(green = 0, yellow = 0, brown = 1), probability = TRUE)
predict(m, data.frame(green = 0.1, yellow = 0.2, brown = 0.7), probability = TRUE)

#' Save the model object
saveRDS(m, "r-shiny/bananas-svm.rds")
