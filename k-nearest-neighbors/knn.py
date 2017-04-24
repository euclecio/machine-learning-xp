# Algorithm k-Nearest Neighbors
# UDESC - Pattern Recognition project

import csv
import random
import math
import operator
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

def splitSets(filename, trainingZ1Set=[], trainingZ2Set=[], testZ3Set=[]):
    classSet = loadDataset(filename)
    trainRate = 0.50
    for key, value in classSet.items():
        for x in range(len(value)):
            # Randomly select an instance to add to the set
            if random.random() < trainRate:
                trainingZ1Set.append(value[x])
            else:
                testZ3Set.append(value[x])

    print('Train set: ' + repr(len(trainingZ1Set)))
    print('Test set: ' + repr(len(testZ3Set)))

def main():
    # Prepare data
    z1TrainingSet = []
    z2TrainingSet = []
    z3TestSet = []
    splitSets('../data/iris.data', z1TrainingSet, z2TrainingSet, z3TestSet)

    # print('Train set: ' + repr(len(trainingSet)))
    # print('Test set: ' + repr(len(testSet)))

    # # Generate predictions
    # predictions=[]
    # k = 3
    # table = "| Predicted | Actual |\n";
    # table = table + "| --------- | ------ |\n"
    # for x in range(len(testSet)):
    #     neighbors = getNeighbors(trainingSet, testSet[x], k)
    #     result = getResponse(neighbors)
    #     predictions.append(result)

    #     if result != testSet[x][-1]:
    #         row = "| **%s** | **%s** |\n" % (repr(result), repr(testSet[x][-1]))
    #     else:
    #         row = "| %s | %s |\n" % (repr(result), repr(testSet[x][-1]))

    #     table = table + row
    # # print(table)
    # accuracy = getAccuracy(testSet, predictions)
    # print('Accuracy: ' + repr(accuracy) + '%')

main()
