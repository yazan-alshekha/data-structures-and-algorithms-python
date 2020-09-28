from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.data_structures.tree.tree import Node,BinaryTree

def test_tree_intersection():
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)

    b = BinaryTree()
    b.root = Node(7)
    b.root.left = Node(13)
    b.root.right = Node(100)
    b.root.left.left = Node(150)
    b.root.left.right = Node(9)
    b.root.right.left = Node(1)
    b.root.right.right = Node(-4)

    actual = tree_intersection(bt,b)
    expected=[7, 13, 9, 1, -4]
    assert actual==expected


def test_2_tree_intersection():
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)

    b = BinaryTree()
    b.root = Node(10)
    b.root.left = Node(20)
    b.root.right = Node(100)
    b.root.left.left = Node(150)
    b.root.left.right = Node(80)
    b.root.right.left = Node(70)
    b.root.right.right = Node(90)

    actual = tree_intersection(bt,b)
    expected=[]
    assert actual==expected




def test_empty_tree_intersection():
    bt = BinaryTree()
    b = BinaryTree()
    actual = tree_intersection(bt,b)
    expected='Empty trees'
    assert actual==expected