from createStudentInfo import createInformation
#from manipulateData import formatStudents,getExams
from ga import generatePopulation,evaluatePopulation,evaluateQuality,evolve

def main(numStudents,courses,minEnrollment,maxEnrollment,timeSlots,popSize,generation):
	"""
	get student information in correct format;
	A list of lists such that each inner list represents information about a single student.
	Each inner list is of size = total exams, with an element = 1 if student is 
	taking that exam and 0 otherwise. 
	"""
	studentInfo,studentCourses = createInformation(numStudents,courses,minEnrollment,maxEnrollment)
	#obtain num of unique exams
	numExams= len(studentInfo[0])
	#create population
	population = generatePopulation(popSize,numExams,timeSlots)
	quality_history = []
	#GA parameters
	retainProportion = 0.5
	mutateProbability = 0.02
	gaPerformance = dict()
	for g in range(generation):
		# print("-------------g-----------")
		# print(g)
		#evaluate each candidate solution
		fitnessOfPopulation = evaluatePopulation(studentInfo,population)
		gaPerformance[g] = fitnessOfPopulation
		#evaluate quality of solution
		quality = evaluateQuality(fitnessOfPopulation)
		quality_history.append(quality)
		#print(quality_history)
		# print(quality_history)
		#evolve
		population = evolve(population,fitnessOfPopulation,quality,retainProportion,mutateProbability,timeSlots)
	return quality_history



studentFile = ""
courses = ["Discrete Math","Operations Research","Real Analysis","Number Theory",
			"Algebraic Structures","Graph Theory","Cryptography","Multivariate Analysis",
			"Matrix Theory","Differential Equations","Numerical Methods","Combinatorics",
			"Discrete Time Finance","Concepts of Mathematics","Basic Logic","Probability"]
numStudents = 75
minEnrollment = 3
maxEnrollment = 6
#Day 1: 1) 8:30 - 11:30, 2) 1:30 - 4:30, 3) 5:30 - 8:30
#Day 2: 4) 8:30 - 11:30, 5) 1:30 - 4:30, 6) 5:30 - 8:30
#Day 3: 7) 8:30 - 11:30, 8) 1:30 - 4:30, 9) 5:30 - 8:30
#Day 4: 10) 8:30 - 11:30, 11) 1:30 - 4:30, 12) 5:30 - 8:30
#Day 5: 13) 8:30 - 11:30, 14) 1:30 - 4:30, 15) 5:30 - 8:30
#Day 6: 16) 8:30 - 11:30, 17) 1:30 - 4:30, 18) 5:30 - 8:30
timeSlots = ["11","12","13","21","22","23","31","32","33","41","42","43"]
size = 10
generation = 100

main(numStudents,courses,minEnrollment,maxEnrollment,timeSlots,size,generation)

