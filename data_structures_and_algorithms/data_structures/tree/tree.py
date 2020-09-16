
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        '''
        root>>left>>right

        function to retrieve value of tree

        input--> nothing
        output--> list of value sorted as pre-order
        '''
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
        '''
        left>>root>>right

        function to retrieve value of tree

        input--> nothing
        output--> list of value sorted as in-order
        '''
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
        '''
        left>>right>>root

        function to retrieve value of tree

        input--> nothing
        output--> list of value sorted as post-order
        '''
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output        

    def breadth_first(self):
        breadth_list=[]
        queue_list=[]
        try :
            if not self.root:
                return "Empty tree"
            else :
                if self.root:
                    queue_list.append(self.root)
                while queue_list:
                    current=queue_list.pop(0)
                    breadth_list.append(current.value)

                    if current.left:
                        queue_list.append(current.left)
                    if current.right:
                        queue_list.append(current.right)

                return breadth_list

        except Exception as ex:
            return f'an Error occured {ex}'


                 






    def find_maximum_value(self):
        '''
        this function should return the maximum value in the binary tree
        input--> nothing
        output--> the maximum numeric value
        '''
        result= self.pre_order()
        try:
            maximum_value=result[0]
            
        except Exception as identifier:
            return "Null Tree"
            

        for i in result:
            print(maximum_value,i)
            if maximum_value<i:
                maximum_value=i 
        return maximum_value        


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
   
    # bst = BinarySearchTree()
    # bst.add(23)
    # bst.add(8)
    # bst.add(4)
    # bst.add(42)
    # bst.add(27)

    # assert bst.root.value == 23
    # assert bst.root.right.value == 42
    # assert bst.root.left.value == 8
    # assert bst.root.left.left.value == 4
    # assert bst.root.right.left.value == 27
    
    # print(bst.contains(23))
    

    print('succes')