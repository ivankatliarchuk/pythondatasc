class Node:
    def __init__(self, data):
        # initialize data
        self.right = self.left=None
        self.data = data
class Solution:
    def insert(self, root, data):
        # insert data
        if root==None:
            return Node(data)
        else:
            if data <= root.data:
                cur=self.insert(root.left, data)
                root.left=cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    def getHeight(self, root):
        # return the height of the binary search tree
        # go left
        if root == None:
            return -1
        return 1 + (max(self.getHeight(root.left),
                        self.getHeight(root.right)))

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def __hasNodeLeft(self, root):
        if root.left != None:
            return True
        else:
            return False
    # level order traversal



T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)

print("height " + str(height))



'''
https://www.hackerrank.com/challenges/30-binary-trees/tutorial
A level
levelOrder(BinaryTree t) {
    if(t is not empty) {
        // enqueue current root
        queue.enqueue(t)

        // while there are nodes to process
        while( queue is not empty ) {
            // dequeue next node
            BinaryTree tree = queue.dequeue();

            process tree's root;

            // enqueue child elements from next level in order
            if( tree has non-empty left subtree ) {
                queue.enqueue( left subtree of t )
            }
            if( tree has non-empty right subtree ) {
                queue.enqueue( right subtree of t )
            }
        }
    }
}

'''
