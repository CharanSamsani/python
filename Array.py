# questions @ https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md


exp = [2200, 2350, 2600, 2130, 2190]
total = 0

print("I have spent ", exp[1]-exp[0], "$ extra in February compared to january")

print("Total expenses in first quarter are ", exp[0]+exp[1]+exp[2])

for i in exp :
    if i == 2000 :
        print("YES")
    else :
        print("NO")

exp.append(1989)
print(exp)

new = exp[3]
exp.remove(exp[3])
exp.insert(3, new + 200)
print(exp)

#---------------------------------------------------------------------------------------------------

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
print(heros.__len__())

heros.append("black panther")
print(heros)

heros.pop()
heros.insert(3, "black panther")
print(heros)

heros[1:3]=["doctor strange"]
print(heros)

heros.sort()
print(heros)

odd = []
X = int(input("Enter a number : "))
for i in range (1, X) :
    if i % 2 != 0:
        odd.append(i)
print("These are the odd numbers from 1 to",X ,odd)
