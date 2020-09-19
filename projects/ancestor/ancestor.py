
def earliest_ancestor(ancestors, starting_node):
    # ancestors is a list of pairs: [(parent, child),..., (parent, child)]
    family_tree = {}

    ## Create the family tree:
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        if child not in family_tree:
            # keys are children, since we're moving up the tree
            family_tree[child] = [parent]
        else:
            # adding an additional parent to list
            family_tree[child].append(parent)

    # print('tree: ', family_tree)
    ## Find the earliest ancestor:
    if starting_node not in family_tree:
        return -1

    path = set()
    children = set([starting_node])
        # set() only accepts iterable objects (lists, tuples, dicts, etc)
    searching = True
    while searching:
        for child in children:
            if child in family_tree:
                # child = starting_node OR current family member/vertex):
                for parent in family_tree[child]:
                    # print('inner: ', child, parent, path)
                    path.add(parent)

        if not path:
            break
        children = path
        path = set()

    # children should be earliest ancestor (or ancestor pair)
    # return the smallest value if children is more than 1
    return min(children)