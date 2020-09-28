from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree,Node


def tree_intersection(bt1,bt2):

    '''
    function takes 2 binary tree and retrieve the nodes which  is same (value and location in their tree) 

    input -->two binary tree
    output--> list []
    '''
    
    try:
        list_bt1=bt1.breadth_first()
        list_bt2=bt2.breadth_first()
        
        if list_bt1 and list_bt2=="Empty tree":
            return 'Empty trees'
        result=[]
        i=0
        while i<len(list_bt1):
            if list_bt1[i]==list_bt2[i]:
                result.append(list_bt1[i])
            i+=1    
        return result
    except Exception as e:
        return e            







if __name__ == "__main__":
    bt = BinaryTree()
    # bt.root = Node(7)
    # bt.root.left = Node(13)
    # bt.root.right = Node(5)
    # bt.root.left.left = Node(8)
    # bt.root.left.right = Node(9)
    # bt.root.right.left = Node(1)
    # bt.root.right.right = Node(-4)

    b = BinaryTree()
    # b.root = Node(7)
    # b.root.left = Node(13)
    # b.root.right = Node(100)
    # b.root.left.left = Node(150)
    # b.root.left.right = Node(9)
    # b.root.right.left = Node(1)
    # b.root.right.right = Node(-4)

    print(tree_intersection(bt,b))


    # print(bt.breadth_first())