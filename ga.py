import random
from evaluationFunctions.py import sameTime,twoInOneDay,consecutive
from evolutionFunctions.py import retain,mutate,reproduce

def generateIndividual(numExams,timeSlots):
	individual = []
	#for each exam, assign an exam time at random from available time slots
	for exam in range(numExams):
		examTime = random.choice(timeSlots)
		individual.append(examTime)


def generatePopulation(popSize,numExams,timeSlots):
	population = []
	#generate candidate solutions (indiviuals) for optimal exam timetable
	for ind in range(popSize)
		individual = generateIndividual(numExams,timeSlots)
		population.append(individual)
	return population


def evaluateFitness(studentInfo,individual):
	totalPenalty = 0
	#determine total penalty for candidate solution based on various evaluate factors
	for student in studentInfo:
		totalPenalty += sameTime(student,individual) + twoInOneDay(student,individual) + consecutive(student,individual)
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
	parents = retain(population,numToRetain,fitnessOfPopulation,quality,retained,parents)
	numChildren = size - numToRetain
	#produce new candidate solutions from those retained to reach full population size
	children =  reproduce(parents,numChildren)
	#mutate some of the parents and chilren to prevent problems of local min/max
	newPopulation = mutate(parents,children,mutateProbability,timeSlots)
	return newPopulation



















