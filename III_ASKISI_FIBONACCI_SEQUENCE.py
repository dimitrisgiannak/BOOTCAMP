
'''
list1=[0,1]
num=list1[0]

while num<50:
   print(num)
   
  
   num=list1[0]+list1[1]
   
   list1[0]=list1[1]
   
   list1[1]=num
  
 '''
   
list1=[1,0]



while len(list1)!=10:
   list1.insert(0,(list1[0]+list1[1]))
else:
   list1.reverse()
   print(list1)
   
   
      
   
   
  
   
   
  
   
