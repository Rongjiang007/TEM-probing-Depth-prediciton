# TEM-probing-Depth-prediciton

TEM probing Depth prediciton program writen by Rongjiang Tang 2024.2.14

Code enviroment:
Python 3.8.5
Tensorflow 2.10.0


To run the code on a Linux system simply

python predi.py


If you need to training a new model, and you may down load the training data form https://zenodo.org/records/10656048
************************************************************************
                     Input and output format     
************************************************************************

The input data format is a two-dimensional numpy array, where the first dimension represents the measurement point index, 
and the second dimension represents the induced electromotive force (unit: T). The transmitter moment is set to 1e4.
Both the cut-off time and the induced electromotive force have taken logarithm and absolute value processing in the code. 
The cut-off time can modified and is defined in the program. The flight height of the ATEM coil can also be defined in the program.


The output data format is a two-dimensional numpy array, where the first dimension represents the measurement point index, 
and the second dimension represents the distribution of predicted depths, with the maximum value corresponding to the predicted probing depth.


Reference:
Tang, R., Gan, L., Li, F., & Shen, F. (2023). A Deep learning estimation for probing Depth of Transient Electromagnetic Observation. Authorea Preprints.
