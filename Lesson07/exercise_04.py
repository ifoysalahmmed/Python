# WAF to find in which line of the file does the word “learning” occur first. Print -1 if word not found.
def find_occur(file, word):
    data = True
    line = 1
    with open(file, "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line)
                return
            line += 1
    print(-1)


find_occur("practice.txt", "xlearning")
