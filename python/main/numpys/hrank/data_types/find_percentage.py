'''
You have a record of  students. Each record contains the student's name, and their percent marks in Maths,
 Physics and Chemistry.
The marks can be floating values. The user enters some integer  followed by the names and marks for
 students. You are required to save the record in a dictionary data type.
 The user then enters a student's name. Output the average percentage marks obtained by that student,
 correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next
 lines contains the name and marks obtained by that student separated by
  a space. The final line contains the name of a particular student previously listed.
input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

output
56.00

'''

# lista=[list(map(int,input().split())) for i in range([int(a_temp) for a_temp in input().strip().split(' ')][0])]


N = int(input())
students = {}
for num in range(N):
    data = input().strip().split(' ')
    students[data.pop(0)] = data

name = str(input())
numbers = list(map(float, students[name]))

count = sum(numbers) / len(numbers)
print("{:.2f}".format(count))

# list(map(int, data))
