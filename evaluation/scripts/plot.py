from qiskit.transpiler.passes import SabreLayout
from qiskit import QuantumCircuit
from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
from qiskit.providers.fake_provider import FakeWashington
from evaluation.utils.plot.util import grouped_bar_plot
import pdb
import matplotlib.pyplot as plt

def plot(config):
    plot_property = config['plot_property']
    
    backend = FakeWashington()

    data_atomique = pd.read_csv(config['atomique_input'])
    data_geyser = pd.read_csv(config['geyser_input'])
    #data_superconducting = pd.read_csv(config['superconducting_input'])
    data_weaver = pd.read_csv(config['weaver_input'])
    output_file = config['output_file']
    n_variables = config['n_variables']

    if not isinstance(n_variables, list):
        n_variables = [n_variables]

    pdb.set_trace()
    if plot_property == 'execution_time':
        data = []
        for var in n_variables:
            atomique_execution_time = data_atomique[data_atomique['n_variables']==var]['execution_time'].mean() * 1e6
            geyser_execution_time = data_geyser['execution_time'].mean() * 1e6
            #superconducting_execution_time = np.array(data_superconducting['execution_time'])
            weaver_execution_time = data_weaver['execution_time (microseconds)'].mean()

            data.append([round(atomique_execution_time,0), round(geyser_execution_time,0), round(weaver_execution_time,0)])

        data = np.array(data)

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))

        grouped_bar_plot(ax, data, bar_labels=['Atomique', 'Geyser', 'Weaver'], group_labels=[str(i) for i in n_variables])

        ax.set_title('Execution time (microseconds)', fontweight='bold')

        plt.legend()

        plt.tight_layout()

        plt.savefig(output_file)
    
    '''
    data1 = pd.read_csv('backend_use_ratio_osaka.csv')
    data2 = pd.read_csv('backend_use_ratio_sheerbroke.csv')
    data3 = pd.read_csv('backend_use_ratio_brisbane.csv')

    #drop Unnamed column
    #pdb.set_trace()
    data = data1 + data2 + data3
    data = data.drop(data.columns[0], axis=1)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))

    data.set_index('Nqubits', inplace=True)
    #sns.set_theme(style='pastel')
    #mean_data = data.groupby('nqubits').mean('whole_time')

    #fid_data = np.array(mean_data[['whole_fid', 'reduced_fid']])
    #time_data = np.array(mean_data[['whole_time', 'reduce_time']])
    index = [str(i) for i in np.array(data.index)]

    #mean_data.plot(kind='bar', y=['whole_fid','reduced_fid'], ax=ax[0], title='Success probability', xlabel='Benchmark size', ylabel='Success probability')
    array = np.array(data[['count']]).reshape(1,8)[0]
    bar_plot(ax, array, index)
    #grouped_bar_plot(ax=ax[0] , y=fid_data, group_labels=index, bar_labels=['Whole backend', 'Reduced backend'])
    #grouped_bar_plot(ax=ax[1], y=time_data, group_labels=index, bar_labels=['Whole backend', 'Reduced backend'])
    #mean_data.plot(kind='bar', y=['whole_time','reduce_time'], ax=ax[1], title='Time', xlabel='Benchmark size', ylabel='Time (s)', legend=False)

    #ax.set_title('Backend used ratio', fontweight='bold')
    ax.set_xlabel('Circuit size')
    ax.set_ylabel('Ratio of backend qubits used')

    plt.tight_layout()
    plt.savefig('backend_use_ratio.pdf')
    '''