from qiskit.transpiler.passes import SabreLayout
from qiskit import QuantumCircuit
from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
from qiskit.providers.fake_provider import FakeWashington
import pdb

def plot(config):
    nqubits = config['nqubits']
    plot_property = config['plot_property']
    
    backend = FakeWashington()

    data_atomique = pd.read_csv(config['input_atomique'])
    data_geyser = pd.read_csv(config['input_geyser'])
    data_superconducting = pd.read_csv(config['input_superconducting'])

    pdb.set_trace()
    if plot_property == 'execution_time':
        pass    
    
    '''
    data1 = pd.read_csv('backend_use_ratio_osaka.csv')
    data2 = pd.read_csv('backend_use_ratio_sheerbroke.csv')
    data3 = pd.read_csv('backend_use_ratio_brisbane.csv')

    #drop Unnamed column
    pdb.set_trace()
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