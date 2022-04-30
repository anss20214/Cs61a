class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, (left, right))


# t = Tree(1, [Tree(2)])
#
# print(t.label)
#
# print(t.branches[0].label)
#
# t.label = t.branches[0].label
#
# print(t)
#
# t.branches.append(Tree(4, [Tree(8)]))
#
# print(t)

# def cumulative_sum(t):
#     """Mutates t so that each node's label becomes the sum of all labels in
#     the corresponding subtree rooted at t.
#
#     >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> cumulative_sum(t)
#     >>> t
#     Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
#     """
#     "*** YOUR CODE HERE ***"
#     for branch in t.branches:
#         if branch == ():
#             return ''


t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])

#
#
# for i in t.branches:
#     print(i)


# def cumulative_sum(t):
#     """Mutates t so that each node's label becomes the sum of all labels in
#     the corresponding subtree rooted at t.
#
#     >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> cumulative_sum(t)
#     >>> t
#     Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
#     """
#     "*** YOUR CODE HERE ***"
#     if t.is_leaf():
#         return t
#     else:
#         for branch in t.branches:
#             cumulative_sum(branch)
#             t.label += branch.label


t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])


def bst_min(t):
    if t.is_leaf():
        return t.label
    else:
        for branch in t.branches:
            bst_min(branch)
            t.label = min(t.label, branch.label)
    return t.label


def bst_max(t):
    if t.is_leaf():
        return t.label
    else:
        for branch in t.branches:
            bst_min(branch)
            t.label = max(t.label, branch.label)
    return t.label


print(bst_max(t1))


#
def is_bst(t):
    if t.is_leaf():
        return True
    if len(t.branches) == 1:
        return is_bst(t.branches[0]) and (t.label >= bst_min(t.branches[0]) or t.label < bst_max(t.branches[0]))
    if len(t.branches) == 2:
        return is_bst(t.branches[0]) and is_bst(t.branches[1]) and bst_max(t.branches[0]) <= t.label < bst_min(
            t.branches[1])
    else:
        return False

t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
print(is_bst(t7))
