possible_numbers_list = ['{}'.format(str(i)).rjust(4,'0') for i in range(10000)]
total = len(possible_numbers_list)
count_repeated = 0
count_sequency = 0
added = False

for j in possible_numbers_list:
    counts = [j.count(number) for number in j]
    for c in counts:
        if(c>1):
            count_repeated += 1
            added = True
            break
    if(added):
        added = False
        continue
    for num in j:
        ant = int(num) - 1
        suc = int(num) + 1
        if( str(ant) in j or str(suc) in j ):
            count_sequency += 1
            added = True
            break
    if not added:
        print(j, ' counter example')
    added = False


print('\nProbability =', (count_repeated + count_sequency) / total, end='\n\n')