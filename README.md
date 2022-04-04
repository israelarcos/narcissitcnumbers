# Narcissistic Numbers
An n-digit number that is the sunof the nth powersof its digits is called an n-narcissistic number. It is also sometimes known as an Armstrong number, perfect digital invariant (Madachy 1979), or plus perfect number. Hardy (1993) wrote, The smallest example of a narcissistic number other than the trivial 1-digit numbers is
153 = 1^3 + 5^3 + 3^3
(1)

The first few are given by 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, ...

#Original Code
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


#Errors
We are using the same number that we use as a parameter in comparisons and conversions. We do not store the original value, and that is why it is lost. It does not give any valid value, since it decreases the number with each iteration. The solution is to create an auxiliary variable that stores the original number.


#Corrected code
#tell if the number n is armstrong
def is_armstrong(n):
    
    if n < 0:
        return False
    
    aux_num = n
    suma = 0
    digits = count_digit(n)
    
    while n:
        r = n%10
        suma += r**digits
        n //= 10
        
    return suma == aux_num

#compute the sum of the digits of number n to thw power b
def narcissistic_function(x, b):
    y = x
    num_digits = 0
    while y > 0:
        num_digits += 1
        y = y // b
    total = 0
    while x > 0:
        total += pow(x % b, num_digits)
        x = x // b
    return total
