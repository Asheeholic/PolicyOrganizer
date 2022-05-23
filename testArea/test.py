add_list = []

# data = {
#     'name' : 'jaeho', 
#     'age' : 5,
# }
data = {}
data['name'] = 'jaeho'

data2 = {}
data2['name'] = 'jaeho2'


add_list.append(data)
add_list.append(data2)

print(add_list[0])
add_list[1].update({'age' : 6})

print(add_list[0])
print(add_list)
