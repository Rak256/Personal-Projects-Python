def Has_33(L):
    for index,item in enumerate(L[:-1]):
        if item == 3 and L[index+1] == 3:
             return True
        
    return False
        

item = input("Enter the list elements seperated with spaces: ")

list = item.split()

list = [int(element) for element in list]

print (Has_33(list))