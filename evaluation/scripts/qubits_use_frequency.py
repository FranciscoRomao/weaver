from qiskit.transpiler.passes import SabreLayout
from qiskit import QuantumCircuit
from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService
from benchmarks.circuits.circuits import BENCHMARK_CIRCUITS, get_circuit
import pdb
from utils.utils_fid import calculate_expected_fidelity
from qiskit.transpiler.layout import Layout
from benchmarks.plot.util import grouped_bar_plot, bar_plot

#Change number of iterations in SabreLayout pass by hand

def remove_ancillas_from_layout(layout) -> list:
    new_layout = {}
    for (a,b) in layout.items():
        if b._register.name != 'ancilla':
            new_layout[b] = a

    return Layout(new_layout)

def run(config):
    nqubits = config['nqubits']
    runs = config['runs']
    backend_name = config['backend']
    
    QiskitRuntimeService.save_account(channel="ibm_quantum", token='99e75b5d99553974336a52afc3609a7d935b1ab6cda362ccd22c3ca59d9d70ad912cea56c4f8702607296aff58c059fa47830ef23422c0e747926be890b552cd', overwrite=True)
    service = QiskitRuntimeService(instance="ibm-q/open/main")
    backend = service.backend(backend_name)

    all_circuits = [[] for _ in nqubits]
    all_layouts = [[] for _ in nqubits]

    for j,nq in enumerate(nqubits):
        for i,circ in enumerate(BENCHMARK_CIRCUITS):
            circuit = get_circuit(circ, nq)
            all_circuits.append(circuit)
            best_fid = 0
            print(f"Transpiling circuit {i} out of {len(BENCHMARK_CIRCUITS)} for {nq} qubits")
            for _ in range(runs):

                trans_circ = transpile(circuit, backend, optimization_level=3)

                fid = calculate_expected_fidelity(trans_circ, backend)

                if fid > best_fid:
                    layout = remove_ancillas_from_layout(trans_circ.layout.initial_layout.get_physical_bits())
                    backend_qubits = list(layout.get_physical_bits().keys())
                    #if len(all_layouts) != 0 and best_fid != 0:
                    #    all_layouts.pop(-1)
                    best_fid = fid
            all_layouts[j] += backend_qubits

    #counts = [[] for _ in nqubits]
    counts = []

    for i,layout in enumerate(all_layouts):
        unique = np.unique(layout)

        counts.append(len(unique)/backend.num_qubits)

        #for j in unique:
        #    counts.append(layout.count(j))

    #qubits = [0 for _ in range(backend.configuration().n_qubits)]

    #for i in range(len(qubits)):
    #    tmp = counts.append(all_layouts.count(i))
    #    if tmp == None:
    #        qubits[i] = 0

    layout = backend.coupling_map.draw()

    #data = pd.DataFrame({'qubit': qubits, 'count': counts})
    data = pd.DataFrame({'Nqubits': nqubits, 'count': counts})
    data.to_csv('backend_use_ratio.csv')

    #data.plot(kind='bar', x='qubit', y='count', title='Qubit Frequency in Layout', xlabel='Qubit', ylabel='Frequency')
    #plt.savefig('qubit_frequency.pdf')

def plot(config):
    #input_files = [config['input']+'_opt0.csv', config['input']+'_opt3.csv']
    #dfs = []
    #dfs.append(pd.read_csv(input_files[0], header=None, names=['col1', 'col2', 'col3']))
    #dfs.append(pd.read_csv(input_files[1], header=None, names=['col1', 'col2', 'col3']))
    #output = config['output'] 
    #sns.set_style(style="whitegrid")
    #sns.set_palette("deep")
    
    #fig = plt.figure(figsize=(10, 4))
    #nrows = 1
    #ncols = 2
    #gs = gridspec.GridSpec(nrows=nrows, ncols=ncols)
    #axes = [fig.add_subplot(gs[i, j]) for i in range(nrows) for j in range(ncols)]
#
    #for i,df in enumerate(dfs):
    #    first_y_value = df['col3'].min()
    #    df['normalized_col3'] = df['col3'] / first_y_value
#
    #    degree = 5  # Change the degree as needed
    #    coefficients = np.polyfit(df['col2'], df['normalized_col3'], degree)
    #    poly_function = np.poly1d(coefficients)
    #    x_values = np.linspace(df['col2'].min(), df['col2'].max(), 100)
    #    y_values = poly_function(x_values)
    #    axes[i].plot(x_values, y_values, label='Polynomial Regression (Degree {})'.format(degree))
#
    #    sns.scatterplot(ax=axes[i], x='col2', y='normalized_col3', data=df, label='Data')
#
    #    #sns.lineplot(x='col2', y='col3', data=df, marker='o')
    #    plt.xlabel('Compilation Time (s)')
    #    plt.ylabel('Fidelity (x times increase)')
#
    #    if i == 0:
    #        plt.title('Fidelity vs Compilation Time (Slow Search)', fontweight='bold', fontsize=12)
    #    else:
    #        plt.title('Fidelity vs Compilation Time (Fast Search))', fontweight='bold', fontsize=12)

        #two barplots one with time and another with fid, grouped by nqubits
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