#!/snap/bin/python0
count = 0

f = open("input.txt", "r")

for line in f:
    line = line.strip()
    #sample input line: '10-11 w: ldslpwbbqwpwtd'
    index, letter, password = line.split(" ")
    index = index.split("-")
    min_, max_ = [int(i) for i in index] 
    valid_range = range(min_, max_+1)#+1 because the end is inclusive


    letter = letter[0] #remote the ':'

    letter_count = password.count(letter)

    if letter_count in valid_range:
        count += 1


f.close()
print(count)
