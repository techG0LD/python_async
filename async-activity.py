def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))



def multi_list(lst):
    if len(lst) == 0:
        return 0
    
    prod = lst[0]
    if len(lst) > 1:
        for num in lst[1:]:
            prod = prod * num

    return prod


print(multi_list([]))
print(multi_list([5]))

print(multi_list([5,4,6]))


def rev_string(str):
    #   short hand to reverse string
    return str[::-1] 


print(rev_string('Mat'))


def num_within(target,start,end):
    return target in range(start,end + 1)


print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))






triangle = [[1],[1,1]]



def pascal(n):
    if n < 1:
        print('NO')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            prev_row = triangle[row_number - 1]
            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    value = triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]

                    row.append(value)
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)


pascal(2)
pascal(5)