# WAF that replace all occurrences of “Java” with “python” in above file.
def replace_word(file, old_word, new_word):
    with open(file, "r") as f:
        data = f.read()
    new_data = data.replace(old_word, new_word)

    with open(file, "w") as f:
        f.write(new_data)


replace_word("practice.txt", "Java", "Python")
