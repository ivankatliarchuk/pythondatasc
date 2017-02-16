from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T') # declare type variable
# todo create comparable interface T extends comparable

class ElementComparator(Generic[T]):
    '''
    Can we generify this?
    '''
    pass


class Tree(Generic[T], metaclass = ABCMeta):

    '''
    check if the tree is empty
    Return 'true' when empty and 'false' otherwise
    '''
    @abstractmethod
    def isEmpty(self): pass

    '''
    Calculate cardinality.
    Returns '0' if its an empty tree, and 'x' when is non-empty tree
    '''
    @abstractmethod
    def cardinality(self): pass

    # generic function
    @abstractmethod
    def member(self, element: T) -> T: pass
    @abstractmethod
    def add(self, element: T): pass

    # def member(self, element: T) -> T: pass

class NonEmptyBST(Tree, Generic[T]):
    def __init__(self, element):
        self.data  = element
        self.left  = EmptyBST()
        self.right = EmptyBST()

    def __init__(self, data, leftElement:T, rightElement: T):
        self.data = data
        self.left = leftElement
        self.right = rightElement

    def cardinality(self):
        '''
        This data plus everyting in the left, plus everything at the right tree.
        :return:
        '''
        return (1 + self.left.cardinality() + self.right.cardinality())

    def isEmpty(self):
        return False

    def add(self, element: T):
        if self.data == element:
             return self
        else:
            if element < self.data:
               return NonEmptyBST(self.data, self.left.add(element), self.right)
            else:
                return NonEmptyBST(self.data, self.left, self.right.add(element))
        pass

    def member(self, element: T) -> T:
        if self.data == element:
            return True
        else:
            if element < self.data:
                # check left member
                return self.left.member(element)
            else:
                return self.right.member(element)


class EmptyBST(Tree, Generic[T]):
    def __init__(self):
        super()

    def cardinality(self):
        return 0

    def isEmpty(self):
        return Tree

    def add(self, element: T):
        '''
        create new non-empty binary search tree with the element.
        :param element: single element.
        :return: non-empty binary search tree.
        '''
        return NonEmptyBST(element)

    def member(self, element: T) -> T:
        return False



class BinarySearchTree:
    pass



'''
tree interface
1. noneemptybst
a class representing non-empty binary search trees
2. emptybst
a class representing empty binary search tree
'''

