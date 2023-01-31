#!/usr/bin/python3

'''
function definition for pascal triangle
'''
def pascal_triangle(n):
    res = [[1]]
    if (n <= 0) :
        return []
    else :
        for i in range(n - 1) :
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1) :
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res