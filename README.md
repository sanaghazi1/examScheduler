# examScheduler
Solves variant of MESP using a genetic algorithm (https://www.macs.hw.ac.uk/~dwcorne/cfm.pdf)

Goal:
Create an 'optimal' exam schedule for all students. This entails the most efficient time allocation for all avaialbe courses among all available timeslots. In this example, an optimal schedule is one that minimizes events in which students are 1) scheduled to take multiple exams at the same time, 2) have 2 exams in the same day or 3) have to take consecutive exams 

Inputs:
Number of Students: Total number of students taking all possible exams offered (datatype: int, example : 10)
Courses: List of all courses for which exams need to be scheduled (datatype: list, example: ["English","Math","Science"])
minEnrolment: Minmimum number of courses a student can be enrolled in at any given time (datatype: int, example: 3)
maxEnrollment: Maxiumum number of courses a student can be enrolled in at any given time (datatype: int, example: 5)
timeSlots: All available timeslots for exames to be schedule (datatype: list, example: ["11","12","21","22])
  # 11: (day 1, time 1), 12: (day 1, time 2), 21: (day 2, time 1), 22: (day 2, time 2)
generation: Number of generations the algoirthm iterates through

Algorithm Overview:
1. Randomly generate student information such that each student is asssigned to take n number of exames (where minEnrollment <= n <= maxEnrollment).
2. Randomly generate the first set of potential exam schedules (number of possible options: size). This is generation 0.
3. Determine quality of each of the solutions in current generation
  3a. Penalize each solutution 1) 20 for each student that has multiple exames scheduled for the same time, 2) 5 for each student that has    two exams scheduled for the same day and, 3) 10 for each student scheduled to take consecutive exams
  3b. Determine overall fitness of each solution such that fitness = 1.0/(1 + total penalty) #higher the fitness, the better tha solution
4. Determine and record overall quality of the solutions
5. Generate subsequent population
  5a. Retain half of the candidate solutions from previous generation (parents), favouring those with relatively better fitness quality
  5b. Generate remaining of half new solutions for current generation (children) by combining two randomly selected parent solutions
  5c> Randomly mutate 2% of the new generation to prevent problem of local minima
6. Repeat steps 3-5 for designated number of generations
