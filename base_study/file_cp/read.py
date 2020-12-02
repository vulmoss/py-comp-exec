filename = input('please you will read the file name :')
with open(filename) as file1:
    count = 0
    for line in file1:
        count += 1
        print(line)
print('line is :',count)
