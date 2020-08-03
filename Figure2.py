import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

from lib.parse_data import get_scores, parse, drug_dictionary

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thresholds", action='store_true', help="whether to use ONS England data or not",
                    default=False)
args = parser.parse_args()

drug_cmax = drug_dictionary()

c_az, ql_az, qm_az, qh_az = parse('AZ', interpolate=False)
c_cq, ql_cq, qm_cq, qh_cq = parse('CQ', interpolate=False)
c_hal, ql_hal, qm_hal, qh_hal = parse('HAL', interpolate=False)
c_hcq, ql_hcq, qm_hcq, qh_hcq = parse('HCQ', interpolate=False)
c_mox, ql_mox, qm_mox, qh_mox = parse('MOX', interpolate=False)
c_qnn, ql_qnn, qm_qnn, qh_qnn = parse('QUIN', interpolate=False)

c_haz, ql_haz, qm_haz, qh_haz = parse('HCQ_AZ', interpolate=False)
c_hhal, ql_hhal, qm_hhal, qh_hhal = parse('HCQ_HAL', interpolate=False)
c_hmox, ql_hmox, qm_hmox, qh_hmox = parse('HCQ_MOX', interpolate=False)
c_lrit, ql_lrit, qm_lrit, qh_lrit = parse('LOP_RIT', interpolate=False)

c_az = c_az / drug_cmax['AZ']
c_cq = c_cq / drug_cmax['CQ']
c_hal = c_hal / drug_cmax['HAL']
c_hcq = c_hcq / drug_cmax['HCQ']
c_mox = c_mox / drug_cmax['MOX']
c_qnn = c_qnn / drug_cmax['QUIN']

c_haz = c_haz / drug_cmax['HCQ_AZ']
c_hhal = c_hhal / drug_cmax['HCQ_HAL']
c_hmox = c_hmox / drug_cmax['HCQ_MOX']
c_lrit = c_lrit / drug_cmax['LOP_RIT']

drugs = ['AZ', 'MOX', 'LOP_RIT', 'CQ', 'QUIN', 'HCQ', 'HCQ_AZ', 'HCQ_MOX', 'HAL', 'HCQ_HAL']
drug_labels = ['azithromycin', 'moxifloxacin', 'lopinavir\n/ritonavir', 'chloroquine', 'quinine', 'hydroxychloroquine', \
'hydroxychloroquine\n/azithromycin', 'hydroxychloroquine\n/moxifloxacin', 'halofantrine', 'hydroxychloroquine\n/halofantrine']
labels = ['Low', 'Intermediate', '', '', '', 'High', '', '', '', '']

cmap = plt.get_cmap("tab10")

fig = plt.figure(figsize=(8, 6), constrained_layout=True)
grid = plt.GridSpec(2, 2, figure=fig)

ax = fig.add_subplot(grid[0, 0])
ax.text(-0.18, 1, 'A', transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax.set_xlim([1e-2, 1e1])
ax.set_ylim([0.01, 0.09])
plt.semilogx(c_az, qm_az, color=cmap(0), label='AZ')
ax.fill_between(c_az, ql_az, qh_az, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_cq, qm_cq, color=cmap(1), label='CQ')
ax.fill_between(c_cq, ql_cq, qh_cq, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hal, qm_hal, color=cmap(2), label='HAL')
ax.fill_between(c_hal, ql_hal, qh_hal, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.semilogx(c_lrit, qm_lrit, color=cmap(3), label='LOP/RIT')
ax.fill_between(c_lrit, ql_lrit, qh_lrit, facecolor=cmap(3), edgecolor=None, alpha=0.2)
plt.semilogx(c_mox, qm_mox, color=cmap(4), label='MOX')
ax.fill_between(c_mox, ql_mox, qh_mox, facecolor=cmap(4), edgecolor=None, alpha=0.2)
plt.semilogx(c_qnn, qm_qnn, color=cmap(5), label='QUIN')
ax.fill_between(c_qnn, ql_qnn, qh_qnn, facecolor=cmap(5), edgecolor=None, alpha=0.2)
ax.legend()
ax.set_ylabel( 'qNet (C/F)' )
ax.set_xticks([0.01, 0.1, 1, 4, 10])
ax.set_xticklabels([0.01, 0.1, 1, 4, 10])
plt.grid(True)

ax2 = fig.add_subplot(grid[1, 0])
ax2.text(-0.18, 1, 'B', transform=ax2.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax2.set_xlim([1e-2, 1e1])
ax2.set_ylim([-0.01, 0.075])
plt.semilogx(c_hcq, qm_hcq, color=cmap(0), label='HCQ')
ax2.fill_between(c_hcq, ql_hcq, qh_hcq, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_haz, qm_haz, color=cmap(1), label='HCQ/AZ')
ax2.fill_between(c_haz, ql_haz, qh_haz, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hhal, qm_hhal, color=cmap(2), label='HCQ/HAL')
ax2.fill_between(c_hhal, ql_hhal, qh_hhal, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.semilogx(c_hmox, qm_hmox, color=cmap(3), label='HCQ/MOX')
ax2.fill_between(c_hmox, ql_hmox, qh_hmox, facecolor=cmap(3), edgecolor=None, alpha=0.2)
ax2.legend()
ax2.set_xlabel( r'$\times$ free $C_{\rm{max}}$' )
ax2.set_ylabel( 'qNet (C/F)' )
ax2.set_xticks([0.01, 0.1, 1, 4, 10])
ax2.set_xticklabels([0.01, 0.1, 1, 4, 10])
plt.grid(True)

ax3 = fig.add_subplot(grid[:, 1])
ax3.text(-0.5, 1, 'C', transform=ax3.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')

for i, j in enumerate(drugs):

    risk_low, risk_median, risk_high = get_scores(j)

    if risk_median < 0.0581:
        colour = 'red'
    elif risk_median > 0.0671:
        colour = 'forestgreen'
    else:
        colour = 'dodgerblue'

    plt.errorbar(risk_median, len(drugs) - 1 - i, xerr=np.array([[risk_median - risk_low, risk_high - risk_median]]).T, fmt='ko', capsize=10, mec=colour, \
      mfc=colour, ecolor=colour, label=labels[i])

handles, labels = ax3.get_legend_handles_labels()
handles = [h[0] for h in handles]
ax3.legend(handles, labels)

plt.axvline(0.0581, color='red', linestyle='dashed')
plt.axvline(0.0671, color='forestgreen', linestyle='dashed')
ax3.set_xlabel('Torsade metric score')
ax3.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ax3.set_yticklabels([drug_labels[9], drug_labels[8], drug_labels[7], drug_labels[6], drug_labels[5], drug_labels[4], drug_labels[3], drug_labels[2], \
  drug_labels[1], drug_labels[0]])
plt.grid(True)

plt.show()
