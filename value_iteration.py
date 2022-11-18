from algo_utils import * 


def value_iteration(L,gamma,tN) :
    V_previous=L
    V_next=np.zeros((3,4))
    politique=np.zeros((3,4))
    for t in range (tN): 
        for i in range (len(L)):
            for j in range (len(L[i])):
                max_val=-np.inf
                actions=0
                for a in range (4):
                    val=0
                    for k in range (len(L)):
                        for l in range (len(L[i])):
                            val+=T ([i,j],[k,l],a)* ( L[i][j] + gamma * V_previous[k][l]) 
                    if val> max_val :
                        max_val=val
                        actions=a 
                V_next[i][j]=max_val
                politique[i][j]=actions
        V_previous = V_next
    return V_next,politique