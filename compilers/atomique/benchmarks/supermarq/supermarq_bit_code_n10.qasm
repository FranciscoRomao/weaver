// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6), q(7), q(8), q(9), q(10), q(11), q(12), q(13), q(14), q(15), q(16), q(17), q(18)]
qreg q[19];
// creg m_mcm0[9];
// creg m_mcm1[9];
// creg m_mcm2[9];
creg m_meas_all[19];


cx q[0],q[1];
cx q[2],q[1];
cx q[2],q[3];
cx q[4],q[3];
cx q[4],q[5];
cx q[6],q[5];
cx q[6],q[7];
cx q[8],q[7];
cx q[8],q[9];
cx q[10],q[9];
cx q[10],q[11];
cx q[12],q[11];
cx q[12],q[13];
cx q[14],q[13];
cx q[14],q[15];
cx q[16],q[15];
cx q[16],q[17];
cx q[18],q[17];

// Gate: cirq.MeasurementGate(9, cirq.MeasurementKey(name='mcm0'), ())
// measure q[1] -> m_mcm0[0];
// measure q[3] -> m_mcm0[1];
// measure q[5] -> m_mcm0[2];
// measure q[7] -> m_mcm0[3];
// measure q[9] -> m_mcm0[4];
// measure q[11] -> m_mcm0[5];
// measure q[13] -> m_mcm0[6];
// measure q[15] -> m_mcm0[7];
// measure q[17] -> m_mcm0[8];

h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[11];
h q[13];
h q[15];
h q[17];
cx q[0],q[1];
cx q[2],q[1];
cx q[2],q[3];
cx q[4],q[3];
cx q[4],q[5];
cx q[6],q[5];
cx q[6],q[7];
cx q[8],q[7];
cx q[8],q[9];
cx q[10],q[9];
cx q[10],q[11];
cx q[12],q[11];
cx q[12],q[13];
cx q[14],q[13];
cx q[14],q[15];
cx q[16],q[15];
cx q[16],q[17];
cx q[18],q[17];

// Gate: cirq.MeasurementGate(9, cirq.MeasurementKey(name='mcm1'), ())
// measure q[1] -> m_mcm1[0];
// measure q[3] -> m_mcm1[1];
// measure q[5] -> m_mcm1[2];
// measure q[7] -> m_mcm1[3];
// measure q[9] -> m_mcm1[4];
// measure q[11] -> m_mcm1[5];
// measure q[13] -> m_mcm1[6];
// measure q[15] -> m_mcm1[7];
// measure q[17] -> m_mcm1[8];

h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[11];
h q[13];
h q[15];
h q[17];
cx q[0],q[1];
cx q[2],q[1];
cx q[2],q[3];
cx q[4],q[3];
cx q[4],q[5];
cx q[6],q[5];
cx q[6],q[7];
cx q[8],q[7];
cx q[8],q[9];
cx q[10],q[9];
cx q[10],q[11];
cx q[12],q[11];
cx q[12],q[13];
cx q[14],q[13];
cx q[14],q[15];
cx q[16],q[15];
cx q[16],q[17];
cx q[18],q[17];

// Gate: cirq.MeasurementGate(9, cirq.MeasurementKey(name='mcm2'), ())
// measure q[1] -> m_mcm2[0];
// measure q[3] -> m_mcm2[1];
// measure q[5] -> m_mcm2[2];
// measure q[7] -> m_mcm2[3];
// measure q[9] -> m_mcm2[4];
// measure q[11] -> m_mcm2[5];
// measure q[13] -> m_mcm2[6];
// measure q[15] -> m_mcm2[7];
// measure q[17] -> m_mcm2[8];

h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[11];
h q[13];
h q[15];
h q[17];

// Gate: cirq.MeasurementGate(19, cirq.MeasurementKey(name='meas_all'), ())
measure q[0] -> m_meas_all[0];
measure q[1] -> m_meas_all[1];
measure q[2] -> m_meas_all[2];
measure q[3] -> m_meas_all[3];
measure q[4] -> m_meas_all[4];
measure q[5] -> m_meas_all[5];
measure q[6] -> m_meas_all[6];
measure q[7] -> m_meas_all[7];
measure q[8] -> m_meas_all[8];
measure q[9] -> m_meas_all[9];
measure q[10] -> m_meas_all[10];
measure q[11] -> m_meas_all[11];
measure q[12] -> m_meas_all[12];
measure q[13] -> m_meas_all[13];
measure q[14] -> m_meas_all[14];
measure q[15] -> m_meas_all[15];
measure q[16] -> m_meas_all[16];
measure q[17] -> m_meas_all[17];
measure q[18] -> m_meas_all[18];
