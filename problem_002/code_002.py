'''
Find the sum of the even values of the Fibonacci sequence
'''

target = 4000000;

val1 = 1;
val2 = 2;
out = 0;

while val2 < target:

    if val2%2 == 0:
        out += val2
        print(val1, val2, out)  

    temp = val2;
    val2 += val1; 
    val1 = temp;

print(out)