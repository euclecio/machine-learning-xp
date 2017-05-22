# Algorithm k-Nearest Neighbors
### UDESC - Pattern Recognition project

Projeto de desenvolvimento e implementação de um classificador kNN (k-Nearest Neighbors).

As bases de dados são separadas em três conjunto de dados menores menores proporcionais em número de itens por classe.
De cada classes são 25% para treino, 25% para validação e 50% para teste.

As bases de dados usadas foram encontradas no site http://archive.ics.uci.edu/ml/ e alguns dados foram adaptados para serem processados pelo algoritmo.

No método 1 são feito T iterações salvando o Z1 e sua acurácia, logo depois são trocados as instâncias erradas com uma correspondente da mesma classe, depois apenas o Z1 com melhor acurácia é usado para a base de testes
No método 2 o Z1 é salvo também o junto com melhor k (entre 3 e 13), isto é, o k com melhor acurácia, depois segue como o método 1

### Resultados:
- [Iris Data Set](/k-nearest-neighbors/result/iris.md)
- [Wine Data Set](/k-nearest-neighbors/result/wine.md)
- [Contraceptive Method Choice Data Set](/k-nearest-neighbors/result/cmc.md)
- [Car Evaluation Data Set](/k-nearest-neighbors/result/car-evaluation.md)
