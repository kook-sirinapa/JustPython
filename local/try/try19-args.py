def average(*scores):
    print(scores)
    sum_score = sum(scores)
    average_score = sum_score / len(scores)
    return average_score

print(str('Kook score average = ') + str(average(75, 50, 65)))
print(str('Sucha sc = ') + str(average(48, 50, 52)))