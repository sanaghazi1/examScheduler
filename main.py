from manipulateData.py import formatStudents,getExams
from ga.py import generatePopulation,evaluatePopulation,evaluateQuality,evolve

def main(studentFile,timeSlots,size,generation):
	"""
	get student information in correct format;
	A list of lists such that each inner list represents information about a single student.
	Each inner list is of size = total exams, with an element = 1 if student is 
	taking that exam and 0 otherwise. 
	"""
	studentInfo = formatStudents(studentFile)
	#obtain num of unique exams
	numExams= len(studentInfo[0])
	#create population
	population = generatePopulation(size,numExams,timeSlots)
	quality_history = []
	for g in range(generation):
		#evaluate each candidate solution
		fitnessOfPopulation = evaluatePopulation(studentInfo,popuation)
		#evaluate quality of solution
		quality = evaluateQuality(fitnessOfPopulation)
		quality_history.append(quality)
		#evolve
		population = evolve(population,fitnessOfPopulation,quality,retainProportion,mutateProbability,timeSlots)



studentFile = ""
#Day 1: 1) 8:30 - 11:30, 2) 1:30 - 4:30, 3) 5:30 - 8:30
#Day 2: 4) 8:30 - 11:30, 5) 1:30 - 4:30, 6) 5:30 - 8:30
#Day 3: 7) 8:30 - 11:30, 8) 1:30 - 4:30, 9) 5:30 - 8:30
#Day 4: 10) 8:30 - 11:30, 11) 1:30 - 4:30, 12) 5:30 - 8:30
#Day 5: 13) 8:30 - 11:30, 14) 1:30 - 4:30, 15) 5:30 - 8:30
#Day 6: 16) 8:30 - 11:30, 17) 1:30 - 4:30, 18) 5:30 - 8:30
timeSlots = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
size = 10
generation = 200

main(studentFile,timeSlots,size,generation)

