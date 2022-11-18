from algo_utils import *  

def evaluation_policy(L,politique , gamma,tN ):
    V_previous=L
    V_next=np.zeros((3,4)) 
    gamma=0.9
    for t in range (tN): 
        for i in range (len(L)):
            for j in range (len(L[i])):
                val=0
                for k in range (len(L)):
                    for l in range (len(L[i])):
                        val+=T ([i,j],[k,l],politique[i][j])* ( L[i][j]+ gamma * V_previous[k][l])  
                V_next[i][j]=val
        V_previous = V_next
    return V_next

def politique_string(politique): 
    Politique=[[],[],[]]
    for i in range (len(politique)): 
        for j in range (len(politique[i])):
            Politique[i].append(get_key(politique[i][j] , dic_dir))
    return Politique

def policy_iteration(L,gamma,K) :
    
    politique_next=np.zeros((3,4))
    politique_previous=np.zeros((3,4))
    for k in range (K): 
        V_previous=evaluation_policy(L,politique_previous,0.9,100)
        for i in range (len(L)):
            for j in range (len(L[i])):
                max_val=-np.inf
                actions=0
                for a in range (4):
                    val=0
                    res=0  # r(s,a)
                    for c in range (len(L)):
                        for l in range (len(L[i])):
                            res+= T ([i,j],[c,l],a) * (L[i][j])
                            val+=T ([i,j],[c,l],a)* ( V_previous[c][l])
                    val*=gamma
                    val=val+res
                    if val> max_val :
                        max_val=val
                        actions=a
                politique_next[i][j]=actions
        if np.array_equal(politique_previous,politique_next) : 
            break
        politique_previous = politique_next
    return politique_next
