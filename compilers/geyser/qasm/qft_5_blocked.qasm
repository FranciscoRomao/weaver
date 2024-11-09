OPENQASM 2.0;
include "qelib1.inc";
gate c0b1 q0,q1,q2 { u3(0,0,pi/4) q0; u3(0,1.406583,-1.406583) q1; u3(pi/2,0,-7*pi/8) q2; cz q0,q1; u3(pi/4,pi/2,-pi/2) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/4,-pi/2,pi/2) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,3*pi/4) q2; cz q0,q1; u3(pi/8,pi/2,-pi/2) q1; cz q0,q1; u3(0,0,pi/4) q0; u3(pi/2,pi/8,-pi) q1; cz q0,q2; u3(0,1.406583,-1.406583) q0; u3(pi/2,pi/4,-pi) q2; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(0,1.406583,-1.406583) q0; u3(pi/2,0,pi) q1; }
gate c1b2 q0,q1,q2 { u3(pi/2,0,-15*pi/16) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,7*pi/8) q1; cz q2,q0; u3(1*pi/16,pi/2,-pi/2) q0; cz q2,q0; u3(pi/2,pi/16,-pi) q0; u3(0,0,pi/8) q2; cz q2,q1; u3(pi/2,0,-3*pi/4) q2; u3(pi/2,pi/8,-pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.406583,-1.406583) q2; }
gate c2b0 q0,q1 { u3(pi/2,0,-3.0434179) q0; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,15*pi/16) q0; u3(pi/2,0,pi) q1; }
gate c3b1 q0,q1 { cz q0,q1; u3(pi/4,pi/2,-pi/2) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/4,-pi/2,pi/2) q1; }
gate c4b2 q0,q1 { cz q0,q1; u3(0.098174807,pi/2,-pi/2) q1; cz q0,q1; u3(pi/2,pi/32,-pi) q1; u3(0,0,pi/16) q0; }
gate c5b0 q0,q1 { cz q1,q0; u3(pi/2,pi/16,-pi) q0; u3(pi/2,0,-7*pi/8) q1; }
gate c6b2 q0,q1,q2 { cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,3*pi/4) q2; }
gate c7b1 q0,q1,q2 { cz q0,q1; u3(pi/8,pi/2,-pi/2) q1; cz q0,q1; u3(0,0,pi/4) q0; u3(pi/2,pi/8,-pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,pi/4,-pi) q2; }
qreg q[5];
c0b1 q[1],q[2],q[4];
c1b2 q[1],q[3],q[4];
c2b0 q[0],q[3];
c3b1 q[1],q[2];
c4b2 q[3],q[4];
c5b0 q[0],q[3];
c6b2 q[1],q[3],q[4];
c7b1 q[1],q[2],q[4];
