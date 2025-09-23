# Build a list of list for adjencty list 

def build_list(vertex):
    main_list = []
    for _ in range(vertex + 1):
        main_list.append([])
    return main_list

print(build_list(4))
