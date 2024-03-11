my_list = []   
my_list.append(10) 
my_list.append(20)   
my_list.append(30)  
my_list.append(40)   

my_list.insert(1, 15)# Inserting 15 to pos. 1

my_list.extend([50, 60, 70])  # Extend my_list  

my_list.pop()  # Remove the last element  

my_list.sort()  # Sorting ascending order

index_of_30 = my_list.index(30) 

print("my_list:", my_list)
print("Index of 30:", index_of_30)