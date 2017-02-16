'''
list = []

insert i e -> insert integer 'e' at position 'i'
print -> print the list
remove e -> delete the list first occurence of integer e
append e -> insert integer 'e' at the end of of the list
sort -> sort the list
pop -> pop the last element from the list
reverse -> reverse the list

extend(l) -> merge another list 'L' to the end
arr.extend([10, 11])

insert(i,x)

index(x) -> returns the first index of a value int he list. May thrwo an error if not found

count(x) -> counts the number of occurences of an element 'x'

'''

def command():
    pass

n = int(input().strip())
list = []
for num in range(n):
    command = input().strip().split(' ')
    if (command[0] == 'insert'):
        list.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(list)
    elif command[0] == 'remove':
        list.remove(int(command[1]))
    elif command[0] == 'append':
        list.append(int(command[1]))
    elif command[0] == 'sort':
        list.sort()
    elif command[0] == 'pop':
        list.pop()
    elif command[0] == 'reverse':
        list.reverse()



