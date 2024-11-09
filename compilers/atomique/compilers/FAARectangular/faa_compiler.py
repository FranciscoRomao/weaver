import itertools
import time

import numpy as np
import yaml
from qiskit import transpile

from utils import gen_res_dict, get_hop_distance_square


class FAACompiler(object):
    def __init__(self, configs):
        self.configs = configs
        self.last_transpiled_circ = None

    def run(self, benchmark_sets, hyperparam_sets):
        res_list = []
        for benchmark in benchmark_sets.all_benchmarks:
            for hyperparams in hyperparam_sets.all_sets:
                res_dict = self.compile(benchmark, hyperparams)

                res_dict["hyperparams"] = hyperparams.__dict__.copy()
                res_dict["path"] = benchmark.path

                res_list.append(res_dict)
                print(res_dict)

        yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))

        return res_list

    def gen_cmap(self, n_rows, n_cols, n_aods, bidirect):
        n_qubits = n_rows * n_cols * (n_aods + 1)
        n_rows_cmap = int(np.floor(np.sqrt(n_qubits)))
        n_cols_cmap = n_rows_cmap
        # n_rows_cmap = n_rows
        # n_cols_cmap = n_cols
        # print(n_cols_cmap)
        cmap = []

        # we have n_rows_cmap rows and n_cols_cmap, each one connect to its four neighbors
        for i in range(n_rows_cmap):
            for j in range(n_cols_cmap):
                if i != 0:
                    cmap.append([i * n_cols_cmap + j, (i - 1) * n_cols_cmap + j])
                    if bidirect:
                        cmap.append([(i - 1) * n_cols_cmap + j, i * n_cols_cmap + j])
                if i != n_rows_cmap - 1:
                    cmap.append([i * n_cols_cmap + j, (i + 1) * n_cols_cmap + j])
                    if bidirect:
                        cmap.append([(i + 1) * n_cols_cmap + j, i * n_cols_cmap + j])
                if j != 0:
                    cmap.append([i * n_cols_cmap + j, i * n_cols_cmap + j - 1])
                    if bidirect:
                        cmap.append([i * n_cols_cmap + j - 1, i * n_cols_cmap + j])
                if j != n_cols_cmap - 1:
                    cmap.append([i * n_cols_cmap + j, i * n_cols_cmap + j + 1])
                    if bidirect:
                        cmap.append([i * n_cols_cmap + j + 1, i * n_cols_cmap + j])

        # remove repeated items in cmap and make each item still a list
        # cmap = [list(pair) for pair in set(tuple(item) for item in cmap)]
        cmap.sort()
        cmap = list(k for k, _ in itertools.groupby(cmap))
        # print(len(cmap))

        return cmap, n_rows_cmap, n_cols_cmap

    def compile(self, benchmark, hyperparams):
        start_time = time.time()
        circ = benchmark.circ
        n_rows = hyperparams.n_rows
        n_cols = hyperparams.n_cols
        n_aods = hyperparams.n_aods
        cmap, n_rows_cmap, n_cols_cmap = self.gen_cmap(
            n_rows, n_cols, n_aods, hyperparams.faa_cmap_bidirect
        )
        # print(cmap)

        if (not hyperparams.retranspile) and self.last_transpiled_circ:
            circ_transpiled = self.last_transpiled_circ
            print("reusing last transpiled circ")
        else:
            circ_transpiled = transpile(
                circ,
                basis_gates=["cz", "id", "u1", "u2", "u3"],
                coupling_map=cmap,
                optimization_level=3,
                layout_method="sabre",
                routing_method="sabre",
                seed_transpiler=hyperparams.faa_seed_transpiler,
            )
            self.last_transpiled_circ = circ_transpiled

        hop_dists, hop_dist_mean, hot_dist_std = get_hop_distance_square(
            circ, circ_transpiled, n_rows_cmap, n_cols_cmap
        )

        # print(hop_dist_mean, hot_dist_std)

        res_dict = gen_res_dict(hyperparams, benchmark, circ_transpiled, "na")
        res_dict["circ_stats"]["compilation_time"] = time.time() - start_time
        res_dict["circ_stats"]["hop_dist_mean"] = float(hop_dist_mean)
        res_dict["circ_stats"]["hop_dist_std"] = float(hot_dist_std)
        res_dict["circ_stats"]["hop_dists"] = hop_dists

        return res_dict
