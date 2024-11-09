OPENQASM 2.0;
include "qelib1.inc";
gate c0b0 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; u3(0,1.406583,-1.406583) q2; }
gate c0b6 q0,q1,q2 { u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; }
gate c0b9 q0,q1,q2 { u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,pi) q2; }
gate c0b39 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; }
gate c0b69 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q2; u3(0,1.406583,-1.406583) q1; }
gate c0b64 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q2; u3(0,1.406583,-1.406583) q1; }
gate c0b72 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q2; u3(0,1.406583,-1.406583) q1; }
gate c0b42 q0,q1,q2 { u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,pi) q2; }
gate c1b1 q0,q1 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c1b20 q0,q1 { u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; }
gate c1b23 q0,q1,q2 { u3(0,1.406583,-1.406583) q1; u3(pi,-1.7350097,1.406583) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c1b65 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; u3(0,1.406583,-1.406583) q2; }
gate c1b62 q0,q1 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c1b56 q0,q1 { u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c2b55 q0 { u3(0,1.406583,-1.406583) q0; }
gate c2b38 q0,q1,q2 { u3(pi/2,0,pi) q2; u3(0,1.406583,-1.406583) q1; cz q2,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q2; }
gate c2b7 q0,q1 { u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c2b46 q0,q1 { u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c2b16 q0,q1 { u3(pi/2,0,pi) q1; u3(0,1.406583,-1.406583) q0; }
gate c3b24 q0,q1 { u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,pi) q0; }
gate c4b13 q0,q1 { u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c4b22 q0,q1 { cz q0,q1; u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c5b47 q0 { u3(pi/2,0,pi) q0; }
gate c5b7 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c6b21 q0,q1,q2 { cz q0,q2; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q2; cz q1,q2; u3(0,1.406583,-1.406583) q1; u3(0,1.406583,-1.406583) q2; }
gate c7b33 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c8b20 q0,q1 { cz q0,q1; u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c8b12 q0,q1 { cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(0,1.406583,-1.406583) q0; }
gate c9b5 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c9b24 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c10b10 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c11b19 q0,q1 { cz q0,q1; u3(0,1.406583,-1.406583) q0; u3(0,1.406583,-1.406583) q1; }
gate c12b5 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c13b22 q0,q1,q2 { cz q2,q1; u3(0,1.406583,-1.406583) q2; u3(0,1.406583,-1.406583) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c14b24 q0,q1 { cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q0; }
gate c15b26 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; }
gate c16b33 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c17b36 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c18b33 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c19b24 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c20b33 q0,q1,q2 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; cz q2,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q2; }
gate c21b47 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c22b20 q0,q1 { cz q0,q1; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,pi) q0; }
gate c23b33 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c24b20 q0,q1,q2 { cz q0,q2; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q2; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; }
gate c25b17 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c26b29 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c27b43 q0,q1,q2 { cz q2,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q2; cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c28b42 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c29b30 q0,q1,q2 { cz q0,q2; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q2; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; }
qreg q[50];
c0b0 q[0],q[1],q[8];
c0b6 q[3],q[10],q[11];
c0b9 q[5],q[6],q[13];
c0b39 q[22],q[23],q[30];
c0b69 q[39],q[46],q[47];
c0b64 q[36],q[43],q[44];
c0b72 q[41],q[48],q[49];
c0b42 q[24],q[25],q[32];
c1b1 q[2],q[9];
c1b20 q[18],q[19];
c1b23 q[13],q[14],q[21];
c1b65 q[37],q[38],q[45];
c1b62 q[35],q[42];
c1b56 q[33],q[40];
c2b55 q[31];
c2b38 q[21],q[28],q[29];
c2b7 q[4],q[12];
c2b46 q[26],q[34];
c2b16 q[16],q[17];
c3b24 q[20],q[21];
c4b13 q[7],q[15];
c4b22 q[12],q[20];
c5b47 q[27];
c5b7 q[5],q[12];
c6b21 q[12],q[13],q[20];
c7b33 q[19],q[20];
c8b20 q[11],q[19];
c8b12 q[13],q[14];
c9b5 q[4],q[11];
c9b24 q[20],q[21];
c10b10 q[12],q[13];
c11b19 q[11],q[19];
c12b5 q[3],q[11];
c13b22 q[12],q[19],q[20];
c14b24 q[20],q[21];
c15b26 q[21],q[22];
c16b33 q[19],q[20];
c17b36 q[20],q[28];
c18b33 q[19],q[20];
c19b24 q[20],q[21];
c20b33 q[19],q[20],q[27];
c21b47 q[27],q[35];
c22b20 q[18],q[19];
c23b33 q[19],q[27];
c24b20 q[11],q[18],q[19];
c25b17 q[10],q[18];
c26b29 q[18],q[25];
c27b43 q[25],q[26],q[33];
c28b42 q[25],q[32];
c29b30 q[17],q[24],q[25];
