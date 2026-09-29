marks = [85, 72, 91, 64, 78]

print(marks)

print(marks[0])
print(marks[-1])

marks[-2] = 70

print(marks)

marks.pop(1)

print(marks)

print(len(marks))

print( 91 in marks)

marks.sort()
print(marks)

print(marks[-1])

print(marks[0])

average_mark = sum(marks) / len(marks)
print(average_mark)
