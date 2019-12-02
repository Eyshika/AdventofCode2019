## Day - 1

def evaluate(mass):
    newfuel = 0
    fuel = int(mass/3) - 2
    while fuel > 0:
        newfuel += fuel
        fuel = int(fuel/3) - 2
        print(fuel)
        
    return newfuel

if __name__ == '__main__':
    module = open("input.txt", 'r')
    total = 0
    for mass in module:
        fuel = evaluate(int(mass.strip()))
        total += fuel
     
    print('Total : ' + str(total))
        
    module.close()