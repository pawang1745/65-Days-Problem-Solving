import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def simplify_fraction(num, den):
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def addFraction(num1, den1, num2, den2):
    common_denominator = lcm(den1, den2)
    new_num1 = num1 * (common_denominator // den1)
    new_num2 = num2 * (common_denominator // den2)
    sum_numerators = new_num1 + new_num2
    result_num, result_den = simplify_fraction(sum_numerators, common_denominator)
    print("{}/{}".format(result_num, result_den))

if __name__=='__main__':
    t= int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])

