
file_score_group = open('score_group.txt') 
# print(file.readline())
# print(file.readline())
# count total of student who passed testing
# pass_count = 0
# for score in file_score:
#     score_int = int(score)
#     if score_int >= 50:
#         pass_count += 1
# print('Total of students paaed: ' + str(pass_count))
# file_score.close() 

# Count passed testing
pass_count = 0
for group_scores in file_score_group:
    group_scores_list = group_scores.split(' ')
    for score in group_scores_list:
        score_int = int(score)
        if score_int >= 50:
            pass_count += 1

print('Total of students paaed: ' + str(pass_count)) 
file_score_group.close()  


