

def mult_of_three(num):
    return num%3 == 0


def mult_of_five(num):
    return num%5 == 0


def sum_mults(num):

    out = 0;

    for val in range(3,num):

        if mult_of_three(val):
            out += val
        elif mult_of_five(val):
            out += val
        else:
            pass

    return out


if __name__ == "__main__":
    print(f'Sum of multiples for 10 is {sum_mults(10)}')
    print(f'Sum of multiples for 10 is {sum_mults(100)}')
    print(f'Sum of multiples for 10 is {sum_mults(1000)}')