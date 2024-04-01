import pickle

obj = {
    'Talha': '0323-4003815',
    'Boss': 3227840263
}
file = open('D://PYTHON//File_Handeling//p2.dat', 'wb')

pickle.dump(obj, file)
file.close()
