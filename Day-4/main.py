from collections import Counter 

def part_1(input_range):
    count = 0
    for val in range(input_range[0], input_range[1]+1):
        if any(x >= 2 for x in Counter(str(val)).values()):
            new_val = int(''.join(sorted(str(val))))
        #print(new_val)
            if new_val >= val:
                count += 1
            #print(new_val)
    print(count)
    return count

def part_2(input_range):
    count = 0
    for val in range(input_range[0], input_range[1]+1):
        if any(x == 2 for x in Counter(str(val)).values()):
            new_val = int(''.join(sorted(str(val))))
        #print(new_val)
            if new_val >= val:
                count += 1
            #print(new_val)
    print(count)
    return count

input_range = [156218, 652527]

count = part_1(input_range)
print("Part 1", count)
count = part_2(input_range)
print("Part 2 ", count)
