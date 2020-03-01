# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa' #1
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
a=str('0' * nb_of_leading_zeroes) + str(f'{int(code):o}')
list_read=list(reversed(a))
dic_move={0:[0,1],1:[1,1],2:[1,0],3:[1,-1],4:[0,-1],5:[-1,-1],6:[-1,0],7:[-1,1]}

dic_onoff={}
pos_x=0
pos_y=0
list_x=[]
list_y=[]
list_position=[]

for i in list_read:
    if [pos_x,pos_y] not in list_position:
        dic_onoff[(pos_x,pos_y)]=1
    if list_position.count([pos_x,pos_y])%2==0:
        dic_onoff[(pos_x, pos_y)] = 1
    else:
            dic_onoff[(pos_x,pos_y)]=2

    list_position.append([pos_x,pos_y])
    list_xy = dic_move.get(int(i))
    pos_x += list_xy[0]
    pos_y += list_xy[-1]

if [pos_x,pos_y] not in list_position:
    dic_onoff[(pos_x,pos_y)]=1
if list_position.count([pos_x,pos_y])%2==0:
    dic_onoff[(pos_x, pos_y)] = 1
else:
    dic_onoff[(pos_x,pos_y)]=2

for key in list(dic_onoff.keys()):
    if dic_onoff.get(key)==2:
        del dic_onoff[key]

for k in dic_onoff.keys():
    list_x.append(k[0])
    list_y.append(k[1])

try:
    pos_N=max(list_y)
    pos_S=min(list_y)
    pos_W=min(list_x)
    pos_E=max(list_x)
except:
    exit()

for m in reversed(range(pos_S,pos_N+1)):
    for n in range(pos_W,pos_E+1):
        if (n,m) in dic_onoff.keys():
            print(on,end='')
        else:
            print(off,end='')
    print()


