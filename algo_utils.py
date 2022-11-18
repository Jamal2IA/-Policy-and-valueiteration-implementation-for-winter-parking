import numpy as np 

dic_dir={"left":0 ,"up":1 , "right":2, "down":3}

L=np.zeros((3,4))
L[0][3]=1
L[1][3]=-100
L[1][1]= 0.1 ## 0.1 pour la case creuse

Moveable=[] ### list determining where you can move
for i in range (len(L)):
    for j in range (len(L[i])):
        if L[i][j]!=0.1 :
            Moveable.append([i,j])


def get_key(val , dic_dir):
    for key, value in dic_dir.items():
         if val == value:
             return key
    return "unfound key"

def Perp(case,i):    
    return [case_move(i-1,case) ,case_move(i+1,case)]

def case_move(i,s):   
    if i > 3 :
        i=0 
    if i < 0 :
        i=3
    if i == 0 :
        case=[ s[0]  , s[1]-1]
        if case in Moveable :
            return case
        else :
            return s
    if i == 1:
        case=[ s[0]-1  , s[1]]
        if case in Moveable :
            return case
        else :
            return s
    if i == 2 :
        case=[ s[0]  , s[1]+1]
        if case in Moveable :
            return case
        else :
            return s
        
    if i == 3 :
        case=[ s[0] +1 , s[1]]
        if case in Moveable :
            return case
        else :
            return s


def T(s1,s2,a) : #  s1=[i,j] : State 1  ,  a : actions , s2=[k,l] : state 2   (transition probability)
    actions = a
    case=case_move(actions, s1)
    proba_actions=0
    if s2 == case :
        proba_actions+=0.8
    for s in Perp(s1,actions):
        if s2==s:
            proba_actions+=0.1
    return proba_actions