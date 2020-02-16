import scipy.io

path = "C:\Users\schouhan\Downloads\CSE 575\\"

Numpyfile= scipy.io.loadmat(path+'mnist_data.mat')

print(",type:", type(Numpyfile))

#print(Numpyfile['trX'])

print(Numpyfile['trX'].shape)
#(12116L, 784L)

print(Numpyfile['trY'].shape)
#(1L, 12116L)

print(Numpyfile['tsX'].shape)
#(2002L, 784L)

print(Numpyfile['tsY'].shape)
#(1L, 2002L)

trMean = Numpyfile['trX'].mean(axis=1)
trStd = Numpyfile['trX'].std(axis=1)

tsMean = Numpyfile['tsX'].mean(axis=1)
tsStd = Numpyfile['tsX'].std(axis=1)


print(trMean.shape,":",trStd.shape,":",tsMean.shape,":",tsStd.shape)

print(trMean)
print(trStd)
print(tsMean)
print(tsStd)
