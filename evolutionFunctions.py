import random

def retain(population,numToRetain,fitnessOfPopulation,quality,retained,parents):
	#recursively call function until number of candidate solutions selected is equal to numToRetain
	#print (retained,numToRetain)
	#print parents
	if retained == numToRetain:
		return parents
	else:
		for ind in range(len(population)):
			if retained >= numToRetain:
				break
			individual = population[ind] # candidate solution
			fitness  = fitnessOfPopulation[ind] #fitness of individual
			p = fitness / quality #greater the fitness, higher the chance of being selected
			if p >= random.random():
				if individual not in parents:
					parents.append(individual)
					retained += 1
		#print(parents)
		retain(population,numToRetain,fitnessOfPopulation,quality,retained,parents)


def reproduce(parents,numChildren):
	childrenAdded = 0
	children = []
	while childrenAdded < numChildren:
		#pick any 2 candidate solutions from the parent list
		parent1 = random.choice(parents)
		parent2 = random.choice(parents)
		if parent1 != parent2:
			half = len(parent1)/2
			#perform a crossover operation to obtain child
			child = parent1[:half] + parent2[half:]
			children.append(child)
			childrenAdded += 1
	return children


def mutate(parents,children,mutateProbability,timeSlots):
	population = parents + children
	#mutate some candidate solutions at random
	for ind in population:
		if mutateProbability > random.random():
			posToMutate = random.randint(0,len(ind) - 1)
			ind[posToMutate] = random.choice(timeSlots)
	return population

