
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output
    
    def inOrder(self):
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            output.append(node.value)
            _walk(node.right)

        _walk(self.root)
        return output

    def Post_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output        


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: # Got to left
                    if current.left == None: # if current is a leaf
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: # if current is a leaf
                        current.right = Node(value)
                        break
                    current = current.right
    
    def contains(self,node,value):
        try:
            if node:
                if node.value == value:
                    return True
                elif node.value > value  :
                    return self.contains(node.left,value)
                elif value > node.value:
                    return self.contains(node.right,value)
            else:
                return False
        except Exception as error:
            return 'error in this function'
        
          
            
           
         
        
        



if __name__ == '__main__':
   def prepare_bst():
    bst = BinarySearchTree()
    bst.add(23)
    # bst.add(8)
    # bst.add(4)
    # bst.add(42)
    # bst.add(27)
    assert bst.root.value == 23
    # assert bst.root.right.value == 42
    # assert bst.root.left.value == 8
    # assert bst.root.left.left.value == 4
    # assert bst.root.right.left.value == 27
    print('succes')
    # print(bst.contains(23))
     
