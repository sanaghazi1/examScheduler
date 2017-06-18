import random
from evaluationFunctions import sameTime,twoInOneDay,consecutive
from evolutionFunctions import retain,mutate,reproduce

def generateIndividual(numExams,timeSlots):
	individual = []
	#for each exam, assign an exam time at random from available time slots
	for exam in range(numExams):
		examTime = random.choice(timeSlots)
		individual.append(examTime)
	return individual


def generatePopulation(popSize,numExams,timeSlots):
	population = []
	#generate candidate solutions (indiviuals) for optimal exam timetable
	for ind in range(popSize):
		individual = generateIndividual(numExams,timeSlots)
		population.append(individual)
	return population


def createTimeSlotDict(solution):
	timeSlotDict = dict()
	for i in range(len(solution)):
		if solution[i] in timeSlotDict:
			timeSlotDict[solution[i]].append(i)
		else:
			timeSlotDict[solution[i]] = [i]
	return timeSlotDict


def evaluateFitness(studentInfo,individual):
	totalPenalty = 0
	timeSlotDict = createTimeSlotDict(individual)
	#determine total penalty for candidate solution based on various evaluation factors
	for studentIdx in range(len(studentInfo)):
		student = studentInfo[studentIdx]
		totalPenalty += sameTime(student,timeSlotDict,individual) + twoInOneDay(student,timeSlotDict,individual) + consecutive(student,timeSlotDict,individual)
	#fitness is inverse of the associated total penalty
	fitness = 1.0 / 1 + totalPenalty
	return fitness


def evaluatePopulation(studentInfo,population):
	popFitness = []
	#evaluate fitness of each candidate solution (individual) in the population
	for ind in range(len(population)):
		fitness = evaluateFitness(studentInfo,population[ind])
		popFitness.append(fitness)
	return popFitness


def evaluateQuality(fitnessOfPopulation):
	quality = 0
	for indFitness in fitnessOfPopulation:
		quality += indFitness
	return quality


def evolve(population,fitnessOfPopulation,quality,retainProportion,mutateProbability,timeSlots):
	size = len(population)
	newPopulation = []
	numToRetain = int(size * retainProportion)
	#select individuals from current generation with probability based on their fitness
	retained = 0
	parents = []
	retain(population,numToRetain,fitnessOfPopulation,quality,retained,parents)
	#produce new candidate solutions from those retained to reach full population size
	numChildren = size - numToRetain
	children =  reproduce(parents,numChildren)
	#mutate some of the parents and chilren to prevent problems of local min/max
	newPopulation = mutate(parents,children,mutateProbability,timeSlots)
	return newPopulation



















