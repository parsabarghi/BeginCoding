class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            # add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        element = []

        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

        return element

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):

        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):

        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            """or we can use left max
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)"""

        return self

def build_tree(element):
    root = BinarySearchTree(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])

    return root

if __name__ == '__main__':
    nums = [23, 4, 65, 2, 1, 7, 89, 99, 23]
    number_tree = build_tree(nums)
    print(f"THE NUMBERS IN OUR LIST 'IN ORDER TRAVERSAL' :\n{number_tree.in_order_traversal()}")
    print("_______________________________________________")
    print(f"DID WE HAD NUMBER 10 IN OUR LIST? {number_tree.search(10)}")
    print(f"WHAT IS MAX NUMBER IN LIST? {number_tree.find_max()}")
    print(f"WHAT IS MAN NUMBER IN LIST? {number_tree.find_min()}")
    number_tree.delete(65)
    print(f"LIST AFTER DELETE ITEM:\n{number_tree.in_order_traversal()}")
