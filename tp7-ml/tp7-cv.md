# Código utilizado

```{r}
# INCISO A
create_folds <- function (dataFrame, k) {
  #Obtiene el tamano del fold
  foldsLenght <- dataFrame %>% nrow() / k %>% ceiling()
  #Divide el data frame en k folds
  value <- split(dataFrame, sample(rep(1:k,foldsLenght)))
  return(value)
}

# INCISO B
cross_validation <- function (dataFrame, nFolds){
  #Dividimos el conjunto de entrenamiento
  folds <- create_folds(dataFrame, nFolds)
  
  #Decidiremos si un arbol tiene inclincacion peligrosa a partir de las variables seleccionadas
  train_formula<- formula(inclinacion_peligrosa ~ especie + altura + diametro_tronco)

  #Valores a retornar
  itera <- NULL
  tp <- NULL
  tn <- NULL
  fp <- NULL
  fn <- NULL
  specifity <- NULL
  sensivity <- NULL
  accuracy <- NULL
  precision_ <- NULL
  
  #Por cada fold a analizar
  for(i in 1:nFolds){
    #Selecciona el conjunto de entrenamiento y test
    dataTrain <- folds[-i] %>% combine()
    dataTest <- folds[i] %>% toDataFrame()
    
    #Entrena el modelo
    data_model <- rpart(train_formula,data=dataTrain, method = "class")

    # obtenemos la predicción
    prediction_class <- predict(data_model, dataTest, type="class")
    
    #Calcula los resultados a devolver
    compare <- data.frame(inclinacion_peligrosa = dataTest$inclinacion_peligrosa, prediction_class)
    results <- dataMatrix(compare)
    
    itera[i] = i
    tp[i] = results$value[1]
    tn[i] = results$value[2]
    fp[i] = results$value[3]
    fn[i] = results$value[4]
    specifity[i] = results$value[5]
    sensivity[i] = results$value[6]
    accuracy[i] = results$value[7]
    precision_[i] = results$value[8]
  }
  return(data.frame(
    itera,
    true_positives = tp,
    true_negatives = tn,
    false_positives = fp,
    false_negatives = fn,
    specifity, 
    sensivity, 
    accuracy, 
    precision = precision_
    ))
}

#Combina una lista con dataframes
combine <- function (dataList) {
  dim <- length(dataList)
  initData <- toDataFrame(dataList[1])
  for (v in dataList[2:dim]){
    initData <- rbind(initData, v)
  }
  return(initData)
}
toDataFrame <- function (dataFrame){
  for(v in dataFrame){return(v)}
}
```
# Métricas alcanzadas cuando se divide el conjunto en 10.

<table class="default">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <tr bgcolor="#666666">
    <td align="center">Iteración</td>
    <td align="center">True positive</td>
    <td align="center">True negative</td>
    <td align="center">False positive</td>
    <td align="center">False negative</td>
    <td align="center">Specifity</td>
    <td align="center">Sensitivity</td>
    <td align="center">Accuracy</td>
    <td align="center">Precision</td>
  </tr>
  <tr >
    <td align="center">1</td>
    <td align="center">293</td>
    <td align="center">320</td>
    <td align="center">157</td>
    <td align="center">147</td>
    <td align="center">0.6659091</td>
    <td align="center">158</td>
    <td align="center">0.6684842</td>
    <td align="center">0.651111</td>
  </tr>
  <tr >
    <td align="center">2</td>
    <td align="center">280</td>
    <td align="center">324</td>
    <td align="center">158</td>
    <td align="center">155</td>
    <td align="center">0.6436782</td>
    <td align="center">159</td>
    <td align="center">0.6586696</td>
    <td align="center">0.639269</td>
  </tr>
  <tr >
    <td align="center">3</td>
    <td align="center">323</td>
    <td align="center">310</td>
    <td align="center">148</td>
    <td align="center">136</td>
    <td align="center">0.7037037</td>
    <td align="center">149</td>
    <td align="center">0.6902944</td>
    <td align="center">0.685774</td>
  </tr>
  <tr >
    <td align="center">4</td>
    <td align="center">301</td>
    <td align="center">321</td>
    <td align="center">153</td>
    <td align="center">145</td>
    <td align="center">0.6748879</td>
    <td align="center">154</td>
    <td align="center">0.6760870</td>
    <td align="center">0.662995</td>
  </tr>
  <tr >
    <td align="center">5</td>
    <td align="center">330</td>
    <td align="center">313</td>
    <td align="center">143</td>
    <td align="center">135</td>
    <td align="center">0.7096774</td>
    <td align="center">144</td>
    <td align="center">0.6981542</td>
    <td align="center">0.697674</td>
  </tr>
  <tr >
    <td align="center">6</td>
    <td align="center">338</td>
    <td align="center">305</td>
    <td align="center">144</td>
    <td align="center">131</td>
    <td align="center">0.7206823</td>
    <td align="center">145</td>
    <td align="center">0.7004357</td>
    <td align="center">0.701244</td>
  </tr>
  <tr >
    <td align="center">7</td>
    <td align="center">337</td>
    <td align="center">282</td>
    <td align="center">155</td>
    <td align="center">143</td>
    <td align="center">0.7020833</td>
    <td align="center">156</td>
    <td align="center">0.6750273</td>
    <td align="center">0.684959</td>
  </tr>
  <tr >
    <td align="center">8</td>
    <td align="center">315</td>
    <td align="center">309</td>
    <td align="center">141</td>
    <td align="center">152</td>
    <td align="center">0.6745182</td>
    <td align="center">142</td>
    <td align="center">0.6804798</td>
    <td align="center">0.690789</td>
  </tr>
  <tr >
    <td align="center">9</td>
    <td align="center">315</td>
    <td align="center">315</td>
    <td align="center">148</td>
    <td align="center">139</td>
    <td align="center">0.6938326</td>
    <td align="center">149</td>
    <td align="center">0.6870229</td>
    <td align="center">0.680345</td>
  </tr>
  <tr >
    <td align="center">10</td>
    <td align="center">334</td>
    <td align="center">304</td>
    <td align="center">150</td>
    <td align="center">130</td>
    <td align="center">0.7198276</td>
    <td align="center">151</td>
    <td align="center">0.6949891</td>
    <td align="center">0.690082</td>
  </tr>
  <tr bgcolor="#666666">
    <td align="center">Media</td>
    <td align="center">319</td>
    <td align="center">310.3</td>
    <td align="center">149.7</td>
    <td align="center">141.3</td>
    <td align="center">0.69088</td>
    <td align="center">150.7</td>
    <td align="center">0.68296</td>
    <td align="center">0.67842</td>
  </tr>
  <tr bgcolor="#555555">
    <td align="center">Desviación estándar</td>
    <td align="center">19.83935</td>
    <td align="center">12.00046</td>
    <td align="center">5.96378</td>
    <td align="center">8.55115</td>
    <td align="center">0.02528</td>
    <td align="center">5.96378</td>
    <td align="center">0.01361</td>
    <td align="center">0.02054</td>
  </tr>
</table>



























































































































































































































