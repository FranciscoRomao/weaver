// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4)]
qreg q[5];
creg m0[5];  // Measurement: q(0),q(1),q(2),q(3),q(4)


h q[0];
cx q[0],q[1];
cx q[1],q[2];
cx q[2],q[3];
cx q[3],q[4];

// Gate: cirq.MeasurementGate(5, cirq.MeasurementKey(name='q(0),q(1),q(2),q(3),q(4)'), ())
measure q[0] -> m0[0];
measure q[1] -> m0[1];
measure q[2] -> m0[2];
measure q[3] -> m0[3];
measure q[4] -> m0[4];
