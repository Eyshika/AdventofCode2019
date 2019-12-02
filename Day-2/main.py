from itertools import combinations_with_replacement

def solve(data, noun = 12, verb = 2):
    #update data before system caught fire
    prog = data[:]
    prog[1] = noun
    prog[2] = verb
    
    for i in range(0,len(prog),4):
        if prog[i] == 1:
            prog[prog[i+3]] = prog[prog[i+1]] + prog[prog[i+2]]
        elif data[i] == 2:
            prog[prog[i+3]] = prog[prog[i+1]] * prog[prog[i+2]]
        elif prog[i] == 99:
            break
    return prog

if __name__ == '__main__':
    inputfile = open("input.txt", 'r')
    for line in inputfile:
        data = list(map(int, line.strip().split(','))) 
            
    comb = combinations_with_replacement(range(100),2)
    for comb_i in list(comb):
        noun = comb_i[0]
        verb = comb_i[1]
        data_new = solve(data, noun, verb)
            
        if data_new[0] == 19690720:
            print("val", 100 * noun + verb)
            break
    print("First place: " ,data_new[0])
