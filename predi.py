from tensorflow.keras.models import load_model
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import matplotlib.pyplot as plt


model = load_model('CNN/Invdep20240213.h5')
model.load_weights('CNN/Invdep20240213_.ckpt')


data1=np.load('data_obs3.npy')
time_channels = np.logspace(np.log10(5e-5), np.log10(1.0e-3), 21)  #define cut-off time
#time_channels = np.logspace(-5, -1.0s, 21)


data1_comb=[]
for i in range(data1.shape[0]):
    
    temp=data1[i,:]
    tem1=np.zeros([32,1,2])
    Np=len(time_channels)
    tem1[:Np,0,0]=-np.log10(time_channels)
    tem1[:Np,0,1]=-np.log10(abs(temp)*1e4)
    tem1[-1,0,0]=0   #Transmitter height
    tem1[-1,0,1]=0   #Receiver height
    data1_comb.append(tem1)
data1_comb=np.array(data1_comb)

prediction = model.predict(data1_comb)

print(prediction)

np.save('prediction_depth.npy', prediction)


#test
plt.rcParams.update({"font.size": 16})
fig = plt.figure(figsize=(7, 4))
max_depth=350
X=np.linspace(0,max_depth,100)
plt.plot(X,prediction[15],color='black')
#plt.plot(X,Y_train[-323])
plt.ylabel(r"$Probability$", fontsize=18)
plt.xlabel(r"$Depth (m)$", fontsize=18)
#plt.gca().invert_yaxis()


plt.subplots_adjust(top=0.95,bottom=0.18,left=0.13,right=0.95)
plt.savefig('predi0.jpg',dpi=500)