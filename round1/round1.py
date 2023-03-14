import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def show_team_pnl(scoreboardfile):
    team_numbers = 8
    match_id = scoreboardfile.split('_')[0]
    score_board = pd.read_csv(scoreboardfile)
    team = score_board['Team'][:team_numbers].values
    pnl = dict()
    for name in team:
        pnl[name] = list()

    for i in range(len(score_board['Time'])):
        row = score_board.iloc[i]
        pnl[row['Team']].append(row['ProfitOrLoss'])

    for name in team:
        plt.plot(pnl[name], label=name)
    plt.title(match_id)
    plt.legend()
    plt.show()


def show_price(logfile):
    TP = list()
    SEQ = list()
    with open(logfile) as f:
        for line in f.readlines():
            words = line.split(' ')
            if 'SMA' in words:
                idx_TP = words.index('TP') + 1
                idx_SEQ = words.index('sequence') + 2
                TP.append(float(words[idx_TP]))
                SEQ.append(int(words[idx_SEQ]))
    TP = np.array(TP)
    m = 25
    UUB = list()
    UB = list()
    LB = list()
    LLB = list()
    for n in SEQ:
        if n > m:
            sma = np.mean(TP[n-m-1:n])
            uub = sma + 1.97*np.std(TP[n-m-1:n])
            ub = sma + 1.5*np.std(TP[n-m-1:n])
            lb = sma - 1.5*np.std(TP[n-m-1:n])
            llb = sma - 1.97 * np.std(TP[n - m - 1:n])
            UUB.append(uub)
            UB.append(ub)
            LB.append(lb)
            LLB.append(llb)
        else:
            sma = TP[n - 1]
            uub = sma + 1.97 * np.std(TP)
            ub = sma + 1.5 * np.std(TP)
            mb = TP[n-1]
            lb = sma - 1.5 * np.std(TP)
            llb = sma - 1.97 * np.std(TP)
            UUB.append(uub)
            UB.append(ub)
            LB.append(lb)
            LLB.append(llb)

    plt.plot(TP, label='Typical Price')
    plt.plot(UB, label='Upper bound')
    plt.plot(UUB, label='UUpper bound')
    plt.plot(LB, label='Lower bound')
    plt.plot(LLB, label='LLower bound')
    plt.title('Price for {0}'.format(logfile.split('_')[0]))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # UUB, UB, TP, LB, LLB 플롯해줌.
    show_price('match160_Cocrew_801.log')
