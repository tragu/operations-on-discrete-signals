# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:12:13 2018

@author: tanka

"""
def coordinates(d,e):
    
    h=-e+1
    g=[]
    j=0
    while j<len(d):
      g.append(h)
      h=h+1
      j=j+1
    i=[]
    for j in range(len(d)):
      i.append((g[j],d[j]))
    return i;

def take():
    a=[int(x) for x in input('Enter numbers with comma seperated:').split(',')]
    return a;
def take1():
    a=[int(x) for x in input('Enter next numbers with comma seperated:').split(',')]
    return a;

if __name__=='__main__':
   z=int(input('For Amplitude scaling:1,Time shifting:2, Signal addition:3, Signal multiplication:4, Time scaling:5 :-'))
   
   if z==1: 
    b=[]
    #Amplitude scale version for given signal
    a=take()
    n=int(input('enter the scaling factor:'))
    for i in a:
        c=i*n
        b.append(c)
    print(b)
   
    
   elif z==2: 
    #Time shifting
    d=take()
    e=int(input('Enter the position of zero index:'))
    i=coordinates(d,e)
    m=[]   
    y=int(input('enter the shifting factor:'))
    for k in range(len(i)):
      m.append((i[k][0]-y,i[k][1]))
    print(m)
    
   elif z==3: 
    #signal addition
    d=take()
    e=int(input('Enter the position of zero index:'))
    i=coordinates(d,e)

    d1=take1()
    e1=int(input('Enter the position of zero index:'))
    i1=coordinates(d1,e1)

    my_dict = {}
    for k in range(0,len(i)):
       my_dict[str(i[k][0])] = i[k][1]
    
    my_dict1 = {}
    for k in range(0,len(i1)):
       my_dict1[str(i1[k][0])] = i1[k][1]
    
    o={ k: my_dict.get(k, 0) + my_dict1.get(k, 0) for k in set(my_dict)|set(my_dict1) }
    print(o)
    
   elif z==4:
    #signal multiplication
    d=take()
    e=int(input('Enter the position of zero index:'))
    i=coordinates(d,e)

    d1=take1()
    e1=int(input('Enter the position of zero index:'))
    i1=coordinates(d1,e1)

    my_dict = {}
    for k in range(0,len(i)):
       my_dict[str(i[k][0])] = i[k][1]
    
    my_dict1 = {}
    for k in range(0,len(i1)):
       my_dict1[str(i1[k][0])] = i1[k][1]
    
    o={ k: my_dict.get(k, 0) * my_dict1.get(k, 0) for k in set(my_dict)|set(my_dict1) }
    print(o)
    
   elif z==5:
     #Time scaling
    d=take()
    e=int(input('Enter the position of zero index:'))
    n = input("Enter the number to multiply: ")
    i=coordinates(d,e)
    try:
      num,den = map(int,n.split('/'))
    except ValueError:
      num=int(n)
      den=1 
    my_dict = {}
    for k in range(0,len(i)):
       my_dict[int(i[k][0])] = i[k][1]
       
    o={ k: my_dict.get((k*num)/den, 0) for k in range(-den*len(my_dict),den*len(my_dict)) }
    print(o)
     
       
       