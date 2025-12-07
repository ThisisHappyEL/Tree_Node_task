from Tree_node import Tree_node

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Tree_node(key, value)
        else:
            self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, current_node, key, value):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Tree_node(key, value)
            else:
                self._insert_recursive(current_node.left, key, value)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Tree_node(key, value)
            else:
                self._insert_recursive(current_node.right, key, value)
        else:
            current_node.value = value
    
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return None
        
        if key == current_node.key:
            return current_node.value

        if key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def height(self):
        return self._height_recursive(self.root)
        
    def _height_recursive(self, current_node):
        if current_node is None:
            return 0

        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)

        return 1 + max(left_height, right_height)
    
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        if node is None:
            return True

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        if abs(left_height - right_height) <= 1:
            if self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
                return True
        return False
        
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current_node, key):
        if current_node is None:
            return current_node

        if key < current_node.key:
            current_node.left = self._delete_recursive(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete_recursive(current_node.right, key)
        
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            
            temp = self._min_value_node(current_node.right)
            
            current_node.key = temp.key
            current_node.value = temp.value
            
            current_node.right = self._delete_recursive(current_node.right, temp.key)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
