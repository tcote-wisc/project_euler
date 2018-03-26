"""
Project Euler Problem 004:
    Find the largest palindrome made from the product of two 3-digit 
    numbers.

    Ex. The largest palindrome made from the product of two 2-digit 
        numbers is 9009 = 91 × 99.
 
"""



def is_palindrome(num):
    """ Check if an integer is a palindrome """
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    
    digits = 3

    min_val = (10**(digits-1))
    max_val = ((10**digits)-1)

    largest = 0
    for i in range(max_val,min_val,-1):
        for j in range(max_val,min_val,-1):
            val = i*j
            if is_palindrome(val) and val > largest:
                largest = val
                factors = [i,j]

    print(f'{factors[0]} * {factors[1]} = {largest}')    



