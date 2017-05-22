
import csv
import random

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
