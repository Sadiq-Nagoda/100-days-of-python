
#####################LIST COMPREHENSION###########################
# new_list = [new_item for item in list]




# numbers = [1,2,3,4,5,6,7,8,9]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)


# name = "Sadiq"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n*2 for n in range(1,5)]
# print(new_list)


#####################CONDITIONAL LIST COMPREHENSION#####################
# new_list = [new_item for item in list if test]


# names = ["Sadiq", "Umar", "Usman", "Aliyu", "Abdul", "Khalid"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# l_names = [name.upper() for name in names if len(name) == 5]
# print(l_names)





#############################DICTIONARY COMPREHENSION###################
# new_dict ={new_key:new_value for item in list}

# import random
# names = ["Aisha", "Umar", "Sadiq", "Sakina", "Al-mustapha", "yahya", "Engineer", "Ismail"]
# student_score = {student:random.randint(70, 100) for student in names}
# # print(student_score)
# # new_dict ={new_key:new_value for (key, value) in dict.items()}
# top_students = {student:scores for (student, scores) in student_score.items() if scores >= 90}
# print(top_students)




#############################CONDITIONAL DICTIONARY COMPREHENSION###################
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}



############################Loop Through a DataFrame##################################
# ccv 