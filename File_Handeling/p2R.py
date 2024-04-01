import pickle
file = open('D://PYTHON//File_Handeling//p2.dat', 'rb')
v = pickle.load(file)
# v = file.read()
print(v)
