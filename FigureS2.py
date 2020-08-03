import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

from lib.parse_data import get_scores, parse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thresholds", action='store_true', help="whether to use ONS England data or not",
                    default=False)
args = parser.parse_args()

drugs = ['AZ', 'MOX', 'LOP_RIT', 'CQ', 'QUIN', 'HCQ', 'HCQ_AZ', 'HCQ_MOX', 'HAL', 'HCQ_HAL', 'QND']
drug_labels = ['azithromycin', 'moxifloxacin', 'lopinavir\n/ritonavir', 'chloroquine', 'quinine', \
'hydroxychloroquine', 'hydroxychloroquine\n/azithromycin', 'hydroxychloroquine\n/moxifloxacin', 'halofantrine', \
'hydroxychloroquine\n/halofantrine', 'quinidine']
labels = ['Low', 'Intermediate', '', '', '', 'High', '', '', '', '', '']

fig = plt.figure()
ax = fig.add_subplot(111)
for i, j in enumerate(drugs):

    risk_low, risk_median, risk_high = get_scores(j)

    if risk_median < 0.0581:
        colour = 'red'
    elif risk_median > 0.0671:
        colour = 'forestgreen'
    else:
        colour = 'dodgerblue'

    plt.errorbar(risk_median, len(drugs) - 1 - i, xerr=np.array([[risk_median - risk_low, risk_high - risk_median]]).T, fmt='ko', capsize=10, \
        mec=colour, mfc=colour, ecolor=colour, label=labels[i])

# get handles
handles, labels = ax.get_legend_handles_labels()
# remove the errorbars
handles = [h[0] for h in handles]
# use them in the legend
ax.legend(handles, labels)

plt.axvline(0.0581, color='red', linestyle='dashed')
plt.axvline(0.0671, color='forestgreen', linestyle='dashed')
plt.xlabel('Torsade metric score')
ax.set_xlim([-0.1, 0.1])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticklabels([drug_labels[10], drug_labels[9], drug_labels[8], drug_labels[7], drug_labels[6], drug_labels[5], drug_labels[4], drug_labels[3], \
    drug_labels[2], drug_labels[1], drug_labels[0]])
plt.grid(True)
plt.tight_layout()
plt.show()