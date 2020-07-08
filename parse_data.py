import numpy as np
from scipy.interpolate import interp1d

def parse(file_str, truncate=True, interpolate=False):

    filename = 'testoutput/' + file_str + '/'

    data = ""
    with open(filename + 'q_net.txt', 'r') as file:
        data = file.read().replace(',', '   ')

    with open(filename + 'q_net_new.dat', "w") as out_file:
        out_file.write(data)

    conc_qnet = np.loadtxt(filename + 'q_net_new.dat', skiprows=1, unpack=True)

    if truncate:
        conc_qnet = conc_qnet.T

        fac = 0
        for j in range(len(conc_qnet)):
            counter = 0
            deleted = False
            k = j - fac
            for i in conc_qnet[k]:
                if i < -1000:
                    counter += 1
                if counter > 1 and deleted == False:
                    conc_qnet = np.delete(conc_qnet, (k), axis=0)
                    deleted = True
                    fac += 1

        conc_qnet = conc_qnet.T

    conc = conc_qnet[0]
    qnet_low = conc_qnet[2]
    qnet_median = conc_qnet[6]
    qnet_high = conc_qnet[10]

    if interpolate:
        conc = np.log10(conc[1:])
        qnet_low = qnet_low[1:]
        qnet_median = qnet_median[1:]
        qnet_high = qnet_high[1:]

        f_low = interp1d(conc, qnet_low, kind='cubic')
        f_median = interp1d(conc, qnet_median, kind='cubic')
        f_high = interp1d(conc, qnet_high, kind='cubic')
        x = np.linspace(np.min(conc), np.max(conc), 1000)

        debug = False
        if debug:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = plt.gca()
            plt.scatter(conc, qnet_low, color='dodgerblue', alpha=0.5)
            plt.plot(x, f_low(x), color='dodgerblue', alpha=0.5)
            plt.scatter(conc, qnet_median, color='dodgerblue')
            plt.plot(x, f_median(x), color='dodgerblue')
            plt.scatter(conc, qnet_high, color='dodgerblue', alpha=0.5)
            plt.plot(x, f_high(x), color='dodgerblue', alpha=0.5)
            plt.grid(True)
            plt.show()

        qnet_low = f_low(x)
        qnet_median = f_median(x)
        qnet_high = f_high(x)
        conc = np.power(10, x)

    return conc, qnet_low, qnet_median, qnet_high

def parse_APD(file_str, MAXROWS=20, interpolate=False):

    filename = 'testoutput/' + file_str + '/'

    data = ""
    with open(filename + 'voltage_results.dat', 'r') as file:
        data = file.read().replace(',', '   ')

    with open(filename + 'voltage_results_new.dat', "w") as out_file:
        out_file.write(data)

    conc_apd = np.loadtxt(filename + 'voltage_results_new.dat', skiprows=1, max_rows=MAXROWS, unpack=True)

    conc = conc_apd[0]
    apd_low = conc_apd[8]
    apd_median = conc_apd[11]
    apd_high = conc_apd[14]

    if interpolate:
        conc = np.log10(conc[1:])
        apd_low = apd_low[1:]
        apd_median = apd_median[1:]
        apd_high = apd_high[1:]

        f_low = interp1d(conc, apd_low, kind='cubic')
        f_median = interp1d(conc, apd_median, kind='cubic')
        f_high = interp1d(conc, apd_high, kind='cubic')
        x = np.linspace(np.min(conc), np.max(conc), 1000)

        debug = False
        if debug:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = plt.gca()
            plt.scatter(conc, apd_low, color='dodgerblue', alpha=0.5)
            plt.plot(x, f_low(x), color='dodgerblue', alpha=0.5)
            plt.scatter(conc, apd_median, color='dodgerblue')
            plt.plot(x, f_median(x), color='dodgerblue')
            plt.scatter(conc, apd_high, color='dodgerblue', alpha=0.5)
            plt.plot(x, f_high(x), color='dodgerblue', alpha=0.5)
            plt.grid(True)
            plt.show()

        apd_low = f_low(x)
        apd_median = f_median(x)
        apd_high = f_high(x)
        conc = np.power(10, x)

    return conc, apd_low, apd_median, apd_high

def get_scores(drug_str):

    drug_str_real = drug_str
    if drug_str in {'HCQ_LOW', 'HCQ_HIGH'}:
        drug_str = 'HCQ'
    if drug_str in {'CQ_HIGH'}:
        drug_str = 'CQ'
    conc, qnet_low, qnet_median, qnet_high = parse(drug_str, truncate=True)

    conc = np.log10(conc[1:])
    qnet_low = qnet_low[1:]
    qnet_median = qnet_median[1:]
    qnet_high = qnet_high[1:]

    f_low = interp1d(conc, qnet_low, kind='cubic')
    f_median = interp1d(conc, qnet_median, kind='cubic')
    f_high = interp1d(conc, qnet_high, kind='cubic')
    x = np.linspace(np.min(conc), np.max(conc), 1000)

    debug = False
    if debug:
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = plt.gca()
        plt.scatter(conc, qnet_low, color='dodgerblue', alpha=0.5)
        plt.plot(x, f_low(x), color='dodgerblue', alpha=0.5)
        plt.scatter(conc, qnet_median, color='dodgerblue')
        plt.plot(x, f_median(x), color='dodgerblue')
        plt.scatter(conc, qnet_high, color='dodgerblue', alpha=0.5)
        plt.plot(x, f_high(x), color='dodgerblue', alpha=0.5)
        plt.grid(True)
        plt.show()

    drug_cmax = drug_dictionary()
    cmax = drug_cmax[drug_str_real]

    risk_l, risk_m, risk_h = 0, 0, 0

    for k in range(4):
        risk_l += f_low(np.log10(cmax * (k + 1)))
        risk_m += f_median(np.log10(cmax * (k + 1)))
        risk_h += f_high(np.log10(cmax * (k + 1)))

    risk_l = risk_l / 4
    risk_m = risk_m / 4
    risk_h = risk_h / 4

    return risk_l, risk_m, risk_h

def drug_dictionary():

    drug_cmax = {'AZ': 1.937, 'CQ': 0.66, 'CQ_HIGH': 1.32, 'HAL': 0.57, 'HCQ': 1.22, 'HCQ_LOW': 0.61, 'HCQ_HIGH': 2.44, 'MOX': 4.111, 'QUIN': 3.9567, 'HCQ_AZ': 1.22 , 'HCQ_HAL': 1.22, 'HCQ_MOX': 1.22, 'LOP_RIT': 0.704}
    
    return drug_cmax
