for i in range(1, 13):
    double= i * 2
    print(double)

print('\n==end==\n')
for i in range(1, 7):
    if i % 3 == 0:
        continue
    print(i)

print('\n==end==\n')
for i in range(1, 7):
    if i % 3 == 0:
        break
    print('break' + str(i))

print('\n==end==\n')