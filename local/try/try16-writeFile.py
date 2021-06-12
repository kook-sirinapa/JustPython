file_read = open('score_group.txt')
file_write = open('test.test','w')


file_write.write('Average Score \n\n')
for group_score in file_read:
    sum_score = 0
    group_score_list = group_score.split(' ')
    for score in group_score_list:
        score_int = int(score)
        sum_score += score_int

    average_score = sum_score / len(group_score_list)
    file_write.write(str(average_score) + '\n')


 

file_read.close()
file_write.close()