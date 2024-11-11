import sys
import yaml
import pdb
import superconducting_run
import geyser_run
import atomique_run
import utils.instances_to_dpqa_json as instances_to_dpqa_json
import utils.instances_to_qasm as instances_to_qasm
import dpqa_run
import weaver_run
import plot

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def main():
    

    print('Transpiling MAX-3SAT instances to QASM circuits')
    instances_to_qasm.run()
    
    print('Running Atomique')
    atomique_run.run()

    print('Running Superconducting (Qiskit)')
    superconducting_run.run()
    
    print('Running Geyser')
    geyser_run.run()
    
    print('Running Weaver')
    weaver_run.run()

    print('Transpiling QASM circuits to DPQA JSON')
    instances_to_dpqa_json.run()
    
    print('Running DPQA')
    dpqa_run.run()
    
    print('Plotting compilation time comparison')
    plot.plot_compilation_time()

    print('Plotting execution time comparison')
    plot.plot_execution_time()
    
    print('Plotting fidelity comparison')
    plot.plot_fidelity()
    
    print('Plotting analysis plots')
    plot.plot_analysis()

if __name__ == "__main__":
    main()
