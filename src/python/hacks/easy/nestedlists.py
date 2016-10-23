
n = int(input().strip())


rangs = [[input(), float(input())] for _ in range(n)]

second_lowest = sorted(list(set([marks for name, marks in rangs])))[1]

names = []
for name, grade in rangs:
    if grade == second_lowest:
        names.append(name)

names.sort()
for name in names:
    print(name)



# maximum = max(grades)
# current = -1
# prev = -1
# for num in grades:
#     if current < num and maximum > num:
#         prev = current
#         current = num
#
# students = []
# for key, value in rangs.items():
#     if value == prev:
#         students.append(key)
#
# students.sort()
# for name in students:
#     print("{}".format(name))
