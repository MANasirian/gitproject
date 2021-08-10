import string
import random

print('''You want to choose a password,
your password has 6 characters,
and you can choose how to generate it.''')
lowchar = int(input('Choose how many lower_case characters you want: '))
print(6-lowchar , ' left.')
upchar = int(input('Choose how many upper_case characters you want: '))
digit = 6-(upchar + lowchar)

def pa(lowchar, upchar, digit):
    up = list(string.ascii_uppercase)
    low = list(string.ascii_lowercase)
    dig = list(string.digits)
    pas = []
    prt1 = random.sample(low,lowchar)
    prt2 = random.sample(up,upchar)
    prt3 = random.sample(dig,digit)
    for i in range(len(prt1)):
        pas.append(prt1[i])
    for j in range(len(prt2)):
        pas.append(prt2[j])
    for t in range(len(prt3)):
        pas.append(prt3[t])
    passw = random.sample(pas,6)
    passwo = ''.join(passw)
    return passwo

print(pa(lowchar, upchar, digit))


#jdfsjfkjd
#fdrttnkj;iipu