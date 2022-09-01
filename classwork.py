# NumberChecker
num = int(input("Enter number:"))

def classwork_(ran):
    odd=[]
    even=[]
    for i in range(ran):
        if( i%2 == 0) and (i !=0):
           even.append(i)
        else:
            odd.append(i)
    print(f"Even list is : {even}, odd list is: {odd}")


#OR

classwork_(num)

odd_list=[]
even_list=[]
[even_list.append(i) if i%2 ==0 else odd_list.append(i) for i in range(0,num)]
print(f"Even list is : {even_list}, odd list is: {odd_list}")

