count = 0

with open("input.txt", "r") as f:
    for line in f:
        #sample input line: '10-11 w: ldslpwbbqwpwtd'
        index, letter, password = line.split(" ")
        index = index.split("-")
        index = [int(i)-1 for i in index] #-1 because the input is 1 indexed

        password = password.strip()

        letter = letter[0] #remote the ':'

        #Only index[0] or index[1] should match the letter,
        #never both or neither for valid passwords.
        #That sounds like an XNOR aka != operator.
        valid = (password[index[0]] == letter) != (password[index[1]] == letter)
        print([i+1 for i in index], letter, password, valid)
        if valid:
            count += 1
print(count)
