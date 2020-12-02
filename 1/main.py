INPUT = [ 1946, 1859, 1654, 1806, 1648, 1873,
         1216, 1831, 1610, 1779, 1626, 1332, 
         1713, 1919, 1353, 1720, 1818, 1976, 
         1993, 1617, 1678, 1655, 1725, 1686, 
         1737, 1696, 1046, 1814, 1909, 1618, 
         2006, 1903, 1528, 1635, 1457, 1924, 
         1734, 1723, 1735, 1984, 1846, 1921, 
         1587, 2009, 1607, 1987, 1910, 1571, 
         1898, 1869, 1537, 1446, 1535, 1802, 
         1847, 1966, 1944, 1793, 1383, 1850, 
         1274, 347, 1208, 1748, 1906, 1771, 
         1849, 1773, 1792, 1705, 1538, 1564, 
         2003, 1994, 1545, 1704, 1657, 1483, 
         1701, 1724, 1293, 1834, 1712, 1950, 
         1844, 1290, 1692, 1820, 1585, 1986, 
         1328, 1841, 1709, 1232, 1945, 1684, 
         1787, 1991, 1914, 1977, 1620, 
         1825, 1866, 1615, 1832, 496, 1932, 
         1819, 1559, 1870, 1677, 1650, 1594, 
         1664, 1600, 1622, 1862, 1937, 1624, 
         1580, 1931, 1803, 1839, 1755, 1952, 
         1473, 1694, 1864, 1178, 1163, 1790, 
         393, 1776, 1871, 1999, 1923, 1174, 
         1557, 1646, 1200, 1842, 1432, 1573, 
         1913, 1954, 1599, 1980, 1948, 1430, 
         1298, 1835, 1643, 1742, 1609, 1649, 
         1382, 1343, 1263, 1908, 1703, 1922, 
         1764, 1603, 1330, 588, 954, 1772, 
         1553, 975, 1499, 1552, 1214, 1829, 
         1698, 1797, 1807, 1961, 1947, 1845, 
         1881, 1821, 1815, 1623, 1675, 1478, 
         1886, 1951, 1700, 1890, 1876, 1781, 
         1853, 1983, 1901, 1939, 1292, 853, 
         1879, 1652, 16
    ] 

def sum_indexes(arr, indexes):
    result = 0
    for i in indexes:
        result += arr[i]
    return result

def find_summed_numbers(arr, n_numbers, sum):
    result = []
    indexes = [i for i in range(0, n_numbers - 1)]
    max_indexes = [i for i in range(0, n_numbers - 1)]
    moved_index_sum = 0
    last_moved_index = -1
    while len(result) == 0:
        if sum_indexes(arr, indexes + [-1]) > sum:
            arr = arr[0:-1]
            indexes = [i for i in range(0, n_numbers - 1)]
            max_indexes = [i for i in range(0, n_numbers - 1)]
            moved_index_sum = 0
            last_moved_index = -1


        elif sum_indexes(arr, indexes + [-1]) == sum:
            result = [arr[i] for i in indexes + [-1]]
        else:
            ldi = -1 # Lowest diff index
            lowest_diff = 0
            for i in indexes:
                if not i + 1 in indexes: # Check if the current index can move
                    if i + 1 >= len(arr): # Could'n find any match
                        return []
                    if indexes.index(i) == last_moved_index: # Check if we are moving an already moves index
                        diff = arr[i + 1] - arr[i] + moved_index_sum
                    else:
                        diff = arr[i + 1] - arr[i]
                    if diff < lowest_diff or lowest_diff == 0:
                        lowest_diff = diff
                        ldi = i
            index_of_ldi = indexes.index(ldi)
            if index_of_ldi != last_moved_index: # Not moving the same as before, reset sum
                moved_index_sum = lowest_diff
            else:                               # Else - Increase the running sum
                moved_index_sum += lowest_diff

            last_moved_index = index_of_ldi
            indexes[index_of_ldi] += 1 # Move the index with the lowest difference
            
            if max_indexes[index_of_ldi] < indexes[index_of_ldi]:
                if index_of_ldi > 0:
                    indexes[0:index_of_ldi] = [i for i in range(0, index_of_ldi)]

                if index_of_ldi < len(indexes) - 1:
                    indexes[index_of_ldi+1:len(indexes)] = [i for i in range(ldi+2, len(indexes[index_of_ldi+1:len(indexes)]) + ldi + 2)]

                max_indexes[index_of_ldi] += 1

    return result

def find_summed_numbers3(arr, sum):
    result = []
    fi = 0
    mi = 1
    while len(result) == 0:
        if arr[fi] + arr[mi] + arr[-1] > sum:
            arr = arr[0:-1]
            fi = 0
            mi = 1
        elif arr[fi] + arr[mi] + arr[-1] < sum:
            if mi - 1 == fi:
                mi += 1
                fi = 0
            else:
                fi += 1
        else:
            result = [arr[fi], arr[mi], arr[-1]]
    return result

if __name__ == "__main__":
    pass
    # input = sorted(INPUT)
    # part_1 = find_summed_numbers(input, 2, 2020)
    # print(part_1, sum(part_1))

    # part_2 = find_summed_numbers(input, 3, 2020)
    # print(part_2, sum(part_2))

    # part_3 = find_summed_numbers(input, 4, 2020)
    # print(part_3, sum(part_3))

#                           #
#       Version 1:          #
#                           #
# def part_1(input, s):
#     for i in input:
#         for j in input:
#             if i == j:
#                 break
#             elif j + i == s:
#                 return (i, j, i*j)

# def part_2(input, s):
#     for i in input:
#         for j in input:
#             for k in input:
#                 if i == j == k:
#                     break
#                 elif j + i + k == s:
#                     return (i, j, k, i*j*k)


# if __name__ == "__main__":
#     print(part_1(INPUT, 2020))
#     print(part_2(INPUT, 2020))
                



#                           #
#       Version 2:          #
#                           #

# def find_summed_numbers(arr, sum):
#     result = []

#     while len(result) == 0:
#         if arr[0] + arr[-1] > sum:
#             arr = arr[0:-1]
#         elif arr[0] + arr[-1] < sum:
#             arr = arr[1:len(arr)]
#         else:
#             result = [arr[0], arr[-1]]
#     return result


# def find_summed_numbers3(arr, sum):
#     result = []
#     fi = 0
#     mi = 1
#     while len(result) == 0:
#         if arr[fi] + arr[mi] + arr[-1] > sum:
#             arr = arr[0:-1]
#             fi = 0
#             mi = 1
#         elif arr[fi] + arr[mi] + arr[-1] < sum:
#             if mi - 1 == fi:
#                 mi += 1
#                 fi = 0
#             else:
#                 fi += 1
#         else:
#             result = [arr[fi], arr[mi], arr[-1]]
#     return result

# def multiply_array(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     return sum


# if __name__ == "__main__":
#     input = sorted(INPUT)
#     part_1 = find_summed_numbers(input, 2, 2020)
#     print(part_1, multiply_array(part_1))

#     part_2 = find_summed_numbers(input, 3, 2020)
#     print(part_2, multiply_array(part_2))




