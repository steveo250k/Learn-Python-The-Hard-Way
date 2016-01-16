def load_a_list(list_size):
    i = 0
    my_list = []

    while i < list_size :
        my_list.append(i)
        i = i + 1
    return my_list
    
numbers = load_a_list(7)
for num in numbers:
    print num