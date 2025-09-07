with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()