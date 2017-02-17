class Solution:
    def __init__(self):
        ''' Initialize object instance'''
        self.__queue = []
        self.__stack = []
        pass

    def pushCharacter(self, char):
        '''Pushes a character into a stack'''
        self.__stack.append(char)

    def enqueuCharacter(self, char):
        '''Enqueues a character in the queue instance variable'''
        self.__queue.append(char)

    def popCharacter(self):
        '''Pops and returns the character at the top of the stack'''
        return self.__stack.pop()

    def dequeueCharacter(self):
        '''Dequeues and returns the first character in the queue'''
        return self.__queue.pop(0)


#read the string
s = input()
# create object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueuCharacter(s[i])

isPalindrome = True

'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    first = obj.popCharacter()
    second = obj.dequeueCharacter()
    print(str(first) + ":" + str(second))
    if first != second:
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The world, " + s + ", is a palindrome.")
else:
    print("The world, " + s + ", is not a palindrome.")
