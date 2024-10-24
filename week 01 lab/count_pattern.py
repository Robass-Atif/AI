def count_pattern(pattern, lst):
    count = 0
    for i in range(len(lst)):
        if pattern == lst[i:len(pattern) + i]:
            count += 1
    return count

print(count_pattern(('a', 'b', 'a'), ('a', 'b', 'a', 'c', 'a', 'c', 'a', 'b')))
