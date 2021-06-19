# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:24:45 2020

@author: HEENA
"""
import math
# calculating equilidian distance
def equilidian_distance_n(test1,test2):
    euclidean = 0
    
    euclidean_list_complete = []
    for i in range(len(test2)):
        euclidean_list = []
        #accesing the content of list
        for j in range(len(test1)):
            for k in range(len(test1[0])):
                #matrix calculation
                euclidean += pow((test2[i][k]-test1[j][k]),2)      
            euclidean_list.append(math.sqrt(euclidean))
            euclidean = 0
            #sort the distance
            euclidean_list.sort(reverse=True)
        euclidean_list_complete.append(euclidean_list)
        del euclidean_list
    #minimum distance inc ase of matrix eg multiple artist vs multiple artist
    a=euclidean_list_complete[len(euclidean_list_complete)-1]
    # a=euclidean_list_complete
    #return value  
    if len(a)>1:
        a = [x for x in a if x != 0]
    else:
        a=a       
    
    return min(a)




a=[]
def norm(vector):
    for i in range(len(vector)):
        b= math.sqrt(sum(x * x for x in vector[i]))    
        a.append(b)
    return(a)
    

#cosine similarity function
def cosine_simillarity_n(test1,test2):
    #information storage lists
    b=[]
    test1i=[]
    test2i=[]
    z=[]
    cos1=[]
    for i in range(len(test1)):
        for j in range(len(test2)):
            for p in range(len(test1[i])):
                #dot product of vector
                dot=test1[i][p]*test2[j][p]
                b.append(dot)
    for i in range(len(test1)):
        for j in range(len(test1[i])):
            #squaring the value of u
                u=test1[i][j]**2
                test1i.append(u)
    for i in range(len(test2)):
        for j in range(len(test2[i])):
            #squaring each value
                v=test2[i][j]**2
                test2i.append(v)
#combining list together for nested
    if len(test1)>1:
        m=[list(t) for t in zip(*[iter(b)]*len(test1[1]))]
        q=[list(t) for t in zip(*[iter(test1i)]*len(test1[1]))]
        r=[list(t) for t in zip(*[iter(test2i)]*len(test2[1]))]
#single value list
    else:
        m=b
        q=test1i
        r=test2i
        

    #taking the square root for calculation for nested list
    if len(test1)>1:
        z1=[math.sqrt(sum(q[i])) for i in range(len(q))]
        z2=[math.sqrt(sum(r[i])) for i in range(len(r))]
        z3=[sum(m[i]) for i in range(len(m))]
    else: 
        #square root single list
        z1=[math.sqrt(sum(q))]
        z2=[math.sqrt(sum(r))]
        z3=[sum(m)]    


     #list of vector product
    for i in range(len(z1)):
        for j in range(len(z2)):
            product=z1[i]*z2[j]
            z.append(product)
    #cosine vormula calculation    
    for i in range(len(z)):
        cos=z3[i]/z[i]
        cos1.append(cos)

    #return minimum valus in case of matrix
    return(min(cos1))
#Pearson correlation
def correlation(x, y):
    #empty lists for value storage
    x_bar=[]
    y_bar=[]
    c=[]
    d=[]
    p=[]
    #x mean value calculation
    for i in range(len(x)):
        x_bar = sum(x[i]) / len(x[i])
        c.append(x_bar)
 
    #y mean valuc calculation
    for j in range(len(y)):
        y_bar = sum(y[j]) / len(y[j])
        d.append(y_bar)
    #squared value of mean substracted by individual value
    for i in range(len(c)):
        for j in range(len(d)):
            var_x = sum((x_i - c[i])**2 for x_i in x[i])
            var_y = sum((y_i - d[j])**2 for y_i in y[j])
        #Leanth check condition
        assert len(x[i]) == len(y[j])
        #Pearson Correlation Coefficient calculation
        numerator = sum((x_i - c[i]) * (y_i - d[j]) for x_i, y_i in zip(x[i], y[j]))
        denominator = math.sqrt(var_x * var_y)
        q=numerator / denominator
        #list in case of matrix
        p.append(q)
    #returing maximum in case of matrix
    return min(p)

def compute_jaccard_index(set_1, set_2):
    #empty list for storage
    a=[]
    #set conversion
    for i in range(len(set_1)):
        set_1[i]=set(set_1[i])
    for j in range(len(set_2)):
        set_2[j]=set(set_2[j])   
    #calculation of Jaccard Distance Coefficient
    for i in range(len(set_1)):
        for j in range(len(set_2)):
        
            n = len(set_1[i].intersection(set_2[j]))
            b=n / float(len(set_1[i]) + len(set_2[j]) - n)  
        a.append(b)
    return max(a)
#split function
def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs
#manhattan/cityblock distance calculation
def manhattan_distance(test1,test2):
    a=[]
    for i in range(len(test1)):
        for j in range(len(test2)):
            for q in range(len(test1[i])):
                #individual value difference
                res=test1[i][q]-test2[j][q]
                a.append(abs(res))
    #storage variables            
    b=[]
    l1=[]
    c=[a]
    #multiple list
    if len(test1)>1:
        b=[list(t) for t in zip(*[iter(a)]*len(test1[1]))]

    else:
        b=c
    #calculation of manhattan/cityblock distance
    for i in range(len(b)):
        l1.append(sum(b[i]))
    if len(l1)>1:
        l1 = [x for x in l1 if x != 0]
    else:
        l1=l1       
    

    return min(l1)


