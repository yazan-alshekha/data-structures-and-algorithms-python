# from trees import __version__
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, Node, BinarySearchTree
import pytest


def test_empty_binary_tree():
    bt = BinaryTree()
    assert bt.root == None

def test_pre_order_traverse(prepare_bt):
    actual = prepare_bt.pre_order()
    expected = [7, 13, 8, 9, 5, 1, -4]
    assert actual == expected

def test_in_order_traverse(prepare_bt):
    actual = prepare_bt.inOrder()
    expected = [8,13,9,7,1,5,-4]
    assert actual == expected

def test_in_order_traverse(prepare_bt):
    actual = prepare_bt.Post_order()
    expected = [8,9,13,1,-4,5,7]
    assert actual == expected

def test_bst_add_on_root():
    bst = BinarySearchTree()
    bst.add(4)
    expected = 4
    actual = bst.root.value
    assert actual == expected

def test_bst_add_4_values(prepare_bst):
    bst = prepare_bst
    assert bst.root.value == 23
    assert bst.root.right.value == 42
    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 4
    assert bst.root.right.left.value == 27

def test_bst_add_3_values():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(8)
    bst.add(42)

    assert bst.root.value == 23
    assert bst.root.left.value == 8
    assert bst.root.right.value == 42

@pytest.fixture
def prepare_bt():
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    return bt

@pytest.fixture
def prepare_bst():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(8)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    return bst

def test_contains2(prepare_bst):
    bst = prepare_bst
    expected=False
    actual=bst.contains(bst.root,100)
    assert expected==actual

def test_contains(prepare_bst):
    bst = prepare_bst
    expected=True
    actual=bst.contains(bst.root,8)
    assert expected==actual

  
def test_maximum_value(prepare_bt):
    actual = prepare_bt.find_maximum_value()
    expected = 13
    assert actual == expected

def test_maximum_value_empty_tree():
    bt = BinaryTree()
    actual = bt.find_maximum_value()
    expected = "Null Tree"
    assert actual == expected
