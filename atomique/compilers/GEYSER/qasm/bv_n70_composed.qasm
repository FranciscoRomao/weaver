OPENQASM 2.0;
include "qelib1.inc";
gate ccz q0,q1,q2 { h q2; ccx q0,q1,q2; h q2; }
gate c4b7 q0 { u3(pi/2,0,-pi) q0; }
gate c0b0 q0,q1,q2 { u3(pi/2,-pi,-pi) q0; u3(0,1.406583,-1.406583) q1; u3(0,pi/2,-pi/2) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c0b6 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q2; u3(0,1.406583,-1.406583) q1; }
gate c0b9 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(0,pi/2,-pi/2) q1; u3(pi/2,0,-pi) q2; }
gate c1b14 q0,q1,q2 { u3(0,pi/2,-pi/2) q0; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; }
gate c2b15 q0,q1 { u3(pi/2,0,-pi) q0; u3(0,pi/2,-pi/2) q1; }
gate c4b16 q0 { u3(0,pi/2,-pi/2) q0; }
gate c1b21 q0,q1 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c3b39 q0,q1 { u3(0,pi/2,-pi/2) q0; u3(pi/2,0,-pi) q1; }
gate c2b48 q0 { u3(0,1.406583,-1.406583) q0; }
gate c0b43 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(0,pi/2,-pi/2) q1; u3(pi/2,0,-pi) q2; }
gate c1b47 q0,q1 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c0b50 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q2; u3(0,1.406583,-1.406583) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; }
gate c2b54 q0 { u3(0,1.406583,-1.406583) q0; }
gate c0b53 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; u3(0,pi/2,-pi/2) q2; }
gate c1b58 q0,q1,q2 { u3(0,1.9492828,2.7631062) q0; u3(0,1.9492828,2.7631062) q2; u3(0,pi/2,-pi/2) q1; }
gate c0b63 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; }
gate c3b84 q0 { u3(pi/2,0,-pi) q0; }
gate c1b80 q0,q1,q2 { u3(0,pi/2,-pi/2) q0; u3(0,1.406583,-1.406583) q1; u3(0,pi/2,-pi/2) q2; }
gate c0b87 q0,q1,q2 { u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; u3(pi/2,0,-pi) q2; }
gate c1b93 q0,q1,q2 { u3(pi/2,pi/2,-pi) q0; u3(0,pi/2,-pi/2) q1; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,pi/2,-pi/2) q2; }
gate c2b95 q0 { u3(0,pi/2,-pi/2) q0; }
gate c2b98 q0,q1 { u3(0,pi/2,-pi/2) q0; u3(0,pi/2,-pi/2) q1; }
gate c0b100 q0,q1,q2 { u3(0,pi/2,-pi/2) q0; u3(pi/2,0,-pi) q2; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(0,1.406583,-1.406583) q2; }
gate c0b108 q0,q1,q2 { u3(0,pi/2,-pi/2) q0; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(0,pi/2,-pi/2) q2; u3(pi/2,0,pi) q1; }
gate c1b1 q0,q1,q2 { u3(0,1.406583,-1.406583) q1; u3(0,pi/2,-pi/2) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c2b10 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c5b34 q0,q1 { u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(0,-1.3697623,1.3697623) q1; }
gate c2b75 q0,q1,q2 { u3(0,0,-pi/2) q0; u3(pi/2,pi/2,-pi) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,-pi/2,pi/2) q1; }
gate c1b99 q0,q1 { u3(0,pi/2,-pi/2) q0; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c1b106 q0,q1,q2 { u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,pi) q1; }
gate c3b0 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c2b3 q0,q1,q2 { cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; cz q0,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c4b91 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,-pi/2,-pi) q1; }
gate c3b61 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c3b108 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c2b104 q0,q1,q2 { u3(0,pi/2,-pi/2) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(0,pi/2,-pi/2) q2; }
gate c3b19 q0,q1,q2 { u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; cz q0,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0.43955587,0,-pi/2) q1; }
gate c6b79 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c5b89 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,pi/2,-1.3716219) q0; u3(pi/2,0,pi) q1; }
gate c3b87 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c4b36 q0,q1 { u3(0,1.406583,-1.406583) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c4b85 q0,q1 { u3(pi/2,0,-pi) q0; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c6b51 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,-pi/2,2.0081162) q1; }
gate c5b83 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,pi/2,-0.43731989) q0; u3(pi/2,-pi/2,pi/2) q1; }
gate c7b68 q0,q1,q2 { cz q0,q2; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q2; cz q0,q2; u3(2.7042728,pi/2,-pi/2) q0; u3(1.1334764,-pi/2,pi/2) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c9b51 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,1.406583,-1.406583) q1; }
gate c8b83 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi/2) q0; u3(pi/2,0,pi) q1; }
gate c9b72 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,-pi/2,0.46756028) q1; }
gate c10b74 q0,q1 { cz q0,q1; u3(pi/2,0,pi/2) q1; u3(pi/2,0,-pi/2) q0; cz q0,q1; u3(pi/2,2.6740324,-pi) q1; u3(pi/2,-1.7699707,-pi) q0; }
gate c11b73 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,pi) q1; }
gate c12b90 q0,q1,q2 { cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(0,-1.406583,1.406583) q0; u3(pi/2,0,-pi) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c13b92 q0,q1,q2 { cz q2,q1; u3(pi/2,0,-pi) q2; u3(0,1.406583,-1.406583) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c14b78 q0,q1,q2 { cz q2,q1; u3(pi/2,0,-pi) q2; u3(0,1.406583,-1.406583) q1; cz q0,q1; u3(pi/2,0,-pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c15b89 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c16b75 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c17b59 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c18b73 q0,q1,q2 { cz q2,q1; u3(pi/2,-pi/2,-2.889125) q1; u3(pi/2,0,-pi) q2; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(0.25246764,pi/2,pi/2) q0; u3(pi,1.1071487,-2.0344439) q1; }
gate c19b74 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c20b85 q0,q1,q2 { cz q2,q1; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,-pi) q2; cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,-pi) q1; }
gate c21b74 q0,q1 { cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(2.4405348,-pi,-pi/2) q0; u3(pi/2,0,pi) q1; }
gate c22b57 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,2.4405348,-pi) q0; u3(0,1.7681919,-1.7681919) q1; }
gate c23b44 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,pi/2,1.014817) q2; u3(pi/2,0,pi) q1; }
gate c25b42 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; }
gate c24b30 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(0.437406,-pi,-pi/2) q1; }
gate c26b43 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,-1.014817,-pi) q0; u3(0.437406,-pi/2,-pi/2) q1; }
gate c25b13 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi/2) q0; u3(pi/2,0,pi) q1; }
gate c27b30 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c28b41 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q2,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q2; cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c29b25 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,pi) q1; }
gate c30b39 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,1.406583,-1.406583) q1; }
gate c31b40 q0,q1,q2 { cz q1,q2; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(2.3642782,0,-pi/2) q0; u3(pi/2,0,pi) q2; }
gate c32b51 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,0,pi/2) q0; u3(0.17586863,0,-pi/2) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,pi/2,-pi/2) q2; }
gate c33b40 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(1.746665,-pi/2,-pi/2) q0; u3(pi/2,-0.77731448,-pi) q1; }
gate c35b51 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(0,1.406583,-1.406583) q1; }
gate c34b23 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi/2) q0; u3(pi/2,-pi/2,pi/2) q1; }
gate c36b35 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi/2) q0; u3(pi/2,0,pi) q1; }
gate c37b51 q0,q1 { cz q0,q1; u3(pi/2,pi/2,-pi/2) q0; u3(pi/2,0,-pi) q1; }
gate c39b36 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(1.2958419,0,-pi/2) q1; u3(0,0,pi/2) q0; }
gate c38b37 q0,q1,q2 { cz q2,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q1,q2; u3(pi/2,0,pi) q1; u3(pi/2,pi/2,-pi/2) q2; cz q0,q1; u3(0,0,pi/2) q0; u3(0,1.406583,-1.406583) q1; }
gate c39b23 q0,q1,q2 { u3(3.1376445,3.2198029,5.5306526) q0; u3(1.692572,4.8031269,5.5696117) q1; u3(0.088062743,5.7444632,4.1734212) q2; ccz q0,q2,q1; u3(0.05399282,2.4442613,3.2875472) q0; u3(3.1319894,4.8284126,1.432603) q1; u3(0.012356734,4.8120712,2.3484084) q2; ccz q0,q1,q2; u3(1.6249686,3.1303086,2.8711216) q0; u3(1.4472975,0.72025708,1.3816014) q1; u3(6.2738933,5.7691788,5.4257245) q2; }
gate c40b24 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,pi/2,-pi/2) q1; u3(3.1086847,-pi,pi/2) q0; }
gate c41b35 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(1.2958419,-pi/2,-pi/2) q0; u3(pi/2,0.032907927,-pi) q1; }
gate c42b49 q0,q1 { cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,-pi) q1; }
gate c43b35 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(2.2315481,0,-pi/2) q0; u3(pi/2,0,pi) q1; }
gate c44b19 q0,q1 { cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,2.2315481,0) q0; u3(1.1312405,pi/2,-pi/2) q1; }
gate c45b5 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,pi) q1; }
gate c46b19 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi/2) q0; u3(0,1.406583,-1.406583) q1; }
gate c47b33 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; }
gate c48b34 q0,q1 { cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,pi/2,-pi/2) q1; }
gate c49b20 q0,q1,q2 { cz q1,q2; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,-pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; }
gate c50b3 q0,q1,q2 { cz q1,q2; u3(pi/2,0,-pi) q1; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,-pi) q0; u3(0,1.406583,-1.406583) q2; }
gate c51b4 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; }
gate c52b1 q0,q1 { cz q0,q1; u3(pi/2,0,-pi) q0; u3(pi/2,0,pi) q1; }
qreg q[70];
c4b7 q[4];
c0b0 q[0],q[1],q[9];
c0b6 q[3],q[11],q[12];
c0b9 q[5],q[6],q[14];
c1b14 q[7],q[15],q[16];
c2b15 q[8],q[17];
c4b16 q[18];
c1b21 q[13],q[21];
c3b39 q[22],q[23];
c2b48 q[27];
c0b43 q[24],q[25],q[33];
c1b47 q[26],q[34];
c0b50 q[28],q[36],q[37];
c2b54 q[38];
c0b53 q[30],q[31],q[39];
c1b58 q[32],q[40],q[41];
c0b63 q[35],q[43],q[44];
c3b84 q[47];
c1b80 q[45],q[46],q[54];
c0b87 q[49],q[50],q[58];
c1b93 q[52],q[53],q[61];
c2b95 q[62];
c2b98 q[55],q[63];
c0b100 q[56],q[64],q[65];
c0b108 q[60],q[68],q[69];
c1b1 q[1],q[2],q[10];
c2b10 q[5],q[13];
c5b34 q[19],q[27];
c2b75 q[42],q[43],q[51];
c1b99 q[57],q[65];
c1b106 q[59],q[67],q[68];
c3b0 q[0],q[1];
c2b3 q[2],q[3],q[11];
c4b91 q[51],q[52];
c3b61 q[35],q[43];
c3b108 q[60],q[68];
c2b104 q[58],q[66],q[67];
c3b19 q[11],q[12],q[20];
c6b79 q[44],q[52];
c5b89 q[50],q[51];
c3b87 q[49],q[58];
c4b36 q[20],q[29];
c4b85 q[48],q[49];
c6b51 q[29],q[38];
c5b83 q[47],q[48];
c7b68 q[38],q[46],q[47];
c9b51 q[30],q[38];
c8b83 q[47],q[48];
c9b72 q[48],q[49];
c10b74 q[49],q[50];
c11b73 q[42],q[50];
c12b90 q[50],q[58],q[59];
c13b92 q[51],q[59],q[60];
c14b78 q[43],q[51],q[52];
c15b89 q[51],q[59];
c16b75 q[42],q[51];
c17b59 q[34],q[42];
c18b73 q[41],q[42],q[50];
c19b74 q[41],q[49];
c20b85 q[48],q[49],q[57];
c21b74 q[41],q[49];
c22b57 q[32],q[41];
c23b44 q[24],q[32],q[33];
c25b42 q[31],q[32];
c24b30 q[16],q[24];
c26b43 q[24],q[33];
c25b13 q[8],q[16];
c27b30 q[16],q[24];
c28b41 q[23],q[24],q[32];
c29b25 q[15],q[23];
c30b39 q[23],q[31];
c31b40 q[22],q[30],q[31];
c32b51 q[29],q[30],q[38];
c33b40 q[22],q[30];
c35b51 q[29],q[30];
c34b23 q[14],q[22];
c36b35 q[20],q[29];
c37b51 q[29],q[30];
c39b36 q[28],q[29];
c38b37 q[21],q[22],q[30];
c39b23 q[13],q[14],q[22];
c40b24 q[21],q[22];
c41b35 q[21],q[29];
c42b49 q[29],q[37];
c43b35 q[20],q[29];
c44b19 q[12],q[20];
c45b5 q[4],q[12];
c46b19 q[12],q[20];
c47b33 q[19],q[20];
c48b34 q[19],q[27];
c49b20 q[11],q[19],q[20];
c50b3 q[2],q[3],q[11];
c51b4 q[10],q[11];
c52b1 q[1],q[10];
