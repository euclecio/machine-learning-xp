# Algorithm k-Nearest Neighbors
# UDESC - Pattern Recognition project

import sys
import csv
import random
from pprint import pprint
from calcfunctions import euclideanDistance, getNeighbors, getResponse, getAccuracy

def loadDataset(filename):
    classSet = {}
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            # Turn attrs into float except the class name
            nAttrs = len(dataset[x])
            for y in range(nAttrs - 1):
                dataset[x][y] = float(dataset[x][y])
            # Split by class
            className = dataset[x][nAttrs - 1]
            className.replace('\'', '')
            if className not in classSet:
                classSet[className] = []
            classSet[className].append(dataset[x])
    return classSet

def splitSets(filename, trainingZ1Set=[], validationZ2Set=[], testZ3Set=[]):
    classSet = loadDataset(filename)
    trainRate = 0.50
    for key, value in classSet.items():

        # Split instances randomly into train and test sets
        trainSet = []
        for x in range(len(value)):
            if random.random() < trainRate:
                trainSet.append(value[x])
            else:
                testZ3Set.append(value[x])

        # Split instances randomly into train and validation sets
        for instance in trainSet:
            if random.random() < trainRate:
                trainingZ1Set.append(instance)
            else:
                validationZ2Set.append(instance)

def main():
    # Prepare data
    z1TrainingSet = []
    z2ValidationSet = []
    z3TestSet = []
    splitSets('../data/iris.data', z1TrainingSet, z2ValidationSet, z3TestSet)

    print('Train set: ' + repr(len(z1TrainingSet)))
    print('Valid set: ' + repr(len(z2ValidationSet)))
    print('Test set: ' + repr(len(z3TestSet)))

    # Generate predictions
    predictions = []
    k = 3
    descPrediction = '';
    for x in range(len(z2ValidationSet)):
        neighbors = getNeighbors(z1TrainingSet, z2ValidationSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)

        if result != z2ValidationSet[x][-1]:
            row = "[F] Predicted: %s \n    Actual: %s \n" % (repr(result), repr(z2ValidationSet[x][-1]))
        else:
            row = "[T] Predicted: %s \n    Actual: %s \n" % (repr(result), repr(z2ValidationSet[x][-1]))

        descPrediction = descPrediction + row
    print(descPrediction)
    accuracy = getAccuracy(z2ValidationSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()
