import pickle

data = {"x": 1, "y": 2}

pickle.dump(data, open("data.pkl", "wb"))   
print(pickle.load(open("data.pkl", "rb")))