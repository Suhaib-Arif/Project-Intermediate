student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
#     pass    #Access key and value



import pandas
student_data_frame = pandas.DataFrame(student_dict)


# student_marks={}
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # student_marks[row.student]=row.score
    # Access index and row
    #Access row.student or row.scor
    # print(row.letter)
    # pass
# print(student_marks)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}


data=pandas.read_csv("nato_phonetic_alphabet.csv")
letter_phonetic={}

letter_phonetic={rows.letter: rows.code for (index, rows) in data.iterrows()}


print(letter_phonetic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input=input("Word: ").lower()

split_input=[leteer for leteer in user_input]

phonetic_name=[letter_phonetic[letter.upper()] for letter in split_input]

print(phonetic_name)