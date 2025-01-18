# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start withan empty dictionary & add one by one. Use subject name as key & marks as value
subjects = {}

subjects.update({"first_subject": input("Enter 1st subject marks: ")})
subjects.update({"second_subject": input("Enter 2nd subject marks: ")})
subjects.update({"third_subject": input("Enter 3rd subject marks: ")})

print(subjects)
