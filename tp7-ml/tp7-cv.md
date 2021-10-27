```{r}
create_folds <- function (dataFrame, k) {
  #Obtiene el tamano del fold
  foldsLenght <- dataFrame %>% nrow() / k %>% ceiling()
  #Divide el data frame en k folds
  value <- split(dataFrame, sample(rep(1:k,foldsLenght)))
  return(value)
}




```