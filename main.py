from Binary_search_tree import Binary_search_tree

bst = Binary_search_tree()
bst.insert(50, "Root")
bst.insert(30, "Left")
bst.insert(70, "Right")
bst.insert(20, "Left-Left")

print(bst.search(70)) # Должен вывести "Right"
print(bst.search(999)) # Должен вывести None
print(bst.height())  # Должен вывести "3"