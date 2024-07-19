import logging
import os

from qiskit import QuantumCircuit

from .block_circuit import BlockCircuit
from .map_circuit import MapCircuit

logging.disable(logging.INFO)

NUM_ITERATIONS = 1


def geyser(circ, hyperparams):
    use_blocking = hyperparams.geyser_use_blocking
    circuits = {}

    circuits["Original"] = circ

    layout = None
    blocks = None
    min_num_blocks = float("inf")

    for _ in range(NUM_ITERATIONS):

        mapper = MapCircuit(circuits["Original"], hyperparams)

        layout = mapper.get_layout()

        blocks = mapper.get_blocks()

        mapped = mapper.get_mapped_circuit()
        circuits["Mapped"] = mapped

        if use_blocking:

            blocker = BlockCircuit(layout, blocks, mapped)

            num_blocks, blocked = blocker.get_blocked_circuit()

            if num_blocks < min_num_blocks:
                circuits["Mapped"] = mapped
                circuits["Blocked"] = blocked
                min_num_blocks = num_blocks

    # new_name = full_path.replace('.qasm', '_geyser.qasm')
    # new_name = new_name.replace('.pt', '_geyser.qasm')
    # with open(new_name, 'w') as f:
    #     f.write(circuits['Mapped'].qasm())
    return circuits["Mapped"]
