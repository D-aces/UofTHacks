from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
from typing import Iterable
import math


@dataclass
class _Node:
    """A node of an individual in a family tree.

    Instance Attributes:
        - item: The data stored in this node.
        - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None

class TreeNode:
    """A recurisve Tree of a family tree data structure.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
    """
    # Private Instance Attributes:
    #   - _root:
    #       The item stored at this tree's root, or None if the tree is empty.
    #   - _subtrees:
    #       The list of subtrees of this tree. This attribute is empty when
    #       self._root is None (representing an empty tree). However, this attribute
    #       may be empty when self._root is not None, which represents a tree consisting
    #       of just one item.
    _root: Optional[Any]
    _subtrees: list[TreeNode]

    def __init__(self, data):
        """Initialize a new Tree with the given data.

        If data is None, the tree is empty.

        Preconditions:
            - data is not none
        """
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def build_family_tree(self):
        root = TreeNode("Child")

        parents = TreeNode("Parents")
        
        grandparents = TreeNode("Grandparents")
        
        siblings = TreeNode("Siblings")
        
        relatives = TreeNode("relatives")

        root.add_child(parents)
        root.add_child(grandparents)
        root.add_child(siblings)
        root.add_child(relatives)
        
        return root


def build_family_tree():
    pass


if __name__ == '__main__':
    root = build_family_tree()
    pass
