# # class A():
# #
# #     def __init__(self, x):
# #         self.x = x
# #
# #     def __repr__(self):
# #         return self.x
# #
# #     def __str__(self):
# #         return self.x * 2
# #
# #
# # a = A("one")
# #
# # print(a)
# #
# # repr(A("two"))
# #
# #
# # class B():
# #     def __init__(self):
# #         print("boo!")
# #         self.a = []
# #
# #     def add_a(self, a):
# #         self.a.append(a)
# #
# #     def __repr__(self):
# #         print(len(self.a))
# #         ret = ""
# #         for a in self.a:
# #             ret += str(a)
# #         return ret
# #
# #
# # b = B()
# #
# # b.add_a(A("a"))
# # b.add_a(A("b"))
# # b
# # repr(b)
#
#

# class Link:
#     """A linked list with a first element and the rest."""
#     empty = ()
#
#     def __init__(self, first, rest=empty):
#         assert rest is Link.empty or isinstance (rest, Link)
#         self.first = first
#         self.rest = rest
#
#     def __getitem__(self, i):
#         if i == 0:
#             return self.first
#         else:
#             return self.rest[i - 1]
#
#     def __len__(self):
#         return 1 + len (self.rest)
#
#
# s = Link (3, Link (4, Link (5)))
#
#
# # def is_palindrome(seq):
# #     """ Returns True if the sequence is a palindrome. A palindrome is a sequence
# #     that reads the same forwards as backwards
# #     >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
# #     False
# #     >>> is_palindrome(["l", "i", "n", "k"])
# #     False
# #     >>> is_palindrome("link")
# #     False
# #     >>> is_palindrome(Link.empty)
# #     True
# #     >>> is_palindrome([])
# #     True
# #     >>> is_palindrome("")
# #     True
# #     >>> is_palindrome(Link("a", Link("v", Link("a"))))
# #     True
# #     >>> is_palindrome(["a", "v", "a"])
# #     True
# #     >>> is_palindrome("ava")
# #     True
# #     """
# #     result = []
# #     for i in range (len (seq)):
# #         result.append (seq[i])
# #     if result[::-1] == result:
# #         return True
# #     else:
# #         return False
#
#
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance (rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len (self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr (self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format (repr (self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str (self.first) + ' '
            self = self.rest
        return string + str (self.first) + '>'


#
# s = Link (3, Link (4, Link (5)))
#
# if s is Link.empty:
#     print ('This linked list is empty!')
# else:
#     print ('This linked list is not empty!')
#
# print (str (s))
#
#
# def sum_nums(lnk):
#     """
#     >>> a = Link(1, Link(6, Link(7)))
#     >>> sum_nums(a)
#     14
#     """
#     result = 0
#     for i in range (len (lnk)):
#         result += lnk[i]
#     return result
#
#
# def multiply_lnks(lst_of_lnks):
#     """
#     >>> a = Link(2, Link(3, Link(5)))
#     >>> b = Link(6, Link(4, Link(2)))
#     >>> c = Link(4, Link(1, Link(0, Link(2))))
#     >>> p = multiply_lnks([a, b, c])
#     >>> p.first
#     48
#     >>> p.rest.first
#     12
#     >>> p.rest.rest.rest is Link.empty
#     True
#     """
#     product = 1
#     for lnk in lst_of_lnks:
#         if lnk is Link.empty:
#             return lnk
#         product *= lnk.first
#     lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
#     return Link (product, multiply_lnks (lst_of_lnks_rest))


counts = [1, 2, 3]
items = iter (counts)
while True:
    try:
        i = next (items)
        print (i)
    except StopIteration:
        break  # Exit the while loop


def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1


gen = gen_naturals ()

next (gen)
next (gen)

square = lambda x: x * x


def many_squares(s):
    for x in s:
        yield square (x)
    yield from map (square, s)


a = many_squares ([1, 2, 3])


# def filter_link(link, f):
#     """
#         >>> link = Link(1, Link(2, Link(3)))
#         >>> g = filter_link(link, lambda x: x % 2 == 0)
#         >>> next(g)
#         2
#         >>> next(g)
#         StopIteration
#         >>> list(filter_link(link, lambda x: x % 2 != 0))
#         [1, 3]
#     """
#     while link is not Link.empty:
#         if f (link.first):
#             yield link.first
#         link = link.rest


def filter_no_iter(link, f):
    if link is Link.empty:
        return
    elif f (link.first):
        yield link.first
    yield from filter_no_iter (link.rest, f)


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance (branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format (self.label, repr (self.branches))
        else:
            return 'Tree({0})'.format (repr (self.label))

    def is_leaf(self):
        return not self.branches


def sum_paths_gen(t):
    """
    >>> t1 = Tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if t.is_leaf():
        yield  t.label
    for branch in t.branches:
        for s in sum_paths_gen (branch):
            yield t.label + s


