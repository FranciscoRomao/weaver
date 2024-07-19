// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5)]
qreg q[6];
creg m0[6];  // Measurement: q(0),q(1),q(2),q(3),q(4),q(5)


ry(pi*3.9994454207) q[0];
ry(pi*1.9989616952) q[1];
ry(pi*0.9774002677) q[2];
ry(pi*2.9296871867) q[3];
ry(pi*3.4618789111) q[4];
ry(pi*1.4784672583) q[5];
rz(pi*1.8428553276) q[0];
rz(pi*2.8026967274) q[1];
rz(pi*3.1898777033) q[2];
rz(pi*3.7895643148) q[3];
rz(pi*3.1687700932) q[4];
rz(pi*1.9701902789) q[5];
cx q[0],q[1];
cx q[1],q[2];
ry(pi*0.168873415) q[0];
cx q[2],q[3];
ry(pi*2.1677624094) q[1];
rz(pi*1.9999502603) q[0];
cx q[3],q[4];
ry(pi*0.8239031662) q[2];
rz(pi*4.0003084262) q[1];
cx q[4],q[5];
ry(pi*1.7729137743) q[3];
rz(pi*2.9957106552) q[2];
ry(pi*2.6312486463) q[4];
ry(pi*0.3197040775) q[5];
rz(pi*3.0674420793) q[3];
rz(pi*2.3591502873) q[4];
rz(pi*2.9928016473) q[5];

// Gate: cirq.MeasurementGate(6, cirq.MeasurementKey(name='q(0),q(1),q(2),q(3),q(4),q(5)'), ())
measure q[0] -> m0[0];
measure q[1] -> m0[1];
measure q[2] -> m0[2];
measure q[3] -> m0[3];
measure q[4] -> m0[4];
measure q[5] -> m0[5];
