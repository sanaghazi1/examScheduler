def sameTime(student,timeSlotDict,solution):
	penalty = 0
	accountFor = []
	for index in range(len(student)):
		takingExam = student[index]
		if takingExam:
			time = solution[index]
			if time in accountFor:
				continue
			else:
				accountFor.append(time)
				if len(timeSlotDict[time]) > 1: #more than 1 exam scheduled at that time
					for exam in timeSlotDict[time]:
						if exam != index:
							takingThisExam = student[exam]
							if takingThisExam:
								penalty += 20
	return penalty


def twoInOneDay(student,timeSlotDict,solution):
	penalty = 0
	accountFor = []
	for index in range(len(student)):
		takingExam = student[index]
		if takingExam:
			time = solution[index]
			day = time[0]
			if day in accountFor:
				continue
			else:
				for timeSlot in timeSlotDict:
					if timeSlot[0] == day: #timeslots in the same day
						for exam in timeSlotDict[time]:
							if exam != index:
								takingThisExam = student[exam]
								if takingThisExam:
									penalty += 5
	return penalty



def consecutive(student,timeSlotDict,solution):
	penalty = 0
	for index in range(len(student)):
		takingExam = student[index]
		if takingExam:
			time = solution[index]
			try:
				day = time[0]
				interval = int(time[1])
				nextInterval = interval + 1
				newTime = day + str(nextInterval)
				nextTimeSlot = timeSlotDict[newTime]
				for exam in nextTimeSlot:
					takingThisExam = student[exam] #taking consecutive exams
					if takingThisExam:
						penalty += 10
			except:
				continue
	return penalty
	


"""
student = [1,0,0,0,0,1,1,0,1,0] -> 10 exams total, student is taking 4 of them
solution = ["12","12","11","21","13","22","22","13","22","23"]
dict = {"12":0,1 ; "11":2 ; "21":3 ; "13":4,7 ; "22":5,6,8 ; "23":9}
"""
