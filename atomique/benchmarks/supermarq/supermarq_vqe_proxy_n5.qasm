// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4)]
qreg q[5];
creg m0[5];  // Measurement: q(0),q(1),q(2),q(3),q(4)


ry(pi*2.2556302668) q[0];
ry(pi*2.1113022111) q[1];
ry(pi*3.9228448735) q[2];
ry(pi*0.5267076233) q[3];
ry(pi*1.3821334607) q[4];
rz(pi*0.9029100958) q[0];
rz(pi*0.3643014136) q[1];
rz(pi*2.4375256641) q[2];
rz(pi*2.9127908904) q[3];
rz(pi*0.3059348822) q[4];
cx q[0],q[1];
cx q[1],q[2];
ry(pi*3.981662561) q[0];
cx q[2],q[3];
ry(pi*0.4372026764) q[1];
rz(pi*1.050060556) q[0];
cx q[3],q[4];
ry(pi*1.3754532502) q[2];
rz(pi*2.5580080834) q[1];
ry(pi*0.7145260027) q[3];
ry(pi*0.0850017328) q[4];
rz(pi*2.0032259674) q[2];
rz(pi*3.9539978313) q[3];
rz(pi*0.2087844816) q[4];

// Gate: cirq.MeasurementGate(5, cirq.MeasurementKey(name='q(0),q(1),q(2),q(3),q(4)'), ())
measure q[0] -> m0[0];
measure q[1] -> m0[1];
measure q[2] -> m0[2];
measure q[3] -> m0[3];
measure q[4] -> m0[4];
