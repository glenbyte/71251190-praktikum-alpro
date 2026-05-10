def map_lists_to_dict_(list_a, list_b):
    return {list_a[i]: list_b[i] for i in range(len(list_a))}

Listcolor = ['red', 'green', 'blue']
Listnumco = ['#FF0000', '#008000', '#0000FF']

# Using Method 
result = map_lists_to_dict_(Listcolor, Listnumco)
print(result)