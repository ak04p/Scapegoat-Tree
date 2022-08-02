import math
class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None

class Scapegoat_tree:
    def __init__(self, a):
        self.size = 0
        self.root = None
        self.alpha = a
        self.max_size = 0
        
    def isEmpty(self):
        return self.root == None

    def search(self, root, val):
        found = False
        if root is not None:
            if val < root.value:
                self.search(root.left, val)
            elif val > root.value:
                self.search(root.right, val)
            elif val == root.value:
                found = True
        return found

    def ret_size(self):
        return self.size

    def printCurrentLevel(self, root, level, children):
        if root is None:
            return
        if level == 1:
            children.append(root.value)
        elif level > 1:
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)

    def height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            if left_height > right_height:
                return left_height+1
            else:
                return right_height+1
    
    def size_of_node(self, node):
        if not node:
            return
        else:
            return self.size_of_node(node.left) + self.size_of_node(node.right) + 1

    def levelorder(self, root):
        h = self.height(root)
        children = []
        for i in range(1, h+1):
            self.printCurrentLevel(root, i, children)
        return children

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
    
    def log32(self, n):
        log23 = 2.4663034623764317
        return int(math.ceil(log23*math.log(n)))

    def minimum(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp

    def insert(self, val, current_node):
        if self.root is None:
            self.root = Node(val)
        elif current_node.value > val:
            if current_node.left is None:
                current_node.left = Node(val)
                current_node.left.parent = current_node
            else:
                self.insert(val, current_node.left)
        elif current_node.value < val:
            if current_node.right is None:
                current_node.right = Node(val)
                current_node.right.parent = current_node
            else:
                self.insert(val, current_node.right)
        return current_node

    def insert_util(self, val):
        new_node = self.insert(val, self.root)
        self.size += 1
        self.max_size = max(self.size, self.max_size)
        depth_of_node = self.find_depth(new_node)
        if depth_of_node > self.log32(self.max_size):
            scapegoat_node = new_node.parent
            while 3*self.size_of_node(scapegoat_node) <= 2*self.size_of_node(scapegoat_node.parent):
                scapegoat_node = scapegoat_node.parent
            self.rebuild_tree(scapegoat_node.parent)

    def find_depth(self, root):
        if root == None:
            return 0
        else:
            left = self.find_depth(root.left)
            right = self.find_depth(root.right)
        return max(left, right)+1

    def flatten(self, node, flat_tree):
        if node:
            if node.left is not None:
                self.flatten(node.left, flat_tree)
            flat_tree.append(node.value)
            if node.left is not None:
                self.flatten(node.right, flat_tree)

    def rebuild_tree(self, s_node):
        parent_node = s_node.parent
        flat_tree = list()
        self.flatten(s_node, flat_tree)
        if parent_node is None:
           self.root = self.build_tree_from_list(flat_tree, 0, self.size_of_node(s_node))
           self.parent = None
        elif parent_node.right == s_node:
            parent_node.right = self.build_tree_from_list(flat_tree, 0, self.size_of_node(s_node))
            parent_node.right.parent = parent_node
        elif parent_node.left == s_node:
            parent_node.left = self.build_tree_from_list(flat_tree, 0, self.size_of_node(s_node))
            parent_node.left.parent = parent_node

    def build_tree_from_list(self, tree_list, start, end):
        if start > end:
            return None
        mid = int(math.ceil(start + (end - start) / 2.0))
        node = Node(tree_list[mid].value)
        node.left = self.build_tree_from_list(tree_list, start, mid-1)
        node.right = self.build_tree_from_list(tree_list, mid+1, end)
        return node       







