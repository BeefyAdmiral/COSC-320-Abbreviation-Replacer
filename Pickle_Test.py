# Using pickle to read and store a dictionary
import pickle
myDict = {"a": "Anshul", "b": "Banshul"}
pickle.dump(myDict, open("myDict.pkl","wb"))
Dic = pickle.load(open('myDict.pkl','rb'))
print(Dic)