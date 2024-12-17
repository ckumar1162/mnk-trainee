# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path 
# going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing
#  to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore,
#  there will be exactly one destination city

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def DestinaionCity(path):
    source = []
    for i in path:
        source.append(i[0])
    print(source)    
    if i[1] not in source:
        return i[1] 
           

print(DestinaionCity(paths))
print(DestinaionCity([["B","C"],["D","B"],["C","A"]]))
print(DestinaionCity([["A","Z"]]))           