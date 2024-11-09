// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6), q(7), q(8), q(9), q(10)]
qreg q[11];
// creg m_mcm0[5];
// creg m_mcm1[5];
// creg m_mcm2[5];
creg m_meas_all[11];


h q[0];
h q[2];
h q[4];
h q[6];
h q[8];
h q[10];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[0];
h q[2];
h q[4];
h q[6];
h q[8];
h q[10];
cz q[0],q[1];
cz q[2],q[1];
h q[0];
cz q[2],q[3];
h q[1];
h q[0];
cz q[4],q[3];
h q[2];
cz q[4],q[5];
h q[3];
h q[2];
cz q[6],q[5];
h q[4];
cz q[6],q[7];
h q[5];
h q[4];
cz q[8],q[7];
h q[6];
cz q[8],q[9];
h q[7];
h q[6];
cz q[10],q[9];
h q[8];
h q[9];
h q[10];
h q[8];

// Gate: cirq.MeasurementGate(5, cirq.MeasurementKey(name='mcm0'), ())
// measure q[1] -> m_mcm0[0];
// measure q[3] -> m_mcm0[1];
// measure q[5] -> m_mcm0[2];
// measure q[7] -> m_mcm0[3];
// measure q[9] -> m_mcm0[4];

h q[10];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
cz q[0],q[1];
cz q[2],q[1];
h q[0];
cz q[2],q[3];
h q[1];
h q[0];
cz q[4],q[3];
h q[2];
cz q[4],q[5];
h q[3];
h q[2];
cz q[6],q[5];
h q[4];
cz q[6],q[7];
h q[5];
h q[4];
cz q[8],q[7];
h q[6];
cz q[8],q[9];
h q[7];
h q[6];
cz q[10],q[9];
h q[8];
h q[9];
h q[10];
h q[8];

// Gate: cirq.MeasurementGate(5, cirq.MeasurementKey(name='mcm1'), ())
// measure q[1] -> m_mcm1[0];
// measure q[3] -> m_mcm1[1];
// measure q[5] -> m_mcm1[2];
// measure q[7] -> m_mcm1[3];
// measure q[9] -> m_mcm1[4];

h q[10];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];
cz q[0],q[1];
cz q[2],q[1];
h q[0];
cz q[2],q[3];
h q[1];
h q[0];
cz q[4],q[3];
h q[2];
cz q[4],q[5];
h q[3];
h q[2];
cz q[6],q[5];
h q[4];
cz q[6],q[7];
h q[5];
h q[4];
cz q[8],q[7];
h q[6];
cz q[8],q[9];
h q[7];
h q[6];
cz q[10],q[9];
h q[8];
h q[9];
h q[10];
h q[8];

// Gate: cirq.MeasurementGate(5, cirq.MeasurementKey(name='mcm2'), ())
// measure q[1] -> m_mcm2[0];
// measure q[3] -> m_mcm2[1];
// measure q[5] -> m_mcm2[2];
// measure q[7] -> m_mcm2[3];
// measure q[9] -> m_mcm2[4];

h q[10];
h q[1];
h q[3];
h q[5];
h q[7];
h q[9];

// Gate: cirq.MeasurementGate(11, cirq.MeasurementKey(name='meas_all'), ())
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
