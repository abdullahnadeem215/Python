list=[1,2,4,6,7]

reverse_list=[]


for i in range(len(list)-1,-1,-1):
    reverse_list.append(list[i])

print(reverse_list)