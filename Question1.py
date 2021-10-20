# Question 1 - Project 1 - SRT211NSA
# Dinh Quy Pham - Yu Huang

import csv

list1 = list()
list2 = list()

# Open file1.csv and process the first column
with open("file1.csv") as csv_1:
    csv_reader1 = csv.reader(csv_1)
    # Use 'next' command to skip the first row "Student ID"
    next(csv_reader1)
    # Add the first column to list 1
    for line1 in csv_reader1:
        list1.append(line1[0])


# Open file2.csv and process the first column
with open("file2.csv") as csv_2:
    csv_reader2 = csv.reader(csv_2)
    # Use 'next' command to skip the first row "Student ID"
    next(csv_reader2)
    # Add the first column to list 2
    for line2 in csv_reader2:
        list2.append(line2[0])


# Filter out duplicate IDs and put it in a list
idIntersection = list(set(list1).intersection(list2))


# Print out the Student ID table in both classes
print("-------------------------------------------------")
print("|          ID STUDENTS IN BOTH CLASSES          |")
print("-------------------------------------------------")

for x in range(len(idIntersection)):
    if x == 0:
        print("|{:>20}".format(idIntersection[x]), end="\t")
        continue
    elif x % 2 != 0:
        print("{:>4}".format(" "), end="")
        print("{:<20}".format(idIntersection[x]), end="")
    else:
        print("|\n|{:>20}".format(idIntersection[x]), end="\t")
print("{:<23}".format(" "), "|")

# Print out the Student ID table not in both classes
print("-------------------------------------------------")
print("|        ID STUDENTS NOT IN BOTH CLASSES        |")
print("-------------------------------------------------")

# Put different ID Students of 2 lists into a new list
diffIDStudent = list(set(list1) ^ set(list2))


for x in range(len(diffIDStudent)):
    if x == 0:
        print("|{:>13}".format(diffIDStudent[x]), end="\t")
        continue
    elif x % 3 != 0:
        print("{:>12}".format(diffIDStudent[x]), end="\t")
    else:
        print("|\n|{:>13}".format(diffIDStudent[x]), end="\t")
print("|")
print("-------------------------------------------------")
print()


# Allows users to find students by Student ID
while True :
    name = input("Enter the Student ID : ")
    if name.isdigit():
        break
    else:
        print("Wrong ID, please enter again !")
        continue

# Check which class Student ID is in
if (name in list1) and (name in list2):
    print(f"{name} is appeared in both classes !")
else:
    if name in list1:
        print(f"{name} is only in Class 1 !")
    elif name in list2:
        print(f"{name} is only in Class 2 !")
    else:
        print(f"No student has ID : {name}")
