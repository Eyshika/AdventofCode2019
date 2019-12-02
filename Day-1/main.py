
def evaluate(mass):
    fuel = round(mass/3) 
    if fuel > 0:
        fuel = fuel - 2
    return fuel

if __name__ == '__main__':
    module = open("input.txt", 'r')
    total = 0
    for mass in module:
        fuel = evaluate(int(mass.strip()))
        total += fuel
     
    print('Total : ' + str(total))
        
    module.close()