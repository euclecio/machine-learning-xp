# -*- coding: utf-8 -*-
# Algorithm k-Nearest Neighbors
# UDESC - Pattern Recognition project

import sys
from pprint import pprint
from calcfunctions import euclideanDistance, getNeighbors, getResponse, getAccuracy
from datasetfunctions import splitSets, exchangeEquivalentInstances

# Improve z1 changing wrongly predicted instances
def getBestZ1(k, t, z1TrainingSet, z2ValidationSet):
    z1List = []
    for iteration in range(t):
        predictions = []
        wrongPredictions = []
        for x in range(len(z2ValidationSet)):
            neighbors = getNeighbors(z1TrainingSet, z2ValidationSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)

            if result != z2ValidationSet[x][-1]:
                wrongPredictions.append(x)

        result = getAccuracy(z2ValidationSet, predictions)
        newZ1 = {
            'dataset': z1TrainingSet,
            'accuracy': result['accuracy']
        }
        z1List.append(newZ1)
        # If z2 instance was predicted wrongly, then change by z1 instance with same class
        exchangeEquivalentInstances(z1TrainingSet, z2ValidationSet, wrongPredictions)

    # Find best Z1
    bestZ1 = z1List[0]
    for x in range(len(z1List)):
        if z1List[x]['accuracy'] > bestZ1['accuracy']:
            bestZ1 = z1List[x]
    bestZ1 = bestZ1['dataset']
    return bestZ1

def run(cont):
    # Prepare data
    row = ''
    z1TrainingSet = []
    z2ValidationSet = []
    z3TestSet = []
    splitSets('../data/wine.data', z1TrainingSet, z2ValidationSet, z3TestSet)

    row += '|' + repr(len(z1TrainingSet))
    row += '|' + repr(len(z2ValidationSet))
    row += '|' + repr(len(z3TestSet))

    # Generate predictions
    k = 4
    t = 50
    bestZ1 = getBestZ1(k, t, z1TrainingSet, z2ValidationSet)

    # Now run with train set
    predictions = []
    for x in range(len(z3TestSet)):
        neighbors = getNeighbors(bestZ1, z3TestSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)

    result = getAccuracy(z3TestSet, predictions)

    row += '|' + repr(result['correct'])
    row += '|' + repr(result['wrong'])
    row += '|' + repr(round(result['accuracy'], 4)) + '%'

    return ('|' + repr(cont) + row + '|\n')

cont = 1
rows = ''
for iteration in range(15):
    rows += run(cont)
    cont += 1

print('| Nº | Train set | Valid set | Test set | Correct | Wrong | Accuracy |')
print('|----|-----------|-----------|----------|---------|-------|----------|')
print(rows)
