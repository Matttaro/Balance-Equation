"""""
PROGRAM OVERVIEW
This program will balance a chemical equation
Go through the multiple combinations
xlist = alist + blist
ylist = clist + dlist
See if the number of each element matches between the left and right side
Each index represents the number of an element in a compound
N-H-O
"""""


# multiplier function - multiply corresponding list, combine call, analyze call, set number back
def multiplier(a_list, b_list, c_list, d_list, m, n):
    for w in range(m, n):
        for x in range(3):
            a_list[x] = a_list[x] * w
        xlist = combine(a_list, b_list)
        ylist = combine(c_list, d_list)
        if analyze(xlist, ylist):
            print("BALANCE FOUND")
            print(a_list)
            print(b_list)
            print(c_list)
            print(d_list)
            return
        for x in range(3):
            a_list[x] = a_list[x] / w

        for u in range(m, n):
            for x in range(3):
                b_list[x] = b_list[x] * u
            xlist = combine(a_list, b_list)
            ylist = combine(c_list, d_list)
            if analyze(xlist, ylist):
                print("BALANCE FOUND")
                print(a_list)
                print(b_list)
                print(c_list)
                print(d_list)
                return
            for x in range(3):
                b_list[x] = b_list[x] / u

            for y in range(m, n):
                for x in range(3):
                    c_list[x] = c_list[x] * y
                xlist = combine(a_list, b_list)
                ylist = combine(c_list, d_list)
                if analyze(xlist, ylist):
                    print("BALANCE FOUND")
                    print(a_list)
                    print(b_list)
                    print(c_list)
                    print(d_list)
                    return
                for x in range(3):
                    c_list[x] = c_list[x] / y

                for z in range(m, n):
                    for x in range(3):
                        d_list[x] = d_list[x] * z
                    xlist = combine(a_list, b_list)
                    ylist = combine(c_list, d_list)
                    if analyze(xlist, ylist):
                        print("BALANCE FOUND")
                        print(a_list)
                        print(b_list)
                        print(c_list)
                        print(d_list)
                        return
                    for x in range(3):
                        d_list[x] = d_list[x] / z


# combine function
def combine(first_list, second_list):
    sum_list = [first_list[0] + second_list[0], first_list[1] + second_list[1], first_list[2] + second_list[2]]
    return sum_list


# analyze function
def analyze(left_list, right_list):
    if left_list[0] == right_list[0]:
        if left_list[1] == right_list[1]:
            if left_list[2] == right_list[2]:
                return True
    return False


alist = [1, 3, 0]  # NH3
blist = [1, 0, 2]  # NO2
clist = [2, 0, 1]  # N2O
dlist = [0, 2, 1]  # H20

m = int(input("Input lower range: "))
n = int(input("Input higher range: "))

multiplier(alist, blist, clist, dlist, m, n)
