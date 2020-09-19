from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree,Node


def fizz_buzz(value):
    """
     Function to do fizz_buzz on the given value
     
    """
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


def fizz_buzz_tree(tree):
    try:
        new_tree=BinaryTree()
        if not tree.root:
            return new_tree
        

        def helper(current):
            new_Node=Node(fizz_buzz(current.value))
            if current.left:
                new_Node.left=helper(current.left)
            if current.right:
                new_Node.right=helper(current.right)
            return new_Node    


        new_tree.root=helper(tree.root)
        return new_tree
    except:
        return "your input not tree"


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(9)

    test_tree=fizz_buzz_tree(tree)
    print(test_tree.root.value)
    print(test_tree.root.left.value)
    print(test_tree.root.right.value)


