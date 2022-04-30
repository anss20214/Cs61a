from linkedlist import Link, map_link, filter_link, extend_link


def empty(s):
    return s is Link.empty


def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2."""
    return filter_link(lambda v: set_contains(set2, v), set1)


def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = filter_link(lambda v: not set_contains(set2, v), set1)
    return extend_link(set1_not_set2, set2)


def square(x):
    return x ** 2


s = Link(4, Link(1, Link(5)))

t = adjoin_set(s, 2)

intersect_set(s, map_link(square, t))

union_set(t, s)


def intersect_set(set1, set2):
    "ordered sequence saving time to compute"
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set(set1.rest, set2)
        elif e1 > e2:
            return intersect_set(set1, set2.rest)


print(intersect_set(s, s.rest))
