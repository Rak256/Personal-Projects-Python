def up_low(s):
    iterable_list = []
    u_count = 0
    l_count = 0

    for item in s.split():
        iterable_list.append(list(map(str.isupper, item)))
    
    for internal_list in iterable_list:
        for element in internal_list:
            if element == True:
                u_count += 1
            else:
                l_count += 1
    
    print("Number of upper case letters: " + str(u_count))
    print("Number of lower case letters: " + str(l_count))

up_low("This is a String")