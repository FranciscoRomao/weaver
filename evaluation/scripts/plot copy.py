from qiskit.transpiler.passes import SabreLayout
from qiskit import QuantumCircuit
from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
from qiskit.providers.fake_provider import FakeWashington
from evaluation.utils.plot.util import grouped_bar_plot, plot_line, stacked_grouped_bar_plot
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick


def plot(config):
    plot_property = config['plot_property']
    
    #backend = FakeWashington()

    data_atomique = pd.read_csv(config['atomique_input'])
    data_geyser = pd.read_csv(config['geyser_input'])
    data_superconducting = pd.read_csv(config['superconducting_input'])
    data_weaver = pd.read_csv(config['weaver_input'])
    data_dpqa = pd.read_csv(config['dpqa_input'])
    output_file = config['output_file']
    n_variables = config['n_variables']

    if not isinstance(n_variables, list):
        n_variables = [n_variables]

    if plot_property == 'compilation_time':
        
        data = []
        fig, ax = plt.subplots(1,2, figsize=(20, 4.5))

        # (a) Compilation time for fixed number of variables (20 variables)
        
        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].to_list()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
        
        geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
        
        superconducting_execution_time = data_superconducting[data_superconducting['n_variables']==var]['runtime'].to_list()
        superconducting_execution_time_mean = data_superconducting[data_superconducting['n_variables']==var]['runtime'].mean()

        weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].to_list()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()

        #dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        least_improv = atomique_execution_time_mean/weaver_execution_time_mean

        best_improv = dpqa_execution_time_mean/weaver_execution_time_mean

        mean_improv = (atomique_execution_time_mean*dpqa_execution_time_mean*geyser_execution_time_mean*superconducting_execution_time_mean)**(1/3) / weaver_execution_time_mean

        print("Improvements: ", least_improv, best_improv, mean_improv)

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
        #if superconducting_fidelity < 1e-20:
        #    superconducting_fidelity = 0

        #if atomique_fidelity < 1e-20:
        #    atomique_fidelity = 0

        data = np.array(data)

        grouped_bar_plot(ax[0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        ax[0].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[0].text(
            8.5,
            60000,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[0].set_yscale('log')

        ax[0].set_ylabel('Compilation time [seconds]')

        ax[0].set_title('(a) Compilation time - Fixed size circuit', fontweight='bold', loc='left')

        spacing = 0.95

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[0].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.43, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Compilation time', fontweight='bold')

        #plt.xlim(-0.3, 5.85)

        # Compilation time variable 

        data = []

        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['runtime']).mean()
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()
            #avg_improv *= atomique_execution_time/weaver_execution_time
            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])
        
        data = np.array(data)

        #print(avg_improv**(1/len(n_variables)))

        #fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax[1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        ax[1].set_yscale('log')

        ax[1].set_title('(b) Compilation time - Variable size circuit', fontweight='bold', loc='left')

        #ax[0][1].set_ylabel('Compilation time [seconds]')

        #ax[0].set_title('Compilation time', fontweight='bold')

        num_groups, num_bars = data.shape

        spacing = 0.95

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        ax[1].set_xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax[1].text(
            4.5,
            10**4.5,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1].set_xlabel('Number of variables')

        ax[0].set_xlabel('MAX-3SAT Benchmark Suite')

        ax[0].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)
        #plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.2))
        ax[1].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)

        plt.subplots_adjust(bottom=0.22)

        plt.tight_layout()

        plt.savefig(output_file)
    
    if plot_property == 'execution_time':

        # Execution time fixed 20 variables

        fig, ax = plt.subplots(1,2, figsize=(20, 4.5))

        spacing = 0.95

        least_improv = 1
        best_improv = 1
        mean_improv = 1

        data = []

        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].tolist()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()
        
        geyser_execution_time = (data_geyser[data_geyser['n_variables']==var]['execution_time'] / 1e6).to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
        
        superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).tolist()
        superconducting_execution_time_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()
        
        weaver_execution_time = (data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'] / 1e6).tolist()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        best_improv *= atomique_execution_time_mean/weaver_execution_time_mean

        least_improv *= geyser_execution_time_mean/weaver_execution_time_mean

        mean_improv *= np.mean([atomique_execution_time_mean, dpqa_execution_time_mean, superconducting_execution_time_mean, geyser_execution_time_mean])/weaver_execution_time_mean

        print("Improvements: ", least_improv, best_improv, mean_improv)

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']

        data = np.array(data)

        grouped_bar_plot(ax[0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[0].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-3.64, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax[0].set_ylabel('Execution time [seconds]')

        ax[0].set_title('(a) Execution time - Fixed size', fontweight='bold', loc='left')

        ax[0].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[0].text(
            8.5,
            0.225,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[0].set_yscale('log')

        # Execution time variable

        data = []
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()# * 1e6
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()# * 1e6
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])

        data = np.array(data)

        num_groups, num_bars = data.shape

        grouped_bar_plot(ax[1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        ax[1].text(
            4.5,
            4,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1].set_title('(b) Execution time - Variable size', fontweight='bold', loc='left')

        ax[1].set_yscale('log')

        ax[1].set_xlabel('Number of variables')

        ax[0].set_xlabel('MAX-3SAT Benchmark Suite')

        ax[1].set_xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-3.65, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax[0].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)

        ax[1].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)

        plt.subplots_adjust(bottom=0.22)

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'fidelity':
        # Estimated probability of success fixed 20 variables

        data = []
        fig, ax = plt.subplots(1,2, figsize=(20, 4.5))
        spacing = 0.95

        var = 20

        atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].to_list()
        atomique_fidelity_mean = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()

        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).tolist()
        superconducting_fidelity_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
        
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].tolist()
        dpqa_fidelity_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].to_list()
        weaver_fidelity_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()

        #dpqa_fidelity = [dpqa_fidelity[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        geyser_fidelity = [np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
        geyser_fidelity_mean = np.NAN

        least_improv = atomique_fidelity_mean/weaver_fidelity_mean

        best_improv = dpqa_fidelity_mean/weaver_fidelity_mean

        mean_improv = (atomique_fidelity_mean*dpqa_fidelity_mean)**(1/2) /weaver_fidelity_mean

        print("Improvements: ", least_improv, best_improv, mean_improv)

        data = [[atomique_fidelity[i], weaver_fidelity[i], dpqa_fidelity[i], geyser_fidelity[i]] for i in range(len(atomique_fidelity))]
        
        data.append([atomique_fidelity_mean, weaver_fidelity_mean, dpqa_fidelity_mean, geyser_fidelity_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        grouped_bar_plot(ax[0], data, bar_labels=['Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks], colors= sns.color_palette("pastel")[1:])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[0].set_title('(a) EPS - Fixed size circuit (20 variables)', fontweight='bold', loc='left')

        ax[0].set_yscale('log')

        ax[0].set_ylim(10**-2.29, 10**-1)

        ax[0].axvline(9.8, color='grey', linestyle='dashed', linewidth=2)

        ax[0].text(
            9.5,
            0.105,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        for nan_n in range(4):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[0].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-2.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        # Estimated probability of success variable

        avg_improv = 1
        data = []

        for var in n_variables:
            atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()
            superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
            dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()
            avg_improv *= atomique_fidelity/weaver_fidelity
            #superconducting_fidelity = [np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
            superconducting_fidelity = np.NAN
            print(var, data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean())
            geyser_fidelity = np.NAN

            if var == 250:
                atomique_fidelity = np.NAN

            data.append([superconducting_fidelity, atomique_fidelity, weaver_fidelity, dpqa_fidelity, geyser_fidelity])
        
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
            #         
        data = np.array(data)

        num_groups, num_bars = data.shape

        print(avg_improv**(1/len(n_variables)))

        grouped_bar_plot(ax[1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        for nan_n in range(5):
            if nan_n == 0:
                continue
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    if nan_n == 4 and j == 0 or nan_n == 4 and j == 1 or nan_n == 4 and j == 2:
                        ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.12, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')    
                        continue
                    if nan_n == 3:
                        ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.1, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')
                        continue
                    if nan_n == 1 and j == 5:
                        #ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.12, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')
                        continue
                        
                    #ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.12, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')
                    ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.12, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax[1].text((1+5*num_groups)//num_groups+1*bar_width-0.12, 10**-53.2, "", ha='center', va='bottom', fontsize=11, fontweight='bold')
        ax[1].text((1+5*num_groups)//num_groups+1*bar_width-0.08, 10**-3, "10⁻⁵¹", ha='center', va='bottom', fontsize=11, fontweight='bold', color=sns.color_palette("pastel")[1])
        ax[1].vlines((1+5*num_groups)//num_groups+1*bar_width-0.08, 10**-41, 10**-4, color=sns.color_palette("pastel")[1], linewidth=2, linestyle='dashed')

        #for j in range(num_groups):
        #        if np.isnan(data[j][0]):
        #            ax[1].text((j*num_groups)//num_groups, 10**-53.2, "12", ha='center', va='bottom', fontsize=10, fontweight='bold')

        ax[1].text(0-0.04, 10**-3, "10⁻⁸", ha='center', va='bottom', fontsize=11, fontweight='bold', color=sns.color_palette("pastel")[0])
        ax[1].vlines(-0.08, 10**-41, 10**-4, color=sns.color_palette("pastel")[0], linewidth=2, linestyle='dashed')
        
        ax[1].text(1-0.06, 10**-3, "10⁻⁵⁶", ha='center', va='bottom', fontsize=11, fontweight='bold', color=sns.color_palette("pastel")[0])
        ax[1].vlines(0.86, 10**-41, 10**-4, color=sns.color_palette("pastel")[0], linewidth=2, linestyle='dashed')
        
        ax[1].text((2*num_groups)//num_groups-0.07, 10**-3, "10⁻¹¹¹", ha='center', va='bottom', fontsize=11, fontweight='bold', color=sns.color_palette("pastel")[0])
        ax[1].vlines(1.83, 10**-41, 10**-4, color=sns.color_palette("pastel")[0], linewidth=2, linestyle='dashed')

        ax[1].text((3*num_groups)//num_groups-0.07, 10**-3, "10⁻¹⁷⁸", ha='center', va='bottom', fontsize=11, fontweight='bold', color=sns.color_palette("pastel")[0])
        ax[1].vlines(2.86, 10**-41, 10**-4, color=sns.color_palette("pastel")[0], linewidth=2, linestyle='dashed')

        #ax[1].bar(-0.08, 10**-1.3, width=0.02, color=sns.color_palette("pastel")[0])

        ax[1].text((4*num_groups)//num_groups, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')
        ax[1].text((5*num_groups)//num_groups-0.05, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax[1].set_ylim(10**-41.3, 5)

        #ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width-0.12, 10**-41.3, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[0].set_ylabel('Estimated probability of success')

        ax[1].text(
            5,
            10**2,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1].set_title('(b) EPS - Variable size circuit', fontweight='bold', loc='left')

        ax[1].set_xlabel('Number of variables')

        ax[0].set_xlabel('MAX-3SAT Benchmark Suite')

        ax[1].set_yscale('log')

        plt.xlim(-0.3, 5.9)
        
        #plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        ax[0].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)
        ax[1].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.285), fontsize=13)

        plt.tight_layout()

        plt.subplots_adjust(bottom=0.21)

        plt.savefig(output_file)

    if plot_property == 'analysis_plots':
        
        data = []

        fig, ax = plt.subplots(1, 3, figsize=(14, 4))

        n_qubits = range(20,200)

        superconducting_complexity = [n_qubits[i]**3 for i in range(len(n_qubits))]

        weaver_complexity = [n_qubits[i]**2 for i in range(len(n_qubits))]

        atomique_complexity = [n_qubits[i]**2.8 for i in range(len(n_qubits))]

        geyser_complexity = [5789.6487*n_qubits[i]**2 - 87825.2997*n_qubits[i] - 103601.8515 for i in range(len(n_qubits))]

        dpqa_complexity = [2**n_qubits[i] for i in range(len(n_qubits))]
        
        df = pd.DataFrame({'n_qubits': list(n_qubits),
                           'Superconducting': superconducting_complexity,
                           'Weaver': weaver_complexity,
                           'Geyser': geyser_complexity,
                           'Atomique': atomique_complexity,
                           'DPQA': dpqa_complexity})
        
        df_melted = df.melt('n_qubits', var_name='complexity_type', value_name='complexity')

        sns.set_theme()
        sns.set_style("whitegrid")
        ax[0].set_yscale('log')

        sns.lineplot(ax=ax[0], x='n_qubits', y='complexity', hue='complexity_type', data=df_melted, linewidth=2)

        ax[0].set_ylim(1e2, 1e20)

        ax[0].legend().set_title('')
        ax[0].legend().set_bbox_to_anchor((0.45, 0.45))

        ax[0].text(105, 10**20.1, "Lower is better ↓", ha='center', va='bottom', fontsize=14, fontweight='bold', color='midnightblue')

        ax[0].text(190, 10**18.5, "10⁶⁰", ha='center', va='bottom', fontsize=14, fontweight='bold', color=sns.color_palette()[4])

        ax[0].text(150, 10**18.5, "10⁴⁵", ha='center', va='bottom', fontsize=14, fontweight='bold', color=sns.color_palette()[4])

        ax[0].set_title('(a) Complexity Comparison', fontweight='bold', pad=20)

        ax[0].set_xlabel('Number of variables')
        ax[0].set_ylabel('Complexity [Number of steps]')

        FONTSIZE = 12

        #--------------------------------------------------------------------

        data = []

        for var in n_variables:
            weaver_gates1q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#u3'].mean()
            weaver_gates2q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#cz'].mean()
            weaver_gates3q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#ccz'].mean()

            dpqa_gates1q = data_dpqa[data_dpqa['n_variables']==var]['1q_gates'].mean()
            dpqa_gates2q = data_dpqa[data_dpqa['n_variables']==var]['2q_gates'].mean() 

            atomique_gates1q = data_atomique[data_atomique['n_variables']==var]['n_1q_gate'].mean()
            atomique_gates2q = data_atomique[data_atomique['n_variables']==var]['n_2q_gate'].mean()
    
            geyser_pulses = data_geyser[data_geyser['n_variables']==var]['n_pulses'].mean()

            weaver_pulses = weaver_gates1q + weaver_gates2q*3 + weaver_gates3q*5

            atomique_pulses = atomique_gates1q + atomique_gates2q*3

            print(atomique_pulses, weaver_pulses, atomique_pulses/weaver_pulses)

            dpqa_pulses = dpqa_gates1q + dpqa_gates2q*3

            data.append([atomique_pulses, weaver_pulses, geyser_pulses, dpqa_pulses])

        data = np.array(data)

        grouped_bar_plot(ax[1], data, bar_labels=['Atomique', 'Weaver', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        spacing = 0.95

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        ax[1].set_yscale('log')

        for nan_n in range(4):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**2.81, "X", ha='center', va='bottom', fontsize=9, fontweight='bold')

        ax[1].set_title('(b) Number of pulses', fontweight='bold', pad=20)

        ax[1].set_xlim(-0.3, 5.85)

        ax[1].set_ylabel('Number of pulses')

        ax[1].set_xlabel('Number of variables')

        ax[1].legend(loc="upper left", ncol=1)

        #--------------------------------------------------------------------
    
        data = []

        fids = [0.9775, 0.98, 0.9825, 0.985, 0.9875, 0.99, 0.9925, 0.995, 0.9975]

        for var in fids:
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==var][data_weaver['num_variables']==n_variables[0]]['eps (fidelity)'].mean()
            data.append(weaver_fidelity)

        atomique_fidelity = data_atomique[data_atomique['n_variables']==n_variables[0]]['total_fidelity'].mean()
        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==n_variables[0]]['eps']).mean()
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==n_variables[0]]['eps'].mean()

        data = [[data[i],fids[i]] for i in range(len(fids))]
        
        data = pd.DataFrame(data, columns=['ccz_fidelity', 'eps'])

        sns.set_theme()
        sns.set_style("whitegrid")

        sns.lineplot(ax=ax[2], data=data, x='eps', y='ccz_fidelity', label='Weaver', markers='o', linewidth=2, legend=False)

        ax[2].set_ylabel('Estimated probability of success (eps)')

        ax[2].set_title('(c) CCZ fidelty threshold', fontweight='bold', pad=20)

        ax[2].set_xlabel('CCZ Gate fidelity')

        #higher is better
        ax[2].text(0.988, 0.127, "Higher is better ↑", ha='center', va='bottom', fontsize=14, fontweight='bold', color='midnightblue')

        ax[2].text(0.9916, dpqa_fidelity-0.006, "X", ha='center', va='bottom', fontsize=18, fontweight='bold', color='r')
        ax[2].hlines(atomique_fidelity, label='Atomique', colors='r', linestyles='dashed', xmin=0.9775, xmax=0.9975, linewidth=2)
        ax[2].hlines(superconducting_fidelity, label='Superconducting', colors='g', linestyles='dashdot', xmin=0.9775, xmax=0.9975, linewidth=2)
        ax[2].hlines(dpqa_fidelity, label='DPQA', colors='b', linestyles='dotted', xmin=0.9775, xmax=0.9975, linewidth=2)

        ax[2].text(0.985, dpqa_fidelity+0.001, "CCZ Fidelity = 0.9916", ha='center', va='bottom', fontsize=12, fontweight='bold')

        ax[2].legend(loc="upper left", ncol=1)

        plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

        plt.tight_layout()

        plt.savefig(output_file)

'''
    if plot_property == 'execution_time_20':
        data = []
        var = 20
        
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].tolist()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()
        
        geyser_execution_time = (data_geyser[data_geyser['n_variables']==var]['execution_time'] / 1e6).to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
        
        superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).tolist()
        superconducting_execution_time_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()
        
        weaver_execution_time = (data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'] / 1e6).tolist()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]


        data = [[geyser_execution_time[i], superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([geyser_execution_time_mean, superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']

        fig, ax = plt.subplots(1, 1, figsize=(15, 6))

        data = np.array(data)

        spacing = 0.95

        grouped_bar_plot(ax, data, bar_labels=['Geyser', 'Superconducting', 'Atomique', 'Weaver', 'DPQA'], group_labels=[str(i) for i in benchmarks])

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 4
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax.text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-3.64, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax.set_xlabel('Number of variables')

        ax.set_ylabel('Execution time [seconds]')

        ax.set_xlabel('MAX-3SAT Benchmark Suite')

        ax.axvline(9.8, color='grey', linestyle='dashed', linewidth=2)

        ax.text(
            5.4,
            0.225,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax.set_yscale('log')

        ax.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        #plt.xlim(-0.3, 5.85)

        plt.savefig(output_file)

    if plot_property == 'compilation_time':
        data = []
        
        #Check why the compilation times for superconducting and weaver are constant but not for atomique

        avg_improv = 1
        
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['runtime']).mean()
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()
            avg_improv *= atomique_execution_time/weaver_execution_time
            data.append([atomique_execution_time, weaver_execution_time, superconducting_execution_time, geyser_execution_time, dpqa_execution_time])

        data = np.array(data)

        print(avg_improv**(1/len(n_variables)))

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver', 'Superconducting', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        ax.set_xlabel('Number of variables')

        ax.set_yscale('log')

        ax.set_ylabel('Compilation time [seconds]')

        #ax.set_title('Compilation time', fontweight='bold')

        plt.xlim(-0.3, 5.85)

        plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.20))

        num_groups, num_bars = data.shape

        spacing = 0.95

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 4
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax.text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax.text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        nan_n = 2
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax.text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax.text(
            3,
            10**4.5,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'compilation_time_20':
        data = []
        
        #Check why the compilation times for superconducting and weaver are constant but not for atomique

        avg_improv = 1
        
        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].to_list()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
        
        geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
        
        superconducting_execution_time = data_superconducting[data_superconducting['n_variables']==var]['runtime'].to_list()
        superconducting_execution_time_mean = data_superconducting[data_superconducting['n_variables']==var]['runtime'].mean()

        weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].to_list()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()

        dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        #avg_improv *= atomique_execution_time/weaver_execution_time

        data = [[geyser_execution_time[i], superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([geyser_execution_time_mean, superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
        #if superconducting_fidelity < 1e-20:
        #    superconducting_fidelity = 0

        #if atomique_fidelity < 1e-20:
        #    atomique_fidelity = 0
        
        data = np.array(data)

        fig, ax = plt.subplots(1, 1, figsize=(14, 6))

        grouped_bar_plot(ax, data, bar_labels=['Geyser', 'Superconducting', 'Atomique', 'Weaver', 'DPQA'], group_labels=[str(i) for i in benchmarks])

        ax.set_xlabel('MAX-3SAT Benchmark Suite')

        ax.axvline(9.8, color='grey', linestyle='dashed', linewidth=2)

        ax.text(
            5.4,
            18000,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax.set_yscale('log')

        ax.set_ylabel('Compilation time [seconds]')

        spacing = 0.95

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 4
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax.text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.43, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Compilation time', fontweight='bold')

        #plt.xlim(-0.3, 5.85)

        plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'all_compilation_time_execution_time':
        data = []
        
        avg_improv = 1
        fig, ax = plt.subplots(3, 2, figsize=(22, 10))

        # Compilation time fixed 20 variables
        
        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].to_list()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
        
        geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
        
        superconducting_execution_time = data_superconducting[data_superconducting['n_variables']==var]['runtime'].to_list()
        superconducting_execution_time_mean = data_superconducting[data_superconducting['n_variables']==var]['runtime'].mean()

        weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].to_list()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()

        #dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        #avg_improv *= atomique_execution_time/weaver_execution_time

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
        #if superconducting_fidelity < 1e-20:
        #    superconducting_fidelity = 0

        #if atomique_fidelity < 1e-20:
        #    atomique_fidelity = 0
        

        data = np.array(data)

        grouped_bar_plot(ax[0][0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        ax[0][0].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[0][0].text(
            8.5,
            60000,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[0][0].set_yscale('log')

        ax[0][0].set_ylabel('Compilation time [seconds]')

        ax[0][0].set_title('(a) Compilation time - Fixed size circuit', fontweight='bold', loc='left')

        spacing = 0.95

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[0][0].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.43, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Compilation time', fontweight='bold')

        #plt.xlim(-0.3, 5.85)

        # Compilation time variable 

        data = []

        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['runtime']).mean()
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()
            avg_improv *= atomique_execution_time/weaver_execution_time
            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])
        
        data = np.array(data)

        print(avg_improv**(1/len(n_variables)))

        #fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax[0][1], data, bar_labels=['Atomique', 'Weaver', 'Superconducting', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        ax[0][1].set_yscale('log')

        ax[0][1].set_title('(b) Compilation time - Variable size circuit', fontweight='bold', loc='left')

        #ax[0][1].set_ylabel('Compilation time [seconds]')

        #ax[0].set_title('Compilation time', fontweight='bold')

        num_groups, num_bars = data.shape

        spacing = 0.95

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        ax[0][1].set_xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[0][1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax[0][1].text(
            4.5,
            10**4.5,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        # Execution time fixed 20 variables

        data = []

        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].tolist()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()
        
        geyser_execution_time = (data_geyser[data_geyser['n_variables']==var]['execution_time'] / 1e6).to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
        
        superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).tolist()
        superconducting_execution_time_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()
        
        weaver_execution_time = (data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'] / 1e6).tolist()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        #dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']

        data = np.array(data)

        grouped_bar_plot(ax[1][0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[1][0].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-3.64, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax[1][0].set_ylabel('Execution time [seconds]')

        ax[1][0].set_title('(2a) Execution time - Fixed size', fontweight='bold', loc='left')

        ax[1][0].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[1][0].text(
            8.5,
            0.225,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1][0].set_yscale('log')

        # Execution time variable

        data = []
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()# * 1e6
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()# * 1e6
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])

        data = np.array(data)

        num_groups, num_bars = data.shape

        grouped_bar_plot(ax[1][1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax[1][1].text(
            4.5,
            4,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        #ax[1][1].set_ylabel('Execution time [seconds]')

        ax[1][1].set_title('(b) Execution time - Variable size', fontweight='bold', loc='left')

        ax[1][1].set_yscale('log')

        ax[1][1].set_xlim(-0.3, 5.85)

        #plt.xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[1][1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-3.65, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')


        # Estimated probability of success fixed 20 variables

        data = []

        var = 20

        atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].to_list()
        atomique_fidelity_mean = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()

        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).tolist()
        superconducting_fidelity_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
        
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].tolist()
        dpqa_fidelity_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].to_list()
        weaver_fidelity_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()

        #dpqa_fidelity = [dpqa_fidelity[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        geyser_fidelity = [np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
        geyser_fidelity_mean = np.NAN

        data = [[superconducting_fidelity[i], atomique_fidelity[i], weaver_fidelity[i], dpqa_fidelity[i], geyser_fidelity[i]] for i in range(len(atomique_fidelity))]
        
        data.append([superconducting_fidelity_mean, atomique_fidelity_mean, weaver_fidelity_mean, dpqa_fidelity_mean, geyser_fidelity_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        grouped_bar_plot(ax[2][0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[2][0].set_ylabel('Estimated probability of success')

        ax[2][0].set_title('(3a) Estimated probability of success (EPS) - Fixed size', fontweight='bold', loc='left')
        #ax[2][0].set_titlex#"('(a) Estimated probability of success (EPS) - Fixed size', fontweight='bold', loc='left')

        ax[2][0].set_yscale('log')

        ax[2][0].axvline(9.8, color='grey', linestyle='dashed', linewidth=2)

        ax[2][0].text(
            8.5,
            0.23,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[2][0].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-10, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        # Estimated probability of success variable

        avg_improv = 1
        data = []

        for var in n_variables:
            atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()
            superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
            dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()
            avg_improv *= atomique_fidelity/weaver_fidelity
            #superconducting_fidelity = np.NAN.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
            geyser_fidelity = np.NAN

            data.append([superconducting_fidelity, atomique_fidelity, weaver_fidelity, dpqa_fidelity, geyser_fidelity])
        
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        num_groups, num_bars = data.shape

        print(avg_improv**(1/len(n_variables)))

        grouped_bar_plot(ax[2][1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[2][1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-185, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[2][1].set_ylabel('Estimated probability of success (EPS)')

        ax[2][1].text(
            4.5,
            10**12,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[2][1].set_title('(3b) Estimated probability of success (EPS) - Variable size', fontweight='bold', loc='left')

        ax[2][1].set_xlabel('Number of variables')

        ax[2][0].set_xlabel('MAX-3SAT Benchmark Suite')

        ax[2][1].set_yscale('log')

        plt.xlim(-0.3, 5.85)
        
        #plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        ax[2][0].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        ax[2][1].legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'compilation_time_execution_time':
        data = []
        
        avg_improv = 1
        
        fig, ax = plt.subplots(3, 1, figsize=(14, 10))

        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['runtime']).mean()
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()
            avg_improv *= atomique_execution_time/weaver_execution_time
            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])
        
        data = np.array(data)

        print(avg_improv**(1/len(n_variables)))

        #fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax[0], data, bar_labels=['Atomique', 'Weaver', 'Superconducting', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        ax[0].set_yscale('log')

        ax[0].set_title('(a) Compilation time', fontweight='bold')

        ax[0].set_ylabel('Compilation time [seconds]')

        #ax[0].set_title('Compilation time', fontweight='bold')

        num_groups, num_bars = data.shape

        spacing = 0.95

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        ax[0].set_xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[0].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax[0].text(
            4.5,
            10**4.6,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        data = []
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()# * 1e6
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()# * 1e6
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

            data.append([superconducting_execution_time, atomique_execution_time, weaver_execution_time, dpqa_execution_time, geyser_execution_time])

        data = np.array(data)

        grouped_bar_plot(ax[1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax[1].text(
            4.5,
            4,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1].set_ylabel('Execution time [seconds]')

        ax[1].set_title('(b) Execution time', fontweight='bold')

        ax[1].set_yscale('log')

        ax[1].set_xlim(-0.3, 5.85)

        #plt.xlim(-0.3, 5.85)

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[1].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-3.65, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #nan_n = 3
        #for j in range(num_groups):
        #    if np.isnan(data[j][nan_n]):
        #        ax[1].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')
#
        #nan_n = 4
        #for j in range(num_groups):
        #    if np.isnan(data[j][nan_n]):
        #        ax[1].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.29, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        avg_improv = 1
        data = []
        for var in n_variables:
            atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()
            superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
            dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()
            avg_improv *= atomique_fidelity/weaver_fidelity
            #superconducting_fidelity = np.NAN.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
            geyser_fidelity = np.NAN

            data.append([superconducting_fidelity, atomique_fidelity, weaver_fidelity, dpqa_fidelity, geyser_fidelity])
        
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        print(avg_improv**(1/len(n_variables)))

        grouped_bar_plot(ax[2], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in n_variables])

        for nan_n in range(5):
            for j in range(num_groups):
                if np.isnan(data[j][nan_n]):
                    ax[2].text((nan_n+j*num_groups)//num_groups+nan_n*bar_width, 10**-185, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[2].set_ylabel('Estimated probability of success (EPS)')

        ax[2].text(
            4.5,
            10**12,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[2].set_title('(c) Estimated probability of success (EPS)', fontweight='bold')

        plt.xlabel('Number of variables')

        ax[2].set_yscale('log')

        plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        plt.xlim(-0.3, 5.85)
        
        plt.tight_layout()

        plt.savefig(output_file)


    if plot_property == 'fidelity':

        avg_improv = 1
        data = []
        for var in n_variables:
            atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()
            #superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
            dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()
            avg_improv *= atomique_fidelity/weaver_fidelity
            data.append([atomique_fidelity, weaver_fidelity, dpqa_fidelity])
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        print(avg_improv**(1/len(n_variables)))

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver', 'DPQA'], group_labels=[str(i) for i in n_variables])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax.set_ylabel('Estimated probability of success (EPS)')

        ax.set_xlabel('Number of variables')

        ax.set_yscale('log')

        plt.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))

        #plt.tight_layout()

        #plt.savefig(output_file)

    if plot_property == 'fidelity_20':
        data = []
        var = 20
        pdb.set_trace()
        atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].to_list()
        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps']
        weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].to_list()

        data = [[superconducting_execution_time[i], atomique_fidelity[i], weaver_fidelity[i], dpqa_fidelity[i]] for i in range(len(atomique_execution_time))]
        data.append([geyser_execution_time_mean, superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']

        benchmarks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0
#
            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        fig, ax = plt.subplots(1, 1, figsize=(12, 6))

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver'], group_labels=[str(i) for i in benchmarks])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax.set_ylabel('Estimated probability of success (EPS)')

        ax.set_xlabel('Number of variables')

        ax.set_yscale('log')

        plt.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'weaver_gates':
        data = []

        fids = [0.9775, 0.98, 0.9825, 0.985, 0.9875, 0.99, 0.9925, 0.995, 0.9975]

        for var in fids:
            weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==var][data_weaver['num_variables']==n_variables[0]]['eps (fidelity)'].mean()
            data.append(weaver_fidelity)

        atomique_fidelity = data_atomique[data_atomique['n_variables']==n_variables[0]]['total_fidelity'].mean()
        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==n_variables[0]]['eps']).mean()
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==n_variables[0]]['eps'].mean()

            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0

            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0


        #data = np.array(data).reshape(len(fids), 1)
        #fids = np.array(fids).reshape(len(fids), 1)

        data = [[data[i],fids[i]] for i in range(len(fids))]
        
        data = pd.DataFrame(data, columns=['ccz_fidelity', 'eps'])

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        #grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver'], group_labels=[str(i) for i in n_variables])

        sns.set_theme()
        sns.set_style("whitegrid")

        sns.lineplot(ax=ax, data=data, x='eps', y='ccz_fidelity', label='Weaver', markers='o', linewidth=2)

        #ax.set_ylabel('Weaver', color='b')
        #ax.set_xlabel(xlabel)

        #xkey:str, xlabel: str, ykeys: list[str], labels: list[str], data: pd.DataFrame, filename: str

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        FONTSIZE = 12
        HIGHERISBETTER = "Higher is better ↑"
        LOWERISBETTER = "Lower is better ↓"
        ISBETTER_FONTSIZE = FONTSIZE + 2

        #ax.text(
        #    2.8,
        #    0.10,
        #    HIGHERISBETTER,
        #    ha="center",
        #    fontsize=ISBETTER_FONTSIZE,
        #    fontweight="bold",
        #    color="midnightblue",
        #)

        ax.set_ylabel('Estimated probability of success (eps)')

        ax.set_xlabel('CCZ Gate Fidelity')

        ax.hlines(atomique_fidelity, label='Atomique', colors='r', linestyles='dashed', xmin=0.9775, xmax=0.9975, linewidth=2)
        ax.hlines(superconducting_fidelity, label='Superconducting', colors='g', linestyles='dashdot', xmin=0.9775, xmax=0.9975, linewidth=2)
        ax.hlines(dpqa_fidelity, label='DPQA', colors='b', linestyles='dotted', xmin=0.9775, xmax=0.9975, linewidth=2)

        ax.text(0.9916, dpqa_fidelity-0.004, "X", ha='center', va='bottom', fontsize=18, fontweight='bold')
        ax.text(0.9875, dpqa_fidelity+0.001, "CCZ Fidelity = 0.9916", ha='center', va='bottom', fontsize=13, fontweight='bold')

        plt.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'n_gates_combination':
        data = []

        data = pd.DataFrame(columns=['System', 'n_variables', '1Q Gates', '2Q Gates', '3Q Gates'])

        for var in n_variables:
            weaver_gates1q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.995]['#u3'].mean()
            weaver_gates2q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.995]['#cz'].mean()
            weaver_gates3q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.995]['#ccz'].mean()

            atomique_gates1q = data_atomique[data_atomique['n_variables']==var]['n_1q_gate'].mean()
            atomique_gates2q = data_atomique[data_atomique['n_variables']==var]['n_2q_gate'].mean()
    
            superconducting_gates1q = data_superconducting[data_superconducting['n_variables']==var]['1q_gates'].mean()
            superconducting_gates2q = data_superconducting[data_superconducting['n_variables']==var]['2q_gates'].mean()

            geyser_gates1q = data_geyser[data_geyser['n_variables']==var]['gates1q'].mean()
            geyser_gates2q = data_geyser[data_geyser['n_variables']==var]['gates2q'].mean()

            data.loc[len(data)] = ['Weaver', var, weaver_gates1q, weaver_gates2q, weaver_gates3q]
            data.loc[len(data)] = ['Atomique', var, atomique_gates1q, atomique_gates2q, 0]
            data.loc[len(data)] = ['Superconducting', var, superconducting_gates1q, superconducting_gates2q, 0]
            data.loc[len(data)] = ['Geyser', var, geyser_gates1q, geyser_gates2q, 0]

        labels = ['1 Qubit Gates', '2 Qubit Gates', '3 Qubit Gates']

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        
        ax = stacked_grouped_bar_plot(ax, data, value_labels=['1Q Gates', '2Q Gates', '3Q Gates'], groups=['1Q Gates', '2Q Gates', '3Q Gates'], group_labels=n_variables, bar_labels=['Weaver', 'Atomique', 'Superconducting', 'Geyser'], ylabel='Number of Gates', xlabel='Number of variables', bar_width=2)

        pdb.set_trace()
            #dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==n_variables[0]]['eps'].mean()

            #data.append(weaver_fidelity)
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0

            #if atomique_fidelity < 1e-20:
        
            #    atomique_fidelity = 0

        #data = np.array(data).reshape(len(fids), 1)
        #fids = np.array(fids).reshape(len(fids), 1)

        #ax.set_ylabel('Weaver', color='b')
        #ax.set_xlabel(xlabel)
    
        #ax.legend(loc='upper left')
        ##xkey:str, xlabel: str, ykeys: list[str], labels: list[str], data: pd.DataFrame, filename: str
#
        ##ax.set_title('Estimated Probability of Success', fontweight='bold')
#
        #ax.set_ylabel('Success probability (eps)')
#
        #ax.set_xlabel('CCZ Gate Fidelity')

        ax.set_yscale('log')

        plt.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'n_pulses':

        #data = pd.DataFrame(columns=['System', 'n_variables', 'Pulses'])
        data = []

        for var in n_variables:
            weaver_gates1q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#u3'].mean()
            weaver_gates2q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#cz'].mean()
            weaver_gates3q = data_weaver[data_weaver['num_variables']==var][data_weaver['ccz_fidelity']==0.98]['#ccz'].mean()

            dpqa_gates1q = data_dpqa[data_dpqa['n_variables']==var]['1q_gates'].mean()
            dpqa_gates2q = data_dpqa[data_dpqa['n_variables']==var]['2q_gates'].mean() 

            atomique_gates1q = data_atomique[data_atomique['n_variables']==var]['n_1q_gate'].mean()
            atomique_gates2q = data_atomique[data_atomique['n_variables']==var]['n_2q_gate'].mean()
    
            geyser_pulses = data_geyser[data_geyser['n_variables']==var]['n_pulses'].mean()

            weaver_pulses = weaver_gates1q + weaver_gates2q*3 + weaver_gates3q*5

            atomique_pulses = atomique_gates1q + atomique_gates2q*3

            print(atomique_pulses, weaver_pulses, atomique_pulses/weaver_pulses)

            dpqa_pulses = dpqa_gates1q + dpqa_gates2q*3

            data.append([atomique_pulses, weaver_pulses, geyser_pulses, dpqa_pulses])

            #data.loc[len(data)] = ['Weaver', var, weaver_pulses]
            #data.loc[len(data)] = ['Atomique', var, atomique_pulses]
            #data.loc[len(data)] = ['Geyser', var, geyser_pulses]

            #dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==n_variables[0]]['eps'].mean()

            #data.append(weaver_fidelity)
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0

            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0

        #data = np.array(data).reshape(len(fids), 1)
        #fids = np.array(fids).reshape(len(fids), 1)

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        data = np.array(data)

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')
        ax.set_yscale('log')

        #ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1]*2)

        ax.set_ylabel('Number of pulses')

        ax.set_xlabel('Number of variables')

        ax.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.xlim(-0.25, 5.75)

        #plt.savefig(output_file)

    if plot_property == 'compilation_time_execution_time_20':
        data = []
        
        #Check why the compilation times for superconducting and weaver are constant but not for atomique

        avg_improv = 1
        fig, ax = plt.subplots(3, 1, figsize=(14, 10))
        
        var = 20
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['compilation_time'].to_list()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['compilation_time'].mean()
        
        geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['runtime'].to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['runtime'].mean()
        
        superconducting_execution_time = data_superconducting[data_superconducting['n_variables']==var]['runtime'].to_list()
        superconducting_execution_time_mean = data_superconducting[data_superconducting['n_variables']==var]['runtime'].mean()

        weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].to_list()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['compilation_time (seconds)'].mean()
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['compile_time'].mean()

        #dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        #avg_improv *= atomique_execution_time/weaver_execution_time

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
        #if superconducting_fidelity < 1e-20:
        #    superconducting_fidelity = 0

        #if atomique_fidelity < 1e-20:
        #    atomique_fidelity = 0
        

        data = np.array(data)

        grouped_bar_plot(ax[0], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        ax[0].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[0].text(
            8.5,
            60000,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[0].set_yscale('log')

        ax[0].set_ylabel('Compilation time [seconds]')

        ax[0].set_title('(a) Compilation time', fontweight='bold')

        spacing = 0.95

        num_groups, num_bars = data.shape

        bar_width = None

        if bar_width == None:
            bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[0].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-1.43, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Compilation time', fontweight='bold')

        #plt.xlim(-0.3, 5.85)

        data = []
        
        atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].tolist()
        atomique_execution_time_mean = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()
        
        geyser_execution_time = (data_geyser[data_geyser['n_variables']==var]['execution_time'] / 1e6).to_list()
        geyser_execution_time_mean = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
        
        superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).tolist()
        superconducting_execution_time_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()
        
        weaver_execution_time = (data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'] / 1e6).tolist()
        weaver_execution_time_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
        
        dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].to_list()
        dpqa_execution_time_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        #dpqa_execution_time = [dpqa_execution_time[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        data = [[superconducting_execution_time[i], atomique_execution_time[i], weaver_execution_time[i], dpqa_execution_time[i], geyser_execution_time[i]] for i in range(len(atomique_execution_time))]
        data.append([superconducting_execution_time_mean, atomique_execution_time_mean, weaver_execution_time_mean, dpqa_execution_time_mean, geyser_execution_time_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']

        data = np.array(data)

        grouped_bar_plot(ax[1], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[1].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-3.64, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax[1].set_ylabel('Execution time [seconds]')

        ax[1].set_title('(b) Execution time', fontweight='bold')

        ax[1].axvline(9.85, color='grey', linestyle='dashed', linewidth=2)

        ax[1].text(
            8.5,
            0.225,
            "Lower is better ↓",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        ax[1].set_yscale('log')

        data = []

        atomique_fidelity = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].to_list()
        atomique_fidelity_mean = data_atomique[data_atomique['n_variables']==var]['total_fidelity'].mean()

        superconducting_fidelity = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).tolist()
        superconducting_fidelity_mean = np.array(data_superconducting[data_superconducting['n_variables']==var]['eps']).mean()
        
        dpqa_fidelity = data_dpqa[data_dpqa['n_variables']==var]['eps'].tolist()
        dpqa_fidelity_mean = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

        weaver_fidelity = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].to_list()
        weaver_fidelity_mean = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['eps (fidelity)'].mean()

        #dpqa_fidelity = [dpqa_fidelity[0], np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]

        geyser_fidelity = [np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
        geyser_fidelity_mean = np.NAN

        data = [[superconducting_fidelity[i], atomique_fidelity[i], weaver_fidelity[i], dpqa_fidelity[i], geyser_fidelity[i]] for i in range(len(atomique_execution_time))]
        
        data.append([superconducting_fidelity_mean, atomique_fidelity_mean, weaver_fidelity_mean, dpqa_fidelity_mean, geyser_fidelity_mean])

        benchmarks = ['uf20-01', 'uf20-02', 'uf20-03', 'uf20-04', 'uf20-05', 'uf20-06', 'uf20-07', 'uf20-08', 'uf20-09', 'uf20-10', 'Mean']
        
            #if superconducting_fidelity < 1e-20:
            #    superconducting_fidelity = 0

            #if atomique_fidelity < 1e-20:
            #    atomique_fidelity = 0
        
        data = np.array(data)

        grouped_bar_plot(ax[2], data, bar_labels=['Superconducting', 'Atomique', 'Weaver', 'DPQA', 'Geyser'], group_labels=[str(i) for i in benchmarks])

        #ax.set_title('Estimated Probability of Success', fontweight='bold')

        ax[2].set_ylabel('Estimated probability of success')

        plt.xlabel('MAX-3SAT Benchmark Suite')

        ax[2].set_title('(c) Estimated probability of success (EPS)', fontweight='bold')

        ax[2].set_yscale('log')

        ax[2].axvline(9.8, color='grey', linestyle='dashed', linewidth=2)

        ax[2].text(
            8.5,
            0.225,
            "Higher is better ↑",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color="midnightblue",
        )

        num_groups, num_bars = data.shape

        bar_width = spacing / (num_bars + 1)

        bar_width = bar_width * 1.1

        nan_n = 3
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[2].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-10, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')

        nan_n = 4
        for j in range(num_groups):
            if np.isnan(data[j][nan_n]):
                ax[2].text((nan_n+j*num_groups-1)//num_groups+nan_n*bar_width, 10**-10, "X", ha='center', va='bottom', fontsize=11, fontweight='bold')


        plt.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.45))

        plt.tight_layout()

        plt.savefig(output_file)

    if plot_property == 'execution_time':
        data = []
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean()# * 1e6
            geyser_execution_time = data_geyser[data_geyser['n_variables']==var]['execution_time'].mean() / 1e6
            superconducting_execution_time = np.array(data_superconducting[data_superconducting['n_variables']==var]['execution_time']).mean()# * 1e6
            weaver_execution_time = data_weaver[data_weaver['ccz_fidelity']==0.98][data_weaver['num_variables']==var]['execution_time (microseconds)'].mean() / 1e6
            dpqa_execution_time = data_dpqa[data_dpqa['n_variables']==var]['eps'].mean()

            data.append([atomique_execution_time, weaver_execution_time, superconducting_execution_time, geyser_execution_time, dpqa_execution_time])
        data = np.array(data)

        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Weaver', 'Superconducting', 'Geyser', 'DPQA'], group_labels=[str(i) for i in n_variables])

        #ax.set_title('Circuit execution time', fontweight='bold')

        ax.set_xlabel('Number of variables')

        ax.set_ylabel('Execution time [seconds]')

        ax.set_yscale('log')

        ax.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.3))

        plt.tight_layout()

        plt.xlim(-0.3, 5.85)

        plt.savefig(output_file)
'''

def get_circuit_n_operations():

    circuit_list = [
        'a1_n20.qasm',
        'a1_n50.qasm',
        'a1_n75.qasm',
        'a1_n100.qasm',
        'a1_n150.qasm',
        'a1_n250.qasm',
    ]

    n_operations = []

    for name in circuit_list:
        qc = QuantumCircuit.from_qasm_file('./evaluation/benchmarks/QASMBench/' + name)
        operations = qc.count_ops()
        n_operations.append(0)

        for i in list(operations.items()):
            name, nops = i
            if name != 'barrier' and name != 'measure':
                n_operations[-1] += nops

    return n_operations