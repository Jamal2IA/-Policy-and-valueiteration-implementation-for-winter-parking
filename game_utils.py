
from algo_utils import *  

def move_proba(direction, Player):   
    if np.random.rand() > 0.8 : 
        if np.random.rand() > 0.5 : 
            return move(dic_dir[direction] + 1, Player)
        else : 
            return move(dic_dir[direction] - 1, Player)
    else : 
        return move(dic_dir[direction], Player)
    
def move(i,Player): 
    if i > 3 :
        i=0 
    if i < 0 :
        i=3
    if i == 0 :
        case=[ Player["position"][0]  , Player["position"][1]-1]
        if case in Moveable :
            Player["position"]= case
            print("You moved ",get_key(i ,dic_dir) )
        
    if i == 1:
        case=[ Player["position"][0] -1 , Player["position"][1]]
        if case in Moveable :
            Player["position"]= case
            print("You moved ",get_key(i ,dic_dir) )
    if i == 2 :
        case=[ Player["position"][0]  , Player["position"][1]+1]
        if case in Moveable :
            Player["position"]= case
            print("You moved ",get_key(i ,dic_dir) )
        
    if i == 3 :
        case=[ Player["position"][0] +1 , Player["position"][1]]
        if case in Moveable :
            Player["position"]= case
            print("You moved ",get_key(i ,dic_dir) )
    Player["score"]+= L[Player["position"][0]][Player["position"][1]]
    return Player