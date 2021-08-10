import math

def perfect_numbers(n):
    f_list = []
    for i in range(1,n):
        g_list = []
        for j in range(1,math.floor(i/2)+1):
            if i%j == 0:
                g_list.append(j)
            else:
                pass
        if sum(g_list) == i:
            f_list.append(i)
        else:
            pass

    print(f_list) 
    
sat = (('m11','m12','m13'),('l11','l12','l13'),('r11','r12','r13'))
sun = (('m21','m22','m23'),('l21','l22','l23'),('r21','r22','r23'))
mon = (('m31','m32','m33'),('l31','l32','l33'),('r31','r32','r33'))
tue = (('m41','m42','m43'),('l41','l42','l43'),('r41','r42','r43'))
wed = (('m51','m52','m53'),('l51','l52','l53'),('r51','r52','r53'))
thu = (('m61','m62','m63'),('l61','l62','l63'),('r61','r62','r63'))
fri = (('m71','m72','m73'),('l71','l72','l73'),('r71','r72','r73'))
date = {'saturday':sat,'sunday':sun,'monday':mon,'tuesday':tue,
                     'wednesday':wed,'thursday':thu,'friday':fri}

class restaurant:
    def __init__(self,date):
        self.date = date
        
    def pish(self):
        tedad = [30,30,30]
        day = input('enter the day: ')
        while day not in date.keys():
            day = input('enter the day: ')
        else:
            pass
        print(date[day][0])
        choice = 
        #vayvayvay
        
#vayvayvay
#dlkjfalkjfkdj
