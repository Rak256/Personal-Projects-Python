#Returns a list that has no repeat elements
def unique_list(list):
    unique_list = []

    for index,item in enumerate(list):
        if list[index] == list[index-1] and index != 0:
            pass
        else:
            same = False
            for k in unique_list:
                if item == k:
                    same = True
                    break
            if same == False:
                unique_list.append(item)


    
    return unique_list

user_list = input("Enter list elements seperated by spaces: ").split()

print (unique_list(user_list))