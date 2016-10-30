from abc import ABCMeta, abstractmethod
from typing import Sequence, TypeVar, Generic

T = TypeVar('T') # declare type variable
# todo create comparable interface T extends comparable

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
    def __init__(self, element: T):
        self.data  = element
        self.left  = EmptyBST()
        self.right = EmptyBST()

    def cardinality(self):
        '''
        This data plus everyting in the left, plus everything at the right tree.
        :return:
        '''
        return (1 + self.left.cardinality() + self.right.cardinality())

    def isEmpty(self):
        return False

    def add(self, element: T):
        super().add(element)

    def member(self, element: T) -> T:
        return super().member(element)


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

