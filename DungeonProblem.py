import queue

# Rows and Columns
R = 5
C = 7

# Creating the matrix
m = [['-' for x in range(C)] for y in range(R)] 

m[0][3] = '#'
m[1][1] = '#'
m[1][5] = '#'
m[2][1] = '#'
m[3][2] = '#'
m[3][3] = '#'
m[4][0] = '#'
m[4][2] = '#'
m[4][5] = '#'

m[4][3] = 'E'

# row direction and column direction for the adjacents
rd = [-1, +1, 0, 0]
cd = [0, 0, -1, +1]

# queue for the checks
rq = queue.Queue()
cq = queue.Queue()

# boolean for the flags
visited = [[False for x in range(C)] for y in range(R)] 

# checking how many steps needed to get to the exit
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

# boolean to check if we are able to get to the exit
reached_end = False

# source / starting point of the pathfinding
sr = sc = 0

# the algorithm
rq.put(sr)
cq.put(sc)

visited[sr][sc] = True

while not rq.empty():
    r = rq.get()
    c = cq.get()

    if m[r][c] == 'E':
        reached_end = True
        break
    
    for i in range(4):
        rr = r + rd[i]
        cc = c + cd[i]

        if rr >= R or cc >= C:
            continue
        if rr < 0 or cc < 0:
            continue

        if visited[rr][cc]:
            continue
        if m[rr][cc] == '#':
            continue
        
        rq.put(rr)
        cq.put(cc)
        nodes_in_next_layer += 1    
    
    nodes_left_in_layer -= 1
    if nodes_left_in_layer == 0:
        nodes_left_in_layer = nodes_in_next_layer
        nodes_in_next_layer = 0
        move_count += 1
if reached_end:
    print(move_count)
else:
    print("There is no way out")