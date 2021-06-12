def clean_text(text):
    return text.strip().capitalize()


clean_text2 = lambda text: text.strip().capitalize()

input_firstname = '  sirinapa'
output_firstname = clean_text2(input_firstname)
print(output_firstname)

input_lastname = 'suraSO'
output_lastname =  clean_text2(input_lastname)
print(output_lastname)