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
        # Shuffle randomly the instances
        random.shuffle(dataset)
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
    times = 0
    for key, value in classSet.items():
        times += 1
        # Split instances z1, z2 and z3 sets
        quarter = len(value) * 0.25 * times
        for x in range(len(value)):
            if len(trainingZ1Set) <= quarter:
                trainingZ1Set.append(value[x])
            elif len(validationZ2Set) <= quarter:
                validationZ2Set.append(value[x])
            else:
                testZ3Set.append(value[x])

def exchangeEquivalentInstances(z1TrainingSet, z2ValidationSet, wrongPredictions):
    for x in wrongPredictions:
        wrongInstance = z2ValidationSet[x]
        for key in range(len(z1TrainingSet)):
            if z1TrainingSet[key][-1] == wrongInstance[-1]:
                newInstance = z1TrainingSet[key]
                z1TrainingSet[key] = z2ValidationSet[x]
                z2ValidationSet[x] = newInstance


def main():
    # Prepare data
    z1TrainingSet = []
    z2ValidationSet = []
    z3TestSet = []
    splitSets('../data/iris.data', z1TrainingSet, z2ValidationSet, z3TestSet)

    print('Train set: ' + repr(len(z1TrainingSet)))
    print('Valid set: ' + repr(len(z2ValidationSet)))
    print('Test set: ' + repr(len(z3TestSet)))
    print('\n')

    # Generate predictions
    k = 4
    t = len(z1TrainingSet) + len(z2ValidationSet)

    # Improve z1 changing wrongly predicted instances
    z1List = []
    for iteration in range(t):
        predictions = []
        wrongPredictions = []
        for x in range(len(z2ValidationSet)):
            neighbors = getNeighbors(z1TrainingSet, z2ValidationSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)

            # If z2 instance was predicted wrongly, then change by z1 instance with same class
            if result != z2ValidationSet[x][-1]:
                wrongPredictions.append(x)

        result = getAccuracy(z2ValidationSet, predictions)
        newZ1 = {
            'dataset': z1TrainingSet,
            'accuracy': result['accuracy']
        }
        z1List.append(newZ1)
        exchangeEquivalentInstances(z1TrainingSet, z2ValidationSet, wrongPredictions)

    # Find best Z1
    bestZ1 = z1List[0]
    for x in range(len(z1List)):
        if z1List[x]['accuracy'] > bestZ1['accuracy']:
            bestZ1 = z1List[x]
    bestZ1 = bestZ1['dataset']

    # Now run with train set
    predictions = []
    for x in range(len(z3TestSet)):
        neighbors = getNeighbors(bestZ1, z3TestSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)

    result = getAccuracy(z3TestSet, predictions)
    print('Correct: ' + repr(result['correct']))
    print('Wrong: ' + repr(result['wrong']))
    print('Accuracy: ' + repr(result['accuracy']) + '%')
    print('\n')

main()
