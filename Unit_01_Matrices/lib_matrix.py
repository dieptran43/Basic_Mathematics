import random
import numpy as np

# Tạo ma trận m dòng và n cột tự nhập tay
def create_matrix(m, n):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            s = "M[" + str(i + 1) + "," + str(j + 1) + "]:"
            x = eval(input(s))
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)

# Tạo vector n phần tử nhập tay
def create_vector(n):
    lst = []
    for i in range(n):
        s = "v[" + str(i + 1) + "]:"
        x = eval(input(s))
        lst.append(x)
    return np.array(lst)

# Tạo ma trận m dòng, n cột, random từ số start,  đến số end

def create_matrix_random(m, n, start, end):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            x = float(random.randint(start, end))
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)

# Tạo vector n, random từ số start, đến số end
def create_vector_random(n, start, end):
    lst = []
    for i in range(n):
        x = float(random.randint(start, end + 1))
        lst.append(x)
    return np.array(lst)

# các phép toán trên vectors
def cal_vectors(op, u, v):
    result = None
    if op == "+":
        result = u + v
    elif op == "-":
        result = u - v
    elif op == "*":
        result = u * v
    elif op == "/":
        result = u / v
    elif op == "dot":
        result = u.dot(v)
    else:
        result = None
    return result


# Các phép toán trên ma trận
def cal_matrices(op, m1, m2):
    result = None
    if op == "+":
        result = m1 + m2
    elif op == "-":
        result = m1 - m2
    elif op == "*":
        result = m1 * m2
    elif op == "/":
        result = m1 / m2
    else:
        result = None
    return result      






