"""Original coursework functions, extracted without algorithm changes.
Benchmark driver and dataset import removed for independent use.
"""
def edgesum(gr):
    w_sum = 0
    l = len(gr)
    for i in range(l):
        for j in range(i,l):
            w_sum += gr[i][j]
    return w_sum

def dijktra(gr, start, end):
    shrt = [0 for i in range(len(gr))]
    slct = [start]
    l = len(gr)
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i==start):
            shrt[start] = 0 #gr[start][start]
        else:
            if(gr[start][i]==0):
                shrt[i] = inf
            else:
                shrt[i] = gr[start][i]
                if(shrt[i] < min_sel):
                    min_sel = shrt[i]
                    ind = i
                
    if(start==end):
        return 0
    # Dijktra
    slct.append(ind) 
    while(ind!=end):
        #print('ind',ind)
        for i in range(l):
            if i not in slct:
                if(gr[ind][i]!=0):
                    #Check if distance needs to be updated
                    if((gr[ind][i] + min_sel) < shrt[i]):
                        shrt[i] = gr[ind][i] + min_sel
        temp_min = 1000000
        #print('shortest:',shortest)
        #print('selected:',selected)
        
        for j in range(l):
            if j not in slct:
                if(shrt[j] < temp_min):
                    temp_min = shrt[j]
                    ind = j
        min_sel = temp_min
        slct.append(ind)
    
    return shrt[end]

def oddverts(gr):
    dgr = [0 for i in range(len(gr))]
    for i in range(len(gr)):
        for j in range(len(gr)):
                if(gr[i][j]!=0):
                    dgr[i]+=1
    #print('\n')            
    #print('The degrees of the vertices are:',dgr)
    #print('\n')
    odds = [i for i in range(len(dgr)) if dgr[i]%2!=0]
    #print('The odd vertices are:',odds)
    #print('\n')
    return odds

def pairmaker(odds):
    pair = []
    for i in range(len(odds)-1):
        pair.append([])
        for j in range(i+1,len(odds)):
            pair[i].append([odds[i],odds[j]])
        
    #print('The vertex pairs are:',pair)
    #print('\n')
    return pair

def CPP(gr):
    odds = oddverts(gr)
    if(len(odds)==0):
        return edgesum(gr)
    pair = pairmaker(odds)
    l = (len(pair)+1)//2
    
    pairings_sum = []
    
    def pairs(pair, done = [], final = []):
        
        if(pair[0][0][0] not in done):
            done.append(pair[0][0][0])
            
            for i in pair[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    pairs(pair[1:],val, f)
                    
        else:
            pairs(pair[1:], done, final)
            
    pairs(pair)
    min_sums = []
    
    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            s += dijktra(gr, i[j][0], i[j][1])
        min_sums.append(s)
    
    added_dis = min(min_sums)
    distance = added_dis + edgesum(gr)
    return distance
