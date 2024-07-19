OPENQASM 2.0;
include "qelib1.inc";
gate c0b0 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,pi/2,-1.6926855) q2; }
gate c0b5 q0,q1 { u3(pi/2,-pi/2,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,-pi/2,1.3941561) q1; }
gate c1b7 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,-pi/2,1.7952533) q2; }
gate c2b3 q0,q1,q2 { u3(pi/2,0,-pi) q0; cz q1,q2; u3(pi/2,0,-pi) q1; u3(2.9229237,0,pi/2) q2; }
gate c3b7 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(2.370867,-2.8163978,-2.9042672) q0; u3(pi/2,0.21866895,0) q1; }
gate c4b8 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q1,q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,-pi) q0; }
gate c5b5 q0,q1 { cz q0,q1; u3(pi/2,0,pi/2) q1; u3(pi/2,0,-pi/2) q0; cz q0,q1; u3(pi/2,0.82694237,0) q1; u3(1.3941561,pi/2,pi/2) q0; }
gate c6b7 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi) q2; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; }
gate c7b4 q0,q1,q2 { cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q2,q1; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,-pi) q2; }
gate c8b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q1,q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,-pi) q0; }
gate c9b1 q0,q1 { cz q1,q0; u3(3.0197035,0,-pi/2) q0; u3(pi/2,0,-pi) q1; }
gate c10b3 q0,q1,q2 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q2; }
gate c11b0 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi/2) q1; u3(pi/2,0,pi/2) q2; cz q1,q2; u3(1.4489071,pi/2,-pi/2) q1; u3(3.0197035,-pi/2,pi/2) q2; cz q1,q0; }
gate c12b6 q0,q1,q2 { cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,pi/2,1.3955169) q1; u3(pi/2,0,-pi) q2; }
gate c13b1 q0,q1,q2 { cz q1,q0; u3(pi/2,-pi/2,-2.9663133) q0; u3(pi/2,0,-pi) q1; cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(pi/2,1.7460757,-pi) q0; u3(pi/2,-0.17527938,-pi) q2; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(1.4429828,0,-pi/2) q0; u3(pi/2,0,-pi) q1; }
gate c14b4 q0,q1 { cz q1,q0; }
gate c15b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q1,q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,-pi) q1; }
gate c16b7 q0,q1,q2 { cz q1,q0; u3(pi/2,0,-pi) q1; cz q2,q0; u3(pi/2,0,-pi) q2; }
gate c17b6 q0,q1,q2 { cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; }
gate c18b0 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(0,-1.406583,1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c18b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,-pi/2,-1.8434144) q0; u3(pi/2,0,-pi) q1; }
gate c19b7 q0,q1,q2 { cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q2,q0; u3(0,-1.406583,1.406583) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; }
gate c20b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; }
gate c21b8 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; }
gate c22b2 q0,q1 { cz q1,q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; }
gate c23b0 q0,q1,q2 { cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; u3(pi/2,pi/2,-0.5880026) q0; u3(pi/2,0,-pi) q2; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,-1.6986099,0) q0; u3(pi/2,0.5880026,0) q1; }
gate c24b2 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q2,q1; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q0,q1; u3(0,0,pi/2) q0; u3(pi/2,0,-pi) q1; }
gate c25b0 q0,q1 { cz q1,q0; }
gate c26b6 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; }
gate c27b0 q0,q1,q2 { cz q2,q0; u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; }
gate c28b1 q0,q1,q2 { cz q1,q0; u3(pi/2,0,-pi) q1; cz q2,q0; }
gate c29b7 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; }
gate c30b1 q0,q1,q2 { cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,pi/2,pi/2) q2; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,pi/2,-pi) q1; }
gate c31b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(1.2981783,0,pi/2) q0; u3(pi/2,-pi,0) q1; }
gate c32b5 q0,q1,q2 { cz q2,q0; u3(pi/2,pi/2,-pi/2) q0; cz q0,q1; u3(pi/2,-pi,-pi) q0; u3(0,3*pi/4,pi/4) q1; cz q2,q0; u3(pi/2,pi/2,pi/2) q0; cz q2,q1; u3(0,0,pi/2) q2; u3(pi/2,pi/2,pi/2) q1; }
gate c33b3 q0,q1,q2 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(0,-2.9773793,1.406583) q1; cz q1,q2; u3(pi/2,0,-pi/2) q1; u3(pi/2,0,pi/2) q2; cz q1,q2; u3(0,-pi,-pi/2) q1; u3(pi/2,-pi,-pi) q2; }
gate c34b1 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,-pi,-pi) q1; }
gate c35b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,pi/2,-pi) q0; u3(pi/2,-pi,-pi) q1; }
gate c36b5 q0,q1,q2 { cz q1,q2; cz q0,q2; u3(pi/2,pi/2,pi/2) q2; }
gate c37b7 q0,q1,q2 { cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(2.4672204,-pi,pi/2) q2; }
gate c38b6 q0,q1,q2 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,-pi,-pi/2) q2; }
gate c39b3 q0,q1,q2 { cz q2,q0; u3(pi/2,pi/2,pi/2) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,-pi/2,0) q1; u3(2.4293402,-pi,-pi/2) q2; }
gate c40b0 q0,q1 { cz q0,q1; u3(pi/2,-pi/2,0) q0; u3(pi/2,-pi/2,0) q1; }
gate c40b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(0,-0.5255596,2.0963559) q0; u3(pi/2,0,pi/2) q1; }
gate c41b6 q0,q1,q2 { cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(pi/2,pi/2,-pi) q0; u3(pi/2,-pi,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; }
gate c42b1 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,pi/2,-pi) q0; u3(0,-2.9773793,1.406583) q1; }
gate c43b0 q0,q1,q2 { cz q2,q1; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; }
gate c44b2 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q1,q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,-pi,-pi/2) q1; }
gate c45b0 q0,q1,q2 { cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q2,q1; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; cz q1,q2; u3(pi/2,pi/2,1.8112355) q1; u3(pi/2,0,-pi) q2; }
gate c46b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(0,-2.9773793,1.406583) q1; }
gate c47b1 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi/2) q1; u3(pi/2,0,pi/2) q2; cz q1,q2; u3(pi/2,0,-pi/2) q1; u3(0.77683878,0,-pi/2) q2; cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(0.77683878,-pi/2,-pi/2) q0; u3(0.13896194,-pi,-pi/2) q2; }
gate c48b7 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(0.89642407,0,pi/2) q0; u3(3.0467688,-pi,-pi/2) q1; }
gate c49b5 q0,q1,q2 { cz q1,q2; u3(pi/2,0,pi/2) q2; u3(pi/2,0,-pi/2) q1; cz q1,q2; u3(pi/2,0,pi/2) q2; u3(1.891378,-pi,-pi/2) q1; cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(0,-0.5255596,2.0963559) q0; u3(pi/2,0,pi/2) q2; }
gate c50b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(1.5710962,-pi,-pi/2) q0; u3(0,-2.9773793,1.406583) q1; }
gate c51b1 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(2.1807824,-pi,pi/2) q0; u3(0.00029984412,-pi/2,-pi/2) q1; }
gate c52b7 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(2.188225,0,pi/2) q0; u3(0.39311453,0,-pi/2) q1; }
gate c53b5 q0,q1,q2 { cz q1,q2; u3(pi/2,0,pi/2) q2; u3(pi/2,0,-pi/2) q1; cz q1,q2; u3(pi/2,0,pi/2) q2; u3(1.4982635,-pi,pi/2) q1; cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(2.3494934,-pi,pi/2) q0; u3(pi/2,0,pi/2) q2; }
gate c54b7 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi/2) q1; u3(pi/2,0,pi/2) q2; cz q1,q2; u3(1.6433291,0,-pi/2) q1; u3(1.6433291,-pi/2,pi/2) q2; cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; u3(pi/2,0,-pi) q2; }
gate c55b5 q0,q1 { cz q0,q1; u3(pi/2,0,pi/2) q1; u3(pi/2,0,-pi/2) q0; cz q0,q1; u3(pi/2,-pi,-pi) q1; u3(pi/2,pi/2,-pi) q0; }
gate c56b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(2.3628956,-pi/2,-pi/2) q0; u3(pi/2,0.23058494,0) q1; }
gate c57b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; }
gate c58b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q1,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,-pi) q1; }
gate c59b4 q0,q1 { cz q1,q0; u3(0,0,pi/2) q1; u3(pi/2,0,-pi) q0; }
gate c60b1 q0,q1,q2 { cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q2,q0; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; cz q0,q2; cz q1,q0; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q0; }
gate c61b3 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,-pi) q1; }
qreg q[10];
c0b0 q[0],q[1],q[4];
c0b5 q[3],q[7];
c1b7 q[5],q[6],q[9];
c2b3 q[2],q[3],q[6];
c3b7 q[6],q[9];
c4b8 q[8],q[9];
c5b5 q[6],q[7];
c6b7 q[5],q[6],q[9];
c7b4 q[2],q[5],q[6];
c8b5 q[6],q[7];
c9b1 q[1],q[2];
c10b3 q[2],q[3],q[6];
c11b0 q[0],q[1],q[4];
c12b6 q[4],q[5],q[8];
c13b1 q[1],q[2],q[5];
c14b4 q[5],q[6];
c15b5 q[6],q[7];
c16b7 q[5],q[6],q[9];
c17b6 q[4],q[5],q[8];
c18b0 q[0],q[4];
c18b5 q[3],q[6];
c19b7 q[5],q[6],q[9];
c20b3 q[2],q[6];
c21b8 q[5],q[8],q[9];
c22b2 q[4],q[5];
c23b0 q[0],q[1],q[4];
c24b2 q[1],q[4],q[5];
c25b0 q[0],q[4];
c26b6 q[4],q[8];
c27b0 q[0],q[1],q[4];
c28b1 q[1],q[2],q[5];
c29b7 q[5],q[9];
c30b1 q[1],q[2],q[5];
c31b3 q[2],q[3];
c32b5 q[3],q[6],q[7];
c33b3 q[2],q[3],q[6];
c34b1 q[2],q[5];
c35b3 q[2],q[3];
c36b5 q[3],q[6],q[7];
c37b7 q[5],q[6],q[9];
c38b6 q[4],q[5],q[8];
c39b3 q[2],q[3],q[6];
c40b0 q[1],q[4];
c40b5 q[3],q[7];
c41b6 q[4],q[5],q[8];
c42b1 q[1],q[2];
c43b0 q[0],q[1],q[4];
c44b2 q[4],q[5];
c45b0 q[0],q[1],q[4];
c46b3 q[2],q[3];
c47b1 q[1],q[2],q[5];
c48b7 q[6],q[9];
c49b5 q[3],q[6],q[7];
c50b3 q[2],q[3];
c51b1 q[2],q[5];
c52b7 q[6],q[9];
c53b5 q[3],q[6],q[7];
c54b7 q[5],q[6],q[9];
c55b5 q[6],q[7];
c56b3 q[2],q[3];
c57b5 q[3],q[7];
c58b3 q[2],q[3];
c59b4 q[5],q[6];
c60b1 q[1],q[2],q[5];
c61b3 q[2],q[6];
