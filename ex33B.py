def load_a_list(list_size, step_size):
    i = 0
    my_list = []

    while i < list_size :
        my_list.append(i)
        i = i + step_size
    return my_list
    
numbers = load_a_list(7, 2)
for num in numbers:
    print num