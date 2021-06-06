items = ['item1','item2','item3','item4','item5']
max_items = 5

if 'item3' in items:
    print('The item is in the lists')

if len(items) < max_items:
    quests.append('new item')
    print(items)
else:
    print('Max is 5, cannot add new item')

for item in items:
    print(item)
    
for i in range(len(items)):
    print(str(i + 1) + '.' + items[i])