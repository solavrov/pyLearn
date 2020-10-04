from itertools import permutations


w = 'ФЗФТШМФТИ'
p = permutations(w, len(w))
p = list(set(p))

for i in range(0, len(p)):
    p[i] = ''.join(p[i])

c = 0
for i in range(0, len(p)):
    if not('ТШ' in p[i]) and not('ФЗ' in p[i]) and not('ФТ' in p[i]):
        c += 1

print('answer:', c)





