# generate fibonacci number sequence

print('please type how many numbers of the fibonacci sequence you would like to see.'
      '(you get 13 entries, little doggy)')
def fib(x):

    a, b = 0, 1

    if x == 1:
        print(a)

    elif x <= 0:
        print('invalid entry, please type positive integer')

    else:
        print(a)

        for i in range(x):
          a, b = b, a + b
          print(a)

for chr in str('oh hai doggy.'):
    fib(int(input()))

    
