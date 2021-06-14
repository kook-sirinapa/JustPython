def check_passed(**scores):
    math = scores.get('math')
    physics = scores.get('physics')
    english = scores.get('english')
    name = scores.get('name')

    print(str('Result of ') + str(name))
    if math is not None and math >= 50:
        print(name + ' is passed Math')
    else:
        print('Sorry, you are not passed Math testing')

    if physics is not None and physics >= 50:
        print(name + ' is passed Physics')
    else:
        print('Sorry, you are not passed Physics testing')

    if english is not None and english >= 50:
        print(name + 'is passed English')
    else:
        print('Sorry, you are not passed English testing')

check_passed(name = 'Sucha', math=50, physics=55, english=0)
print('\n' + '=============================')
check_passed(name = 'Kook', math=90, physics=55, english=10) 


