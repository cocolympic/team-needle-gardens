with open("sample.txt", "r") as f:
    print(f.read(5))  
    f.seek(0)      
    print(f.read(5))  