questions = [
    '    555    ',
    '   x + y = ?',
    'why do you leave me?', 
    'what do you want'
]

# - MAP
# --- Map version
# cleaned_questions = list(map(lambda q: q.strip().capitalize(), questions))
# print(cleaned_questions)

# ---list one lined version
cleaned_questions = [q.strip().capitalize() for q in questions]
# print(cleaned_questions)


# - Filter
# -- Filter version
# filter_question = list(filter(lambda q: len(q) >= 10, cleaned_questions))
# print(filter_question)

# --- list one lined version
filter_question = [q for q in cleaned_questions if len(q) >= 10]
print(filter_question)