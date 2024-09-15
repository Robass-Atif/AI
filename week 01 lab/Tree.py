

def tree_ref(tree,index):
    if not index:
        return tree
    
    return tree_ref(tree[index[0]],index[1:])


print(tree_ref((((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10)),[3,3]))