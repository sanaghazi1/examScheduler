import random

def createInformation(numStudents,courses,minEnrollment,maxEnrollment):
	studentCourseIndex = dict()
	studentCourseName = dict()
	for student in range(numStudents):
		classes = [0] * len(courses)
		courseProfile = [0] * len(courses)
		numToEnroll = random.randint(minEnrollment,maxEnrollment)
		numEnrolled = 0
		while (numEnrolled < numToEnroll):
			courseIndex = random.randint(0,len(courses) - 1)
			course = courses[courseIndex]
			if classes[courseIndex] == 0:
				classes[courseIndex] = 1
				courseProfile[courseIndex] = (course)
				numEnrolled += 1
		studentCourseIndex[student] = classes
		studentCourseName[student] = courseProfile
	return studentCourseIndex,studentCourseName
