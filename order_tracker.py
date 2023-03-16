import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_orders(logfile):
    ETF_TP = list()
    FUTURE_TP = list()
    SEQ = list()
    with open(logfile) as f:
        for line in f.readlines():
            words = line.split(' ')
            if 'book' in words:
                idx_etf = words.index('equals') + 2
                idx_fut = words.index('equals') + 3
                idx_SEQ = words.index('sequence') + 2
                ETF_TP.append(float(words[idx_etf].split('=')[1]))
                FUTURE_TP.append(float(words[idx_fut].split('=')[1]))
                SEQ.append(int(words[idx_SEQ]))
    plt.plot(SEQ[10:486], ETF_TP[10:486], label='ETF Typical Price')
    plt.plot(SEQ[10:486], FUTURE_TP[10:486], label='FUTURE Typical Price')
    plt.title('Price for {0}'.format(logfile.split('.')[0]))
    plt.legend()
    plt.show()


with open('test1.txt') as f:
    lines = f.readlines()
    cnt = 0
    FUTURE_ask_0 = list()
    FUTURE_bid_0 = list()
    ETF_ask_0 = list()
    ETF_bid_0 = list()

    for line in lines:
        if cnt % 2 == 0:
            new_idx = line.index('\n')
            line = line[:new_idx]
            entries = line.split(',')
            FUTURE_bid_0.append(float(entries[0].split(':')[1]))
            FUTURE_ask_0.append(float(entries[1].split(':')[1]))
        else:
            new_idx = line.index('\n')
            line = line[:new_idx]
            entries = line.split(',')
            ETF_bid_0.append(float(entries[0].split(':')[1]))
            ETF_ask_0.append(float(entries[1].split(':')[1]))
        cnt += 1
ETF_bid_0 = np.array(ETF_bid_0)
ETF_ask_0 = np.array(ETF_ask_0)
FUTURE_bid_0 = np.array(FUTURE_bid_0)
FUTURE_ask_0 = np.array(FUTURE_ask_0)
bid_diff = ETF_bid_0 - FUTURE_bid_0
ask_diff = ETF_ask_0 - FUTURE_ask_0

plt.subplot(2, 2, 1)
plt.plot(ETF_bid_0[2:], label='ETF Best bid')
plt.plot(ETF_ask_0[2:], label='ETF Best ask')
plt.legend()
plt.subplot(2, 2, 2)
plt.plot(FUTURE_bid_0[2:], label='FUTURE Best bid')
plt.plot(FUTURE_ask_0[2:], label='FUTURE Best ask')
plt.legend()
plt.subplot(2, 2, 3)
plt.plot(bid_diff[2:], label='ETF best bid minus FUTURE best bid')
plt.legend()
plt.subplot(2, 2, 4)
plt.plot(ask_diff[2:], label='ETF best ask minus FUTURE best ask')
plt.legend()
plt.show()