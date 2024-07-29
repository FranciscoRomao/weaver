# main_evaluation.py
import sys
import yaml
import pdb
import evaluation.scripts.geyser as geyser
import evaluation.scripts.instances_to_qasm as instances_to_qasm
import evaluation.scripts.superconducting as superconducting
import evaluation.scripts.atomique as atomique
import evaluation.scripts.plot as plot
#import .qcomp.evaluation.scripts.optimization_fidelity as optimization_fidelity
#import scripts.mapping_similarity as mapping_similarity
#import scripts.qubits_use_frequency as qubits_use_frequency
#import scripts.compilation_execution as compliation_execution
#import scripts.success_prob as success_prob
#import scripts.synthesis_vs_caching as synthesis_vs_caching
#import scripts.final_evaluation as final_evaluation

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def main():
    if len(sys.argv) <= 2:
        print("Usage: python evaluation.py <evaluation_script> <run/plot>")
        sys.exit(1)

    config = load_config('evaluation/config.yml')
    evaluation_script = sys.argv[1]
    action = sys.argv[2]

    if evaluation_script not in config:
        print(f"Evaluation script '{evaluation_script}' not found in configuration.")
        sys.exit(1)

    # Run selected evaluation script with its respective settings
    if evaluation_script == 'atomique':
        if action == 'run':
            atomique.run(config[evaluation_script][action])
        elif action == 'plot':
            atomique.plot(config[evaluation_script][action])
    elif evaluation_script == 'geyser':
        if action == 'run':
            geyser.run(config[evaluation_script][action])
        elif action == 'plot':
            geyser.plot(config[evaluation_script][action])
    elif evaluation_script == 'superconducting':
        if action == 'run':
            superconducting.run(config[evaluation_script][action])
        elif action == 'plot':
            superconducting.plot(config[evaluation_script][action])
    elif evaluation_script == 'instances_to_qasm':
        if action == 'run':
            instances_to_qasm.run(config[evaluation_script][action])
        elif action == 'plot':
            instances_to_qasm.plot(config[evaluation_script][action])
    elif evaluation_script == 'plot':
        if action == 'run':
            plot.plot(config[evaluation_script][action])
        elif action == 'plot':
            plot.plot(config[evaluation_script][action])
    else:
        print("Invalid evaluation script.")
        sys.exit(1)

if __name__ == "__main__":
    main()
