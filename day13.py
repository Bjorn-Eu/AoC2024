import re
import numpy as np
def find_cost(A,B,target):
    A = np.array(A,dtype='f')
    B = np.array(B,dtype='f')
    mat = np.column_stack((A, B))
    t = np.array(target,dtype='f')
    out = np.linalg.solve(mat,t)
    n = out[0]
    m = out[1]
    if np.mod(n,1)==0 and np.mod(m,1)==0:
        if n>=0 and m>=0 and n<= 100 and m<= 100:
            return 3*n+m
    return 0 #not a solution

def find_cost2(A,B,target):
    c = 10000000000000
    A = np.array(A,dtype='float32')
    B = np.array(B,dtype='float32')
    mat = np.column_stack((A, B))
    t = c+np.array(target,dtype='float32')
    out = np.linalg.solve(mat,t)
    n = np.round(out[0],decimals=3)
    m = np.round(out[1],decimals=3)
    #we adjust for rounding errors to check if integer solution
    #a more accurate solution would round and then check if it is a solution..
    if np.mod(n,1)==0 and np.mod(m,1)==0:
        if n>=0 and m>=0:
            return 3*n+m
        
    return 0 #not a solution


f = open('data/day13.txt')
data = f.read()

#prepare date
X_data = re.findall("X\+\\d+",data)
Y_data = re.findall("Y\+\\d+",data)
X_target = re.findall("X=\\d+",data)
Y_target = re.findall("Y=\\d+",data)
X_data = [s[2:] for s in X_data]
Y_data = [s[2:] for s in Y_data]
X_target = [s[2:] for s in X_target]
Y_target = [s[2:] for s in Y_target]
n_targets = len(X_target)

#calculate cost
total_cost = 0
for i in range(n_targets):
    target = [X_target[i],Y_target[i]]
    A =[X_data[2*i],Y_data[2*i]]
    B = [X_data[2*i+1],Y_data[2*i+1]]
    cost = find_cost(A,B,target)
    if cost != -1:
        total_cost += cost

print("The total cost is ",total_cost)

#calculate adjusted cost
n_targets = len(X_target)
total_cost = 0
for i in range(n_targets):
    target = [X_target[i],Y_target[i]]
    A =[X_data[2*i],Y_data[2*i]]
    B = [X_data[2*i+1],Y_data[2*i+1]]
    cost = find_cost2(A,B,target)
    if cost != -1:
        total_cost += cost

print("The total adjusted cost is ",total_cost)

