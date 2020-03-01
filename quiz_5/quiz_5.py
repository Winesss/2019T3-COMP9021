# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):
    pass
    read=[]
    n=''
    for e in list_of_integers:
        read.append(bin(e)[2:])
    for i in range(len(read)):
        if i !=0:
            n+='0'
        mid=read[i]
        for k in mid:
            n=n+k+k
    result=int(n,2)
    return result


def decode(integer):
    pass
    read=list(bin(integer)[2:])
    n=''
    i=0
    result=[]
    if len(read)==1:
        return None
    o=len(read)
    while i <=len(read)-1:
        if len(read)-i>=2:
            if read[i]==read[i+1]:
                n+=read[i]
                i+=2
            elif read[i]=='1':
                return None
            else:
              n+='_'
              i+=1
        if i == len(read)-1:
            return None
    code=n.split('_')
    for i in range(len(code)):
        result.append(int(code[i],2))
    return result


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
