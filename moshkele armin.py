def calculate_grade(n, grades):
  total_weighted_grade = 0
  total_weight = 0
  for weight, grade in grades:
    total_weighted_grade += weight * grade
    total_weight += weight

  average_grade = total_weighted_grade / total_weight

  # Convert average grade to letter grade
  if average_grade >= 4:
    return 'A'
  elif average_grade >= 3:
    return 'B'
  elif average_grade >= 2:
    return 'C'
  elif average_grade >= 1:
    return 'D'
  else:
    return 'F'

# Get input from the user
n = int(input())
grades = []
for _ in range(n):
  weight, grade = input().split()
  grades.append((int(weight), int(grade)))

# Calculate and print the average grade
average_grade = calculate_grade(n, grades)
print(average_grade)
