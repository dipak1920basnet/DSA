# Generate matrix 
new_list = []
for i in range(4):
    inside = []
    for j in range(4):
        inside.append(0)
    new_list.append(inside)

for j in range(len(new_list)):
    print(new_list[j])
    