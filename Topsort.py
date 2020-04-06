from collections import defaultdict

'''
0 ---> 1 --> 2 <-- 3
        ^
        |
        4
'''

adjacent = [None]*5
adjacent[0] = 1
adjacent[1] = 2
adjacent[2] = None
adjacent[3] = 2
adjacent[4] = 1

visited = [False]*5

output_stack = []

def dfs( number ):
    if not visited[number]:
        visited[number] = True
        if adjacent[number] != None:
            dfs(adjacent[number])
        output_stack.insert(0, number)

def topsort( source ):
    for i in range(5):
        if not visited[i]:
            dfs(i)

topsort(0)
print(output_stack)