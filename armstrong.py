

# 153 is narcisistic because 1^3 + 5^3 +3^3 = 153


def count_digit(n):
    count = 0
    while n:
        n //= 10
        count += 1
    return count

def is_armstrong(n):
    
    if n < 0:
        return False
    
    suma = 0
    digits = count_digit(n)
    
    while n:
        r = n%10
        suma += r**digits
        n //= 10
        
    return suma == n


def narcissistic_function(x, b):
    num_digits = 0
    while x > 0:
        num_digits += 1
        x = x // b
    total = 0
    while x > 0:
        total += pow(x % b, num_digits)
        x = x // b
    return total


















