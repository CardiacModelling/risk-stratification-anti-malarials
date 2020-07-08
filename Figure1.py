import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import Rectangle

from lib.parse_data import parse, parse_APD, drug_dictionary

drug_cmax = drug_dictionary()

c_hcq, al_hcq, am_hcq, ah_hcq = parse_APD('HCQ', MAXROWS=19, interpolate=False)
c_haz, al_haz, am_haz, ah_haz = parse_APD('HCQ_AZ', MAXROWS=19, interpolate=False)
c_hhal, al_hhal, am_hhal, ah_hhal = parse_APD('HCQ_HAL', MAXROWS=19, interpolate=False)
c_hmox, al_hmox, am_hmox, ah_hmox = parse_APD('HCQ_MOX', MAXROWS=19, interpolate=False)

c_az, al_az, am_az, ah_az = parse_APD('AZ', MAXROWS=19, interpolate=True)
c_cq, al_cq, am_cq, ah_cq = parse_APD('CQ', MAXROWS=19, interpolate=True)
c_hal, al_hal, am_hal, ah_hal = parse_APD('HAL', MAXROWS=19, interpolate=True)
c_mox, al_mox, am_mox, ah_mox = parse_APD('MOX', MAXROWS=19, interpolate=True)
c_lrit, al_lrit, am_lrit, ah_lrit = parse_APD('LOP_RIT', MAXROWS=19, interpolate=True)
c_qnn, al_qnn, am_qnn, ah_qnn = parse_APD('QUIN', MAXROWS=19, interpolate=True)

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

cont_ap = np.loadtxt('testoutput/HCQ/conc_0_voltage_trace.dat', skiprows=1, unpack=True)
t_cont = cont_ap[0] + 5
v_cont = cont_ap[1]
hcq_ap = np.loadtxt('testoutput/HCQ_supp/conc_' + str(drug_cmax['HCQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hcq = hcq_ap[0] + 5
v_hcq = hcq_ap[1]
hcq_ap2 = np.loadtxt('testoutput/HCQ_supp/conc_' + str(4 * drug_cmax['HCQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hcq2 = hcq_ap2[0] + 5
v_hcq2 = hcq_ap2[1]
az_ap = np.loadtxt('testoutput/AZ_supp/conc_' + str(drug_cmax['AZ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_az = az_ap[0] + 5
v_az = az_ap[1]
az_ap2 = np.loadtxt('testoutput/AZ_supp/conc_' + str(4 * drug_cmax['AZ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_az2 = az_ap2[0] + 5
v_az2 = az_ap2[1]
haz_ap = np.loadtxt('testoutput/HCQ_AZ_supp/conc_' + str(drug_cmax['HCQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_haz = haz_ap[0] + 5
v_haz = haz_ap[1]
haz_ap2 = np.loadtxt('testoutput/HCQ_AZ_supp/conc_' + str(4 * drug_cmax['HCQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_haz2 = haz_ap2[0] + 5
v_haz2 = haz_ap2[1]
hal_ap = np.loadtxt('testoutput/HAL_supp/conc_' + str(drug_cmax['HAL']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hal = hal_ap[0] + 5
v_hal = hal_ap[1]
hal_ap2 = np.loadtxt('testoutput/HAL_supp/conc_' + str(4 * drug_cmax['HAL']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hal2 = hal_ap2[0] + 5
v_hal2 = hal_ap2[1]
hhal_ap = np.loadtxt('testoutput/HCQ_HAL_supp/conc_' + str(drug_cmax['HCQ_HAL']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hhal = hhal_ap[0] + 5
v_hhal = hhal_ap[1]
hhal_ap2 = np.loadtxt('testoutput/HCQ_HAL_supp/conc_' + str(4 * drug_cmax['HCQ_HAL']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hhal2 = hhal_ap2[0] + 5
v_hhal2 = hhal_ap2[1]
mox_ap = np.loadtxt('testoutput/MOX_supp/conc_' + str(drug_cmax['MOX']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_mox = mox_ap[0] + 5
v_mox = mox_ap[1]
mox_ap2 = np.loadtxt('testoutput/MOX_supp/conc_' + str(4 * drug_cmax['MOX']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_mox2 = mox_ap2[0] + 5
v_mox2 = mox_ap2[1]
hmox_ap = np.loadtxt('testoutput/HCQ_MOX_supp/conc_' + str(drug_cmax['HCQ_MOX']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hmox = hmox_ap[0] + 5
v_hmox = hmox_ap[1]
hmox_ap2 = np.loadtxt('testoutput/HCQ_MOX_supp/conc_' + str(4 * drug_cmax['HCQ_MOX']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_hmox2 = hmox_ap2[0] + 5
v_hmox2 = hmox_ap2[1]
cq_ap = np.loadtxt('testoutput/CQ_supp/conc_' + str(drug_cmax['CQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_cq = cq_ap[0] + 5
v_cq = cq_ap[1]
cq_ap2 = np.loadtxt('testoutput/CQ_supp/conc_' + str(4 * drug_cmax['CQ']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_cq2 = cq_ap2[0] + 5
v_cq2 = cq_ap2[1]
lrit_ap = np.loadtxt('testoutput/LOP_RIT_supp/conc_' + str(drug_cmax['LOP_RIT']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_lrit = lrit_ap[0] + 5
v_lrit = lrit_ap[1]
lrit_ap2 = np.loadtxt('testoutput/LOP_RIT_supp/conc_' + str(4 * drug_cmax['LOP_RIT']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_lrit2 = lrit_ap2[0] + 5
v_lrit2 = lrit_ap2[1]
qnn_ap = np.loadtxt('testoutput/QUIN_supp/conc_' + str(drug_cmax['QUIN']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_qnn = qnn_ap[0] + 5
v_qnn = qnn_ap[1]
qnn_ap2 = np.loadtxt('testoutput/QUIN_supp/conc_' + str(4 * drug_cmax['QUIN']) + '_voltage_trace.dat', skiprows=1, unpack=True)
t_qnn2 = qnn_ap2[0] + 5
v_qnn2 = qnn_ap2[1]

cmap = plt.get_cmap("tab10")

fig = plt.figure(figsize=(11, 7.5), constrained_layout=True)
grid = plt.GridSpec(4, 3, figure=fig)

ax1 = plt.subplot(grid[0, 0])
ax1.text(-0.12, 1, 'Ai', transform=ax1.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([1e-1, 14])
axes.set_ylim([-10, 160])
plt.semilogx(c_az, am_az, color=cmap(0))
ax1.fill_between(c_az, al_az, ah_az, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_cq, am_cq, color=cmap(1))
ax1.fill_between(c_cq, al_cq, ah_cq, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hal, am_hal, color=cmap(2))
ax1.fill_between(c_hal, al_hal, ah_hal, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.semilogx(c_lrit, am_lrit, color=cmap(3))
ax1.fill_between(c_lrit, al_lrit, ah_lrit, facecolor=cmap(3), edgecolor=None, alpha=0.2)
plt.semilogx(c_mox, am_mox, color=cmap(4))
ax1.fill_between(c_mox, al_mox, ah_mox, facecolor=cmap(4), edgecolor=None, alpha=0.2)
plt.semilogx(c_qnn, am_qnn, color=cmap(5))
ax1.fill_between(c_qnn, al_qnn, ah_qnn, facecolor=cmap(5), edgecolor=None, alpha=0.2)
plt.axvline(1, color='red', linestyle='dashed')
plt.axvline(4, color='magenta', linestyle='dotted')
ax1.set_ylabel( r'$\Delta$APD (%)' )
ax1.set_xticks([0.1, 0.2, 0.5, 1, 2, 4, 10])
ax1.set_xticklabels([0.1, 0.2, 0.5, 1, 2, 4, 10])
plt.grid(True)

ax2 = plt.subplot(grid[0, 1])
ax2.text(-0.11, 1, 'Aii', transform=ax2.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver', label='Control')
plt.plot(t_az, v_az, color=cmap(0), label='AZ')
plt.plot(t_cq, v_cq, color=cmap(1), label='CQ')
plt.plot(t_hal, v_hal, color=cmap(2), label='HAL')
plt.plot(t_lrit, v_lrit, color=cmap(3), label='LOP/RIT')
plt.plot(t_mox, v_mox, color=cmap(4), label='MOX')
plt.plot(t_qnn, v_qnn, color=cmap(5), label='QUIN')
ax2.legend(fontsize=9, loc='upper right')
ax2.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
autoAxis = ax2.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='red', linestyle='dashed')
rec = ax2.add_patch(rec)
rec.set_clip_on(False)

ax3 = plt.subplot(grid[0, 2])
ax3.text(-0.11, 1, 'Aiii', transform=ax3.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver')
plt.plot(t_az2, v_az2, color=cmap(0))
plt.plot(t_cq2, v_cq2, color=cmap(1))
plt.plot(t_hal2, v_hal2, color=cmap(2))
plt.plot(t_lrit2, v_lrit2, color=cmap(3))
plt.plot(t_mox2, v_mox2, color=cmap(4))
plt.plot(t_qnn2, v_qnn2, color=cmap(5))
ax3.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
autoAxis = ax3.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='magenta', linestyle='dotted')
rec = ax3.add_patch(rec)
rec.set_clip_on(False)

ax4 = plt.subplot(grid[1, 0])
ax4.text(-0.12, 1, 'Bi', transform=ax4.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([1e-1, 14])
axes.set_ylim([-10, 210])
plt.semilogx(c_hcq, am_hcq, color=cmap(0))
ax4.fill_between(c_hcq, al_hcq, ah_hcq, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_az, am_az, color=cmap(1))
ax4.fill_between(c_az, al_az, ah_az, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_haz, am_haz, color=cmap(2))
ax4.fill_between(c_haz, al_haz, ah_haz, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.axvline(1, color='red', linestyle='dashed')
plt.axvline(4, color='magenta', linestyle='dotted')
ax4.set_ylabel( r'$\Delta$APD (%)' )
ax4.set_xticks([0.1, 0.2, 0.5, 1, 2, 4, 10])
ax4.set_xticklabels([0.1, 0.2, 0.5, 1, 2, 4, 10])
plt.grid(True)

ax5 = plt.subplot(grid[1, 1])
ax5.text(-0.12, 1, 'Bii', transform=ax5.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver', label='Control')
plt.plot(t_hcq, v_hcq, color=cmap(0), label='HCQ')
plt.plot(t_az, v_az, color=cmap(1), label='AZ')
plt.plot(t_haz, v_haz, color=cmap(2), label='HCQ/AZ')
ax5.legend(fontsize=9, loc='upper right')
ax5.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax5.spines['bottom'].set_visible(False)
ax5.spines['left'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
autoAxis = ax5.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='red', linestyle='dashed')
rec = ax5.add_patch(rec)
rec.set_clip_on(False)

ax6 = plt.subplot(grid[1, 2])
ax6.text(-0.11, 1, 'Biii', transform=ax6.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver')
plt.plot(t_hcq2, v_hcq2, color=cmap(0))
plt.plot(t_az2, v_az2, color=cmap(1))
plt.plot(t_haz2, v_haz2, color=cmap(2))
ax6.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax6.spines['bottom'].set_visible(False)
ax6.spines['left'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)
autoAxis = ax6.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='magenta', linestyle='dotted')
rec = ax6.add_patch(rec)
rec.set_clip_on(False)

ax7 = plt.subplot(grid[2, 0])
ax7.text(-0.12, 1, 'Ci', transform=ax7.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([1e-1, 14])
axes.set_ylim([-10, 310])
plt.semilogx(c_hcq, am_hcq, color=cmap(0))
ax7.fill_between(c_hcq, al_hcq, ah_hcq, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_hal, am_hal, color=cmap(1))
ax7.fill_between(c_hal, al_hal, ah_hal, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hhal, am_hhal, color=cmap(2))
ax7.fill_between(c_hhal, al_hhal, ah_hhal, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.axvline(1, color='red', linestyle='dashed')
plt.axvline(4, color='magenta', linestyle='dotted')
ax7.set_ylabel( r'$\Delta$APD (%)' )
ax7.set_xticks([0.1, 0.2, 0.5, 1, 2, 4, 10])
ax7.set_xticklabels([0.1, 0.2, 0.5, 1, 2, 4, 10])
plt.grid(True)

ax8 = plt.subplot(grid[2, 1])
ax8.text(-0.11, 1, 'Cii', transform=ax8.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver', label='Control')
plt.plot(t_hcq, v_hcq, color=cmap(0), label='HCQ')
plt.plot(t_hal, v_hal, color=cmap(1), label='HAL')
plt.plot(t_hhal, v_hhal, color=cmap(2), label='HCQ/HAL')
ax8.legend(fontsize=9, loc='upper right')
ax8.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax8.spines['bottom'].set_visible(False)
ax8.spines['left'].set_visible(False)
ax8.spines['right'].set_visible(False)
ax8.spines['top'].set_visible(False)
autoAxis = ax8.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='red', linestyle='dashed')
rec = ax8.add_patch(rec)
rec.set_clip_on(False)

ax9 = plt.subplot(grid[2, 2])
ax9.text(-0.11, 1, 'Ciii', transform=ax9.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver')
plt.plot(t_hcq2, v_hcq2, color=cmap(0))
plt.plot(t_hal2, v_hal2, color=cmap(1))
plt.plot(t_hhal2, v_hhal2, color=cmap(2))
ax9.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax9.spines['bottom'].set_visible(False)
ax9.spines['left'].set_visible(False)
ax9.spines['right'].set_visible(False)
ax9.spines['top'].set_visible(False)
autoAxis = ax9.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='magenta', linestyle='dotted')
rec = ax9.add_patch(rec)
rec.set_clip_on(False)

ax10 = plt.subplot(grid[3, 0])
ax10.text(-0.12, 1, 'Di', transform=ax10.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([1e-1, 14])
axes.set_ylim([-10, 270])
plt.semilogx(c_hcq, am_hcq, color=cmap(0))
ax10.fill_between(c_hcq, al_hcq, ah_hcq, facecolor=cmap(0), edgecolor=None, alpha=0.2)
plt.semilogx(c_mox, am_mox, color=cmap(1))
ax10.fill_between(c_mox, al_mox, ah_mox, facecolor=cmap(1), edgecolor=None, alpha=0.2)
plt.semilogx(c_hmox, am_hmox, color=cmap(2))
ax10.fill_between(c_hmox, al_hmox, ah_hmox, facecolor=cmap(2), edgecolor=None, alpha=0.2)
plt.axvline(1, color='red', linestyle='dashed')
plt.axvline(4, color='magenta', linestyle='dotted')
ax10.set_xlabel( r'$\times$ $C_{\rm{max}}$' )
ax10.set_ylabel( r'$\Delta$APD (%)' )
ax10.set_xticks([0.1, 0.2, 0.5, 1, 2, 4, 10])
ax10.set_xticklabels([0.1, 0.2, 0.5, 1, 2, 4, 10])
plt.grid(True)

ax11 = plt.subplot(grid[3, 1])
ax11.text(-0.11, 1, 'Dii', transform=ax11.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver', label='Control')
plt.plot(t_hcq, v_hcq, color=cmap(0), label='HCQ')
plt.plot(t_mox, v_mox, color=cmap(1), label='MOX')
plt.plot(t_hmox, v_hmox, color=cmap(2), label='HCQ/MOX')
ax11.legend(fontsize=9, loc='upper right')
ax11.set_xlabel( 'Time (ms)' )
ax11.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax11.spines['bottom'].set_visible(False)
ax11.spines['left'].set_visible(False)
ax11.spines['right'].set_visible(False)
ax11.spines['top'].set_visible(False)
autoAxis = ax11.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='red', linestyle='dashed')
rec = ax11.add_patch(rec)
rec.set_clip_on(False)

ax12 = plt.subplot(grid[3, 2])
ax12.text(-0.11, 1, 'Diii', transform=ax12.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
axes = plt.gca()
axes.set_xlim([-5, 805])
plt.plot(t_cont, v_cont, color='silver')
plt.plot(t_hcq2, v_hcq2, color=cmap(0))
plt.plot(t_mox2, v_mox2, color=cmap(1))
plt.plot(t_hmox2, v_hmox2, color=cmap(2))
ax12.set_xlabel( 'Time (ms)' )
ax12.set_ylabel( 'Voltage (mV)' )
plt.grid(True)

ax12.spines['bottom'].set_visible(False)
ax12.spines['left'].set_visible(False)
ax12.spines['right'].set_visible(False)
ax12.spines['top'].set_visible(False)
autoAxis = ax12.axis()
rec = Rectangle((autoAxis[0]-0.7,autoAxis[2]-0.2),(autoAxis[1]-autoAxis[0])+1,(autoAxis[3]-autoAxis[2])+0.4, fill=False, lw=1.5, color='magenta', linestyle='dotted')
rec = ax12.add_patch(rec)
rec.set_clip_on(False)

plt.show()
