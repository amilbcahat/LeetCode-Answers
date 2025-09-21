# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flattenTree(self, node): 

        # Handle the null scenario
        if not node:
            return None

        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node

        # Recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)

        # Recursively flatten the right subtree
        rightTail = self.flattenTree(node.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side
        # anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return rightTail if rightTail else leftTail



    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #Approach 1 
        # self.flattenTree(root)

        #Approach 2 
         # Handle the null scenario
        if not root:
            return None

        START, END = 1, 2

        tailNode = None
        stack = collections.deque([(root, START)])

        while stack:

            currentNode, recursionState = stack.pop()

            # We reached a leaf node. Record this as a tail
            # node and move on.
            if not currentNode.left and not currentNode.right:
                tailNode = currentNode
                continue

            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursionState == START:

                # If the current node has a left child, we add it
                # to the stack AFTER adding the current node again
                # to the stack with the END recursion state.
                if currentNode.left:
                    stack.append((currentNode, END))
                    stack.append((currentNode.left, START))
                elif currentNode.right:

                    # In case the current node didn't have a left child
                    # we will add it's right child
                    stack.append((currentNode.right, START))
            else:
                # If the current node is in the END recursion state,
                # that means we did process one of it's children. Left
                # if it existed, else right.
                rightNode = currentNode.right

                # If there was a left child, there must have been a leaf
                # node and so, we would have set the tailNode
                if tailNode:

                    # Establish the proper connections.
                    tailNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                    rightNode = tailNode.right

                if rightNode:
                    stack.append((rightNode, START))




        #Approach 3 
        # # Handle the null scenario
        # if not root:
        #     return None

        # node = root
        # while node:

        #     # If the node has a left child
        #     if node.left:

        #         # Find the rightmost node
        #         rightmost = node.left
        #         while rightmost.right:
        #             rightmost = rightmost.right

        #         # rewire the connections
        #         rightmost.right = node.right
        #         node.right = node.left
        #         node.left = None

        #     # move on to the right side of the tree
        #     node = node.right