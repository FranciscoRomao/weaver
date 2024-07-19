OPENQASM 2.0;
include "qelib1.inc";
gate c0b0 q0,q1,q2 { u3(pi/2,-pi,-pi) q0; u3(pi/2,0,pi) q1; u3(pi,3*pi/2,pi/2) q2; cz q2,q0; u3(pi/2,0,pi) q0; cz q2,q1; u3(pi/2,0,pi) q1; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/4,pi/2,-pi/2) q2; cz q1,q2; u3(pi/2,0,pi/2) q1; u3(pi/4,-pi/2,pi/2) q2; cz q0,q2; u3(pi/2,-pi/2,5*pi/4) q0; u3(pi/2,-3*pi/4,0) q2; cz q2,q1; u3(pi/2,-pi/2,-pi) q1; u3(pi/2,pi/2,pi) q2; cz q2,q1; u3(pi/2,-pi,pi/4) q1; u3(pi/2,-pi,-pi/2) q2; cz q0,q2; u3(pi/2,pi/4,-pi/2) q0; u3(pi,2.186276,2.9716742) q2; }
gate c1b1 q0,q1,q2 { u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q2; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c2b0 q0,q1,q2 { cz q0,q2; u3(pi/4,pi/2,-pi/2) q2; cz q1,q2; u3(pi/2,0,pi/2) q1; u3(pi/4,-pi/2,pi/2) q2; cz q0,q2; u3(pi/2,0,-3*pi/4) q0; u3(pi/2,-3*pi/4,0) q2; cz q2,q1; u3(pi/2,-pi/2,-pi) q1; u3(pi/2,pi/2,pi) q2; cz q2,q1; u3(pi/2,-pi,pi/4) q1; u3(pi/2,3*pi/2,pi/2) q2; cz q2,q0; u3(pi/4,pi/2,-pi/2) q0; u3(0,0,pi/4) q2; cz q2,q0; u3(pi/2,0,0) q0; u3(pi/2,0,pi) q2; cz q1,q2; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.406583,-1.406583) q2; cz q1,q2; u3(pi/2,0,pi) q2; }
qreg q[4];
c0b0 q[0],q[1],q[2];
c1b1 q[1],q[2],q[3];
c2b0 q[0],q[1],q[2];
