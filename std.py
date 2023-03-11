import numpy as np

TP_list = np.linspace(1,50,50)
n=9
SMA = np.sum(TP_list[n-51:n])/50
UB = SMA + 2*np.std(TP_list[n-51:n])
MB = np.sum(TP_list[n-51:n])/50
LB = SMA - 2*np.std(TP_list[n-51:n])

print(UB)
print(SMA)
print(np.std(TP_list[n-51:n]))

if 10<n<20:
    print(1)
else:
    print(2)