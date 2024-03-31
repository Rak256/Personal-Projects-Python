#Does not add numbers between 6 and 9 in a list, including. Adds all other list items
def six_to_nine(a):
    add = True
    sum = 0
    for index,item in enumerate(a):
        if a[index] == 6:
            add = False
        if add == True:
            sum += item
        
        if a[index] == 9:
            add = True

    return sum
print (six_to_nine([4,5,6,7,8,9]))
