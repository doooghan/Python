import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)

f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlsit = pickle.load(f)
print(storedlsit)
