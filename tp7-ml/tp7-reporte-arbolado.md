# EJERCICIO 1

Primeramente se eliminaros las variables: ultima_modificacion, long, lat, area_seccion, nombre_seccion, circ_tronco_cm, seccion. 

Luego se dividió el data frame por árboles que tienen inclinación peligrosa y los que no.

Una vez separado el data frame, se duplicaron 1000 elementos al azar del conjunto que tiene inclinación peligrosa resultando un total de aproximadamente 4600 registros y se sekeccionó al azar esa misma cantidad del otro conjunto.

Sobre el conjunto de validación se obtuvieron las siguientes métricas:

<table class="default">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <colgroup bgcolor="#555555">
  <colgroup bgcolor="#444444">
  <tr bgcolor="#666666">
    <td align="center">True positive</td>
    <td align="center">True negative</td>
    <td align="center">False positive</td>
    <td align="center">False negative</td>
    <td align="center">Specifity</td>
    <td align="center">Sensitivity</td>
    <td align="center">Accuracy</td>
    <td align="center">Precision</td>
  </tr>
  <tr>
    <td align="center">1926</td>
    <td align="center">129</td>
    <td align="center">237</td>
    <td align="center">899</td>
    <td align="center">0.6475</td>
    <td align="center">0.6818</td>
    <td align="center">0.6778</td>
    <td align="center">0.9372</td>
  </tr>
</table>

