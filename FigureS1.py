import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

from parse_data import get_scores, parse, drug_dictionary

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thresholds", action='store_true', help="whether to use ONS England data or not",
                    default=False)
args = parser.parse_args()

drug_cmax = drug_dictionary()

c_cq, ql_cq, qm_cq, qh_cq = parse('CQ', interpolate=False)
c_h_cq, ql_h_cq, qm_h_cq, qh_h_cq = parse('CQ', interpolate=False)

c_hcq, ql_hcq, qm_hcq, qh_hcq = parse('HCQ', interpolate=False)
c_lhcq, ql_lhcq, qm_lhcq, qh_lhcq = parse('HCQ', interpolate=False)
c_hhcq, ql_hhcq, qm_hhcq, qh_hhcq = parse('HCQ', interpolate=False)

c_cq = c_cq / drug_cmax['CQ']
c_h_cq = c_h_cq / drug_cmax['CQ_HIGH']

c_hcq = c_hcq / drug_cmax['HCQ']
c_lhcq = c_lhcq / drug_cmax['HCQ_LOW']
c_hhcq = c_hhcq / drug_cmax['HCQ_HIGH']

drugs_cq = ['CQ', 'CQ_HIGH', 'HCQ']
drug_labels_cq = ['chloroquine', 'chloroquine\n(high dose)', 'hydroxychloroquine']
labels_cq = ['Intermediate', 'High', '']

drugs_hcq = ['HCQ_LOW', 'HCQ', 'HCQ_HIGH']
drug_labels_hcq = ['hydroxychloroquine\n(low dose)', 'hydroxychloroquine', 'hydroxychloroquine\n(high dose)']
labels_hcq = ['Intermediate', 'High', '']

cmap = plt.get_cmap("tab10")

fig = plt.figure(figsize=(8, 6), constrained_layout=True)
grid = plt.GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(grid[0, 0])
ax1.text(-0.16, 0.95, 'A', transform=ax1.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax1.set_xlim([1e-2, 1e1])
ax1.set_ylim([-0.01, 0.075])
plt.semilogx(c_cq, qm_cq, color=cmap(0), label='CQ')
ax1.fill_between(c_cq, ql_cq, qh_cq, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_h_cq, qm_h_cq, color=cmap(1), label='CQ-high')
ax1.fill_between(c_h_cq, ql_h_cq, qh_h_cq, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hcq, qm_hcq, color=cmap(2), label='HCQ')
ax1.fill_between(c_hcq, ql_hcq, qh_hcq, facecolor=cmap(2), edgecolor=None, alpha=0.2)
ax1.legend()
ax1.set_ylabel( 'qNet (C/F)' )
ax1.set_xticks([0.01, 0.1, 1, 4, 10])
ax1.set_xticklabels([0.01, 0.1, 1, 4, 10])
plt.grid(True)

ax2 = fig.add_subplot(grid[1, 0])
ax2.text(-0.16, 0.95, 'C', transform=ax2.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax2.set_xlim([1e-2, 1e1])
ax2.set_ylim([-0.01, 0.075])
plt.semilogx(c_lhcq, qm_lhcq, color=cmap(4), label='HCQ-low')
ax2.fill_between(c_lhcq, ql_lhcq, qh_lhcq, facecolor=cmap(4), edgecolor=None, alpha=0.2)
plt.semilogx(c_hcq, qm_hcq, color=cmap(2), label='HCQ')
ax2.fill_between(c_hcq, ql_hcq, qh_hcq, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.semilogx(c_hhcq, qm_hhcq, color=cmap(3), label='HCQ-high')
ax2.fill_between(c_hhcq, ql_hhcq, qh_hhcq, facecolor=cmap(3), edgecolor=None, alpha=0.2)
ax2.legend()
ax2.set_xlabel( r'$\times$ $C_{\rm{max}}$' )
ax2.set_ylabel( 'qNet (C/F)' )
ax2.set_xticks([0.01, 0.1, 1, 4, 10])
ax2.set_xticklabels([0.01, 0.1, 1, 4, 10])
plt.grid(True)

ax3 = fig.add_subplot(grid[0, 1])
ax3.text(-0.5, 0.95, 'B', transform=ax3.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')

for i, j in enumerate(drugs_cq):

    risk_low, risk_median, risk_high = get_scores(j)

    if risk_median < 0.0581:
        colour = 'red'
    elif risk_median > 0.0671:
        colour = 'forestgreen'
    else:
        colour = 'dodgerblue'

    plt.errorbar(risk_median, len(drugs_cq) - 1 - i, xerr=np.array([[risk_median - risk_low, risk_high - risk_median]]).T, fmt='ko', capsize=10, mec=colour, mfc=colour, ecolor=colour, label=labels_cq[i])

# get handles
handles, labels = ax3.get_legend_handles_labels()
# remove the errorbars
handles = [h[0] for h in handles]
# use them in the legend
ax3.legend(handles, labels)

ax3.set_xlim([0.01, 0.07])
plt.axvline(0.0581, color='red', linestyle='dashed')
plt.axvline(0.0671, color='forestgreen', linestyle='dashed')
ax3.set_yticks([0, 1, 2])
ax3.set_yticklabels([drug_labels_cq[2], drug_labels_cq[1], drug_labels_cq[0]])
plt.grid(True)

ax4 = fig.add_subplot(grid[1, 1])
ax4.text(-0.5, 0.95, 'D', transform=ax4.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')

for i, j in enumerate(drugs_hcq):

    risk_low, risk_median, risk_high = get_scores(j)

    if risk_median < 0.0581:
        colour = 'red'
    elif risk_median > 0.0671:
        colour = 'forestgreen'
    else:
        colour = 'dodgerblue'

    plt.errorbar(risk_median, len(drugs_hcq) - 1 - i, xerr=np.array([[risk_median - risk_low, risk_high - risk_median]]).T, fmt='ko', capsize=10, mec=colour, mfc=colour, ecolor=colour, label=labels_hcq[i])

# get handles
handles, labels = ax4.get_legend_handles_labels()
# remove the errorbars
handles = [h[0] for h in handles]
# use them in the legend
ax4.legend(handles, labels)

ax4.set_xlim([0.01, 0.07])
plt.axvline(0.0581, color='red', linestyle='dashed')
plt.axvline(0.0671, color='forestgreen', linestyle='dashed')
ax4.set_xlabel('Torsade metric score')
ax4.set_yticks([0, 1, 2])
ax4.set_yticklabels([drug_labels_hcq[2], drug_labels_hcq[1], drug_labels_hcq[0]])
plt.grid(True)

plt.show()