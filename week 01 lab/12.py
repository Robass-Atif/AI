def depth(tree):
    
    if not isinstance(tree, tuple):
        return 0
    return 1 + max(depth(branch) for branch in tree)

 
print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))
