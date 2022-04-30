def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)

def print_partitions(n, m):
    lists = count_partitions(n, m)
    strings = map(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))

count_partitions(6,4)