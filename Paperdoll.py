# Returns a string with each character repeated 3 times

def Paper_doll(a):
    final_list = []
    more = list(a)

    for item in more:
        for _ in range(3):
            final_list.append(item)

    return "".join(final_list)

b = input("Enter your string: ")

print (Paper_doll(b))
