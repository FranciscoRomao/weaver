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
    #config = load_config('evaluation/config.yml')
    #evaluation_script = sys.argv[1]
    #action = sys.argv[2]

    #instances_to_qasm.run()
    atomique_run.run()
    #superconducting_run.run()
    #geyser_run.run()
    #weaver_run.run()
    #instances_to_dpqa_json.run()
    #dpqa_run.run()
    
    #plot.plot_compilation_time()
    #plot.plot_execution_time()
    #plot.plot_fidelity()
    #plot.plot_analysis()

if __name__ == "__main__":
    main()
