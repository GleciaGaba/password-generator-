"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91

"""

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

student_scores = sorted(student_scores)

print(f"The highest score in the class is: {student_scores[-1]}")

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


student_score = input().split()
for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])

highest_score = 0
for score in student_score:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")






