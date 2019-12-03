inputfile = open("input.txt", 'r').read()
A, B = inputfile.strip().split("\n")
A = list(A.split(','))
B = list(B.split(','))

grid = {'L': (0, 1), 'R': (0, -1), 'U': (1, 1), 'D': (1, -1)} #represents at [0] 0 says x  1 says y location [1] represent value

curr = [0, 0]
steps = 0
signals = {}

for path in A:
    dir, step = path[0], int(path[1:])
    #i, c = grid[dir]
    assert dir in grid  #assertion error if direction not found in grid
    for val in range(step):
        
        curr[grid[dir][0]] += grid[dir][1]
        steps += 1 #to calculate steps at each step for part 2 of question
        signals[tuple(curr)] = steps

steps = 0
curr = [0, 0] 
Intersection = []
for path in B:
    dir, step = path[0], int(path[1:])
    #i, c = grid[dir]
    assert dir in grid  #assertion error if direction not found in grid
    for val in range(step):
        
        curr[grid[dir][0]] += grid[dir][1]
        steps += 1
        #signals[tuple(curr)] = steps
        if tuple(curr) in signals:
            Intersection.append((signals[tuple(curr)]+steps, tuple(curr)))
            print(Intersection)
            
mini = min(abs(val[1][0]) + abs(val[1][1]) for val in Intersection)
few = min(abs(val[0]) for val in Intersection)
print("Manhattan Distance : ", mini)
print("Fewest steps : ", few )
    
