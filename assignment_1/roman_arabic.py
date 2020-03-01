import sys

def checkInput():
    print('Hey, ask me something that\'s not impossible to do!')
    sys.exit()

def delespace(string):
    for i in string:
        if i ==' ':
            string=string.replace('',' ')
    return string

def checkRomannumber(string):
    Roman=('I','V','X','L','C','D','M')
    for i in string:
        if i not in Roman:
            return False
    return True

def checkposinteger(string):
    if string.isdigit():
        if int(string)>0:
            return True
    else:
        return False

def int_convert_romannum(input_num,int_roma):  #integer convert to roman number
    romannumber=''
    list_1=list(int_roma.keys())
    list_2=list(reversed(list_1))
    for key in list_2:
        while input_num >= key:
            input_num=input_num-key
            romannumber=romannumber+int_roma.get(key)
    return romannumber

def romannum_convert_int(input_letter,roma_int):   #roman number convert to integer
    if input_letter=='0':
        return 0
    else:
        integernum=0
        for i in range(len(input_letter)):
            if i >0 and roma_int[input_letter[i]]>roma_int[input_letter[i-1]]:
                integernum=integernum-roma_int[input_letter[i-1]]
                integernum=integernum+roma_int[input_letter[i]]-roma_int[input_letter[i-1]]
            else:
                integernum=integernum+roma_int[input_letter[i]]
        return integernum

def check_distinct(string):  #distinct
    for i in string:
        if string.count(i)>1:
            return False
    return True

def int_con_genroman(genroman):  #got int_roma
    dict_genroman={}
    list_2=list(reversed(genroman))
    n=1
    i=0
    while i<len(genroman):
        if i==0:
            dict_genroman[n]=list_2[i]
            n=5
        elif i==1:
            dict_genroman[n-1]=list_2[0]+list_2[i]
            dict_genroman[n]=list_2[i]
        elif i%2==0:
            if n==5:
                dict_genroman[n*2-1]=list_2[i-2]+list_2[i]
            else:
                dict_genroman[n*2-int(n/5)]=list_2[i-2]+list_2[i]
            dict_genroman[n*2]=list_2[i]
            n=n*2
        elif i%2==1 and i>1:
            dict_genroman[n*5-n]= list_2[i-1] + list_2[i]
            dict_genroman[n*5]=list_2[i]
            n=n*5
        i+=1
    return dict_genroman

def genroman_con_int(genroman):  #got roman_int
    dict_genroman = {}
    list_2 = list(reversed(genroman))
    n = 1
    i = 0
    while i<len(genroman):
        if i==0:
            dict_genroman[list_2[i]]=n
            n=5
        elif i==1:
            dict_genroman[list_2[i]]=n
        elif i % 2==0:
            n=n*2
            dict_genroman[list_2[i]]=n
        elif i%2==1 and i>1:
            n=n*5
            dict_genroman[list_2[i]]=n
        i += 1
    return dict_genroman

def checkgenroman(input_word):
    list_genroman=list(reversed(input_word))
    list_order=[]
    i=0
    while i < len(input_word):
        if len(input_word)-i>=6:
            if list_genroman[i]==list_genroman[i+1] and list_genroman[i]!=list_genroman[i+2] and list_genroman[i]!=list_genroman[i+3] and list_genroman[i]!=list_genroman[i+4] and list_genroman[i+2]!=list_genroman[i+3] and list_genroman[i+2]!=list_genroman[i+4] and list_genroman[i+4]!=list_genroman[i+3] and list_genroman[i+2]==list_genroman[i+5]:#DDACBA
                list_order.append(list_genroman[i])
                list_order.append('_')
                list_order.append(list_genroman[i+3])
                list_order.append('_')
                list_order.append(list_genroman[i+2])
                list_order.append(list_genroman[i+4])
                i+=6
                continue
        if len(input_word)-i>=5:
            if list_genroman[i]==list_genroman[i+1]==list_genroman[i+2]:
                if list_genroman[i+3]==list_genroman[i+4]: #AAABB
                    list_order.append(list_genroman[i])
                    list_order.append('_')
                    i+=3
                    continue
                if list_genroman[i+3]!= list_genroman[i+4]: #AAABC
                    list_order.append(list_genroman[i])
                    list_order.append(list_genroman[i+3])
                    i+=4
                    continue
                if list_genroman[i+2]==list_genroman[i+4]: #AAABA
                    list_order.append(list_genroman[i])
                    list_order.append('_')
                    i+=3
                    continue
            if list_genroman[i]==list_genroman[i+1] and list_genroman[i]!=list_genroman[i+2] and list_genroman[i]!=list_genroman[i+3] and list_genroman[i+2]==list_genroman[i+4] and list_genroman[i+2]!=list_genroman[i+3]:#AABCB
                list_order.append(list_genroman[i])
                list_order.append('_')
                list_order.append(list_genroman[i+3])
                list_order.append('_')
                list_order.append(list_genroman[i+2])
                i+=5
                continue
            if list_genroman[i]!=list_genroman[i+1] and list_genroman[i]!=list_genroman[i+2] and list_genroman[i+1]!=list_genroman[i+2] and list_genroman[i+1]==list_genroman[i+3] and list_genroman[i+1]==list_genroman[i+4]:#ABCBB
                list_order.append(list_genroman[i])
                list_order.append('_')
                list_order.append(list_genroman[i+2])
                list_order.append('_')
                list_order.append(list_genroman[i+1])
                list_order.append('_')
                i+=5
                continue
        if len(input_word)-i>=4:
            if list_genroman[i]==list_genroman[i+1]:
                if list_genroman[i]==list_genroman[i+2] and list_genroman[i+2]!=list_genroman[i+3] and len(input_word)-i==4: #AAAB
                    list_order.append(list_genroman[i])
                    list_order.append(list_genroman[i+3])
                    i+=4
                    continue
                if list_genroman[i]==list_genroman[i+3] and list_genroman[i]!=list_genroman[i+2]:#AABA
                    list_order.append(list_genroman[i])
                    list_order.append('_')
                    i+=2
                    continue
                if list_genroman[i+1]!=list_genroman[i+2] and list_genroman[i+2]==list_genroman[i+3] and list_genroman[i+2:].count(list_genroman[i+2])>1:#AAB...B
                    list_order.append(list_genroman[i])
                    list_order.append('_')
                    i+=2
                    continue
                if list_genroman[i]==list_genroman[i+1] and list_genroman[i+1]!=list_genroman[i+2] and list_genroman[i+2]!=list_genroman[i+3] and list_genroman[i+2:].count(list_genroman[i+2])==1:#AAB...C
                    list_order.append(list_genroman[i])
                    list_order.append(list_genroman[i+2])
                    i+=3
                    continue
            if list_genroman[i]==list_genroman[i+3] and list_genroman[i]!=list_genroman[i+1] and list_genroman[i]!=list_genroman[i+2]:#ACBA
                list_order.append(list_genroman[i+1])
                list_order.append('_')
                list_order.append(list_genroman[i+3])
                if list_genroman[i+2] not in list_genroman[i+3:]:
                    list_order.append(list_genroman[i+2])
                else:
                    list_order.append('_')
                i+=4
                continue
            if list_genroman[i]!=list_genroman[i+1] and list_genroman[i]==list_genroman[i+2]==list_genroman[i+3]:#ABAA
                list_order.append(list_genroman[i+1])
                list_order.append('_')
                i+=2
                continue
        if len(input_word)-i>=3:
            if list_genroman[i]==list_genroman[i+1]:
                if list_genroman[i+2]==list_genroman[i] and len(input_word)-i==3:#AAA
                    list_order.append(list_genroman[i])
                    i+=3
                    continue
                if list_genroman[i+2]!=list_genroman[i] and len(input_word)-i==3:#AAB
                    list_order.append(list_genroman[i + 0])
                    list_order.append(list_genroman[i + 2])
                    i+=3
                    continue
            if list_genroman[i]==list_genroman[i+2] and list_genroman[i]!=list_genroman[i+1]:#ABA
                list_order.append(list_genroman[i + 1])
                list_order.append('_')
                i+=2
                continue
            if list_genroman[i+1]==list_genroman[i+2] and list_genroman[i]!=list_genroman[i+1]:#ABB
                list_order.append(list_genroman[i + 0])
                list_order.append('_')
                i+=1
                continue
            if list_genroman[i]!=list_genroman[i+1]!=list_genroman[i+2] and list_genroman[i+2:].count(list_genroman[i+1])==0:#ABC
                if i >= 2:
                    if list_genroman[i]==list_genroman[i-2]:
                        list_order.append(list_genroman[i])
                        list_order.append(list_genroman[i+1])
                        i+=2
                        continue
                list_order.append(list_genroman[i+1])
                list_order.append(list_genroman[i])
                i += 2
                continue
        if len(input_word)-i>=2:
            if list_genroman[i]==list_genroman[i+1] and len(input_word)-i==2:#AA
                list_order.append(list_genroman[i])
                i+=2
                continue
            if list_genroman[i]!=list_genroman[i+1] and len(input_word)-i==2:#AB
                list_order.append(list_genroman[i+1])
                list_order.append(list_genroman[i])
                i+=2
                continue
        if len(input_word)-i==1:
            list_order.append(list_genroman[i+0])
            i+=1
            continue
        checkInput()
    list_order=list(reversed(list_order))
    return list_order

def checkresult(string): #anti-MMMM
    for i in string:
        if string.index(i)+3<len(string):
            if i==string[string.index(i)+1] and i==string[string.index(i)+2] and i==string[string.index(i)+3]:
                return False
    return True

def checkfive(first,roma_int):
    #roma_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in first:
        if first.index(i)+1<len(first):
            five=str(roma_int.get(i))
            if first.count(i)>1 and five[0]=='5':
                return False
    return True

def differentletter(first,second):
    for i in first:
        if i not in second:
            return False
    return True

try:
    command=input('How can I help you? ')
    if command=='':
        raise NameError
    command=command.strip()
    command=command.split(' ')
    n=len(command)
    i=0
    while i <n:
        if '' in command:
            command.remove('')
            i+=1
        else:
            break
    if command[0]!='Please':
        raise NameError
    if command[1]!='convert':
        raise NameError
    if len(command)>5:
        raise NameError
    if len(command)==5 and command[3]!='using':
        raise NameError
    if len(command)==4 and command[-1]!='minimally':
        raise NameError
except NameError:
    print('I don\'t get what you want, sorry mate!')
    sys.exit()


if len(command)==3:
    command_1=command[-1]
    if checkRomannumber(command_1)==False and checkposinteger(command_1)==False:
        checkInput()
    if command_1[0]=='0': #anti-035
        checkInput()
    if checkresult(command_1)==False:
        checkInput()
    if checkposinteger(command_1)==True:
        int_roma = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',500: 'D', 900: 'CM', 1000: 'M'}
        command_1=int(command_1)
        command_1=int_convert_romannum(command_1,int_roma)
        if checkresult(command_1)==False:
            checkInput()
        print('Sure! It is',command_1)
        sys.exit()
    if checkRomannumber(command_1)==True:
        roma_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        command_11=romannum_convert_int(command_1,roma_int)
        int_roma = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',500: 'D', 900: 'CM', 1000: 'M'}
        command_12=int_convert_romannum(command_11,int_roma)
        if command_1!=command_12:
            checkInput()
        else:
            print('Sure! It is', command_11)
            sys.exit()

elif len(command)==5:
    first_star=command[2]
    second_star=command[-1]
    if checkposinteger(first_star)==False and first_star.isalpha()==False:
        checkInput()
    if second_star.isalpha()==False:
        checkInput()
    if check_distinct(second_star)==False:
        checkInput()
    if checkposinteger(first_star)==False and differentletter(first_star,second_star)==False:
        checkInput()
    if checkposinteger(first_star)==True and first_star[0]=='0':
        checkInput()
    if checkposinteger(first_star)==True:
        int_roma=int_con_genroman(second_star)
        first_star=int(first_star)
        command_2=int_convert_romannum(first_star, int_roma)
        if checkresult(command_2)==False:
            checkInput()
        print('Sure! It is', command_2)
        sys.exit()
    if first_star.isalpha()==True:
        roma_int_2=genroman_con_int(second_star)
        if checkfive(first_star,roma_int_2)==False:
            checkInput()
        command_2=romannum_convert_int(first_star,roma_int_2)
        int_roma_2=int_con_genroman(second_star)
        command_21 = int_convert_romannum(command_2, int_roma_2)
        if first_star!=command_21 and checkresult(command_21)==True:
            checkInput()
        print('Sure! It is', command_2)
        sys.exit()

elif len(command)==4:
    command_3=command[2]
    if command_3.isalpha()==False:
        checkInput()
    if checkresult(command_3)==False:
        checkInput()
    list_order=checkgenroman(command_3)
    using=''.join(list_order)
    list_comp=['1']
    n=1
    for i in list_order:
        if i == '_':
            list_order[list_order.index(i)] = list_comp[-1]
            list_comp.append(n+1)
            n+=1
    if len(set(list_order))!=len(list_order):
        checkInput()
    roma_int_3=genroman_con_int(list_order)
    command_3=romannum_convert_int(command_3,roma_int_3)
    print('Sure! It is', command_3,'using',using)
    sys.exit()









