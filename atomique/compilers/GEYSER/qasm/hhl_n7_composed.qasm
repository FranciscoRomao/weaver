OPENQASM 2.0;
include "qelib1.inc";
gate c0b1 q0,q1,q2 { u3(pi,-pi/2,-pi) q0; u3(pi/2,1.9018722,0) q1; u3(0.66826757,-pi/2,pi/2) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.9492828,-0.37848648) q0; u3(0,1.406583,-1.406583) q2; }
gate c1b3 q0,q1 { u3(pi/2,0.66826757,-pi) q1; cz q1,q0; u3(1.1407901,0.75006393,-0.37047558) q0; cz q1,q0; u3(pi/2,0,1.4307098) q1; u3(pi/2,-2.0008025,-2.3208603) q0; }
gate c2b4 q0,q1,q2 { u3(pi/2,-3.1118791,0) q0; u3(0.56487101,-pi/2,pi/2) q2; cz q1,q2; u3(pi,-0.93081111,-2.5016074) q1; u3(0.86001238,0,pi/2) q2; cz q1,q2; u3(pi/2,0,2.4308087) q1; u3(pi/2,0.49149092,-pi/2) q2; }
gate c3b1 q0,q1,q2 { cz q0,q2; u3(pi,-0.93081111,-2.5016074) q0; u3(1.4215679,0,pi/2) q2; cz q0,q2; u3(pi,2.21918,-2.3668688) q0; u3(1.4215679,pi/2,0) q2; cz q1,q2; u3(pi,-0.93081111,-2.5016074) q1; u3(0.29845685,0,pi/2) q2; cz q1,q2; u3(0,-1.7471272,0.020465019) q1; u3(0.29845685,-pi/2,-pi) q2; }
gate c4b2 q0,q1 { cz q0,q1; u3(0.59691369,0,pi/2) q1; u3(pi,-0.93081111,-2.5016074) q0; cz q0,q1; u3(2.1212419,-0.90871057,-0.74461534) q1; u3(0,1.8789743,0.31844849) q0; }
gate c5b3 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,0,0.668267450000000) q0; u3(pi/2,0,pi) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,0.32901271,-1.5293335) q2; }
gate c6b2 q0,q1,q2 { cz q2,q1; u3(pi/4,-pi/2,pi/2) q1; cz q2,q1; u3(0,1.406583,-1.406583) q2; u3(pi/4,pi/2,-pi/2) q1; cz q0,q1; u3(pi/8,-pi/2,pi/2) q1; cz q0,q1; u3(0,0,-pi/4) q0; u3(pi/8,pi/2,-pi/2) q1; cz q0,q2; u3(pi/4,-pi/2,pi/2) q2; cz q0,q2; u3(pi/2,0,-pi) q0; u3(pi/4,pi/2,-pi/2) q2; }
gate c7b4 q0,q1,q2 { cz q2,q0; u3(pi/16,-pi/2,pi/2) q0; cz q2,q0; u3(pi/2,-pi/16,-pi) q0; u3(0,0,-pi/8) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q1; cz q2,q0; u3(pi/8,-pi/2,pi/2) q0; cz q2,q0; u3(pi/8,pi/2,-pi/2) q0; u3(0,0,-pi/4) q2; }
gate c8b1 q0,q1,q2 { cz q1,q2; u3(pi/32,-pi/2,pi/2) q2; cz q1,q2; u3(0,0,-pi/16) q1; u3(pi/32,pi/2,-pi/2) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.406583,-1.406583) q2; }
gate c9b0 q0,q1,q2 { u3(1.2811182,0,-pi) q0; cz q1,q2; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q2,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q1,q2; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q2,q0; u3(0.078807054,0,0) q0; }
gate c10b4 q0,q1,q2 { cz q2,q1; u3(pi/4,-pi/2,pi/2) q1; cz q2,q1; u3(3*pi/4,-pi,-pi/2) q1; u3(0,1.406583,-1.406583) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,0,pi) q0; u3(0,1.406583,-1.406583) q2; }
gate c11b1 q0,q1,q2 { cz q1,q0; u3(pi/16,-pi/2,pi/2) q0; cz q1,q0; u3(pi/2,-pi/16,-pi) q0; u3(pi/2,-pi/2,-2.7718644) q1; cz q1,q2; u3(pi/2,-pi/2,pi/2) q1; u3(pi/2,-pi,0) q2; cz q1,q2; u3(3*pi/8,-pi,-pi/2) q1; u3(pi/2,-pi/2,-pi) q2; cz q1,q2; u3(pi/8,pi/2,-pi) q1; u3(0,1.4750737,-1.4521029) q2; }
gate c12b4 q0,q1,q2 { cz q1,q0; u3(pi/2,pi/4,-pi) q0; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(0,1.406583,-1.406583) q2; cz q1,q2; u3(0,1.406583,-1.406583) q1; u3(pi/4,pi/2,-pi/2) q2; }
gate c13b0 q0,q1,q2 { cz q1,q0; u3(0.10745405,0,0) q0; cz q2,q0; u3(0.059433054,-pi,-pi) q0; }
gate c14b1 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; cz q1,q2; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q2,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q2; cz q1,q2; u3(pi/2,0,pi) q2; }
gate c15b0 q0,q1,q2 { cz q1,q0; u3(0.037086754,-pi,-pi) q0; u3(pi/2,0,pi) q1; cz q2,q0; u3(1.4596621,0,-pi) q0; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,1.406583,-1.406583) q1; }
gate c16b2 q0,q1,q2 { cz q2,q0; u3(0.090469154,0,0) q0; cz q1,q0; u3(0.11644025,-pi,-pi) q0; }
gate c17b4 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(0,-1.3697623,1.3697623) q1; }
gate c18b2 q0,q1,q2 { cz q2,q0; u3(0.097611854,-pi,-pi) q0; u3(pi/2,0,pi) q2; cz q1,q0; u3(0.092056754,0,0) q0; }
gate c19b4 q0,q1 { cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q1; }
gate c20b2 q0,q1,q2 { cz q2,q0; u3(0.11154455,0,0) q0; cz q1,q0; u3(0.033985854,-pi,-pi) q0; }
gate c21b0 q0,q1,q2 { cz q0,q1; u3(0.049624054,-pi,-pi) q1; cz q2,q1; u3(0.10831795,0,0) q1; }
gate c22b2 q0,q1,q2 { cz q2,q0; u3(0.083772754,0,0) q0; cz q1,q0; u3(0.16223735,-pi,-pi) q0; }
gate c23b1 q0,q1 { cz q1,q0; u3(0.14683265,-pi,-pi) q0; }
gate c24b2 q0,q1,q2 { cz q1,q0; u3(0.084469154,0,0) q0; cz q2,q0; u3(0.10841315,0,0) q0; cz q1,q0; u3(0.048240054,-pi,-pi) q0; }
gate c25b0 q0,q1,q2 { cz q0,q1; u3(0.033623554,-pi,-pi) q1; cz q2,q1; u3(0.11157745,0,0) q1; u3(pi/2,pi/2,-1.6484773) q2; }
gate c26b2 q0,q1,q2 { cz q2,q0; u3(1.6588532,-1.5432989,0.30311408) q0; cz q0,q1; u3(pi/2,0,-pi/2) q0; u3(pi/2,0,pi/2) q1; cz q0,q1; u3(pi/2,-1.4931154,-pi) q0; u3(1.6614002,2.8384072,3.1132954) q1; }
gate c27b4 q0,q1 { cz q1,q0; u3(0.10838905,-pi,-pi) q0; u3(pi/2,0,pi) q1; }
gate c28b2 q0,q1,q2 { cz q0,q1; u3(0.090848554,0,0) q1; cz q2,q1; u3(0.11118865,0,0) q1; cz q0,q1; u3(0.036333354,-pi,-pi) q1; }
gate c29b0 q0,q1,q2 { cz q0,q2; u3(pi/2,-pi/2,-pi) q0; u3(0.055353654,-pi,-pi) q2; cz q1,q2; u3(0.10764895,0,0) q2; }
gate c30b2 q0,q1,q2 { cz q2,q1; u3(pi/2,0,pi) q2; u3(0.080853954,0,0) q1; cz q0,q1; u3(1.7718146,0,-pi) q1; cz q1,q2; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q2,q1; u3(pi/2,0,pi) q2; u3(pi/2,0,pi) q1; cz q1,q2; u3(0,1.406583,-1.406583) q2; u3(pi/2,0,pi) q1; }
gate c31b1 q0,q1,q2 { cz q1,q2; u3(pi/4,-pi/2,pi/2) q1; u3(pi/2,0,pi) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(0,1.406583,-1.406583) q1; }
gate c32b4 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c33b1 q0,q1 { cz q0,q1; u3(pi/4,pi/2,-pi/2) q1; cz q0,q1; u3(pi/2,-pi/2,-0.15514721) q0; u3(pi/4,-pi/4,pi/2) q1; }
gate c34b0 q0,q1,q2 { cz q0,q1; u3(pi/2,-pi/2,pi/2) q0; u3(pi/2,-pi,0) q1; cz q0,q1; u3(3*pi/8,-pi,-pi/2) q0; u3(pi/2,-pi/2,-pi) q1; cz q0,q1; u3(pi/2,-0.82660049,-pi/2) q0; u3(pi/2,0,-3*pi/8) q1; cz q0,q2; u3(pi/16,pi/2,-pi/2) q2; cz q0,q2; u3(0,0,pi/32) q0; u3(pi/16,-pi/2,pi/2) q2; }
gate c35b2 q0,q1,q2 { cz q2,q0; u3(pi/4,pi/2,-pi/2) q0; cz q2,q0; u3(3*pi/4,-pi/2,pi/2) q0; u3(0,0,pi/8) q2; cz q2,q1; u3(pi/8,pi/2,-pi/2) q1; cz q2,q1; u3(0,0,pi/16) q2; u3(pi/8,-pi/2,pi/2) q1; }
gate c36b0 q0,q1,q2 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,pi/4,pi/2) q0; u3(pi/2,0,pi) q1; cz q0,q2; u3(pi/4,pi/2,-pi/2) q2; cz q0,q2; u3(0,0,pi/8) q0; u3(pi/4,-pi/4,pi/2) q2; }
gate c37b1 q0,q1,q2 { cz q0,q1; u3(pi/32,pi/2,-pi/2) q1; cz q0,q1; u3(0,0,-0.668267500000000) q0; u3(pi/32,-pi/2,pi/2) q1; cz q2,q1; u3(pi/16,pi/2,-pi/2) q1; cz q2,q1; u3(pi/16,-pi/2,pi/2) q1; u3(pi/2,0,2.4733252) q2; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; }
gate c38b0 q0,q1,q2 { cz q0,q1; u3(pi/8,pi/2,-pi/2) q1; cz q0,q1; u3(0,0,-0.668267500000000) q0; u3(pi/8,-pi/2,pi/2) q1; cz q2,q1; u3(pi/4,pi/2,-pi/2) q1; cz q2,q1; u3(pi/4,-2.2390638,pi/2) q1; u3(0,0,-0.668267500000000) q2; }
gate c39b1 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,pi/2,0) q1; }
gate c41b3 q0,q1 { cz q0,q1; u3(0.59691369,0,pi/2) q1; u3(pi,-0.93081111,-2.5016074) q0; cz q0,q1; u3(0.59691369,-pi/2,-pi) q1; u3(0,-1.4136889,1.4850436) q0; }
gate c40b0 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,pi/2,-pi) q1; }
gate c42b2 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q1,q0; u3(pi/2,0,pi) q1; u3(pi/2,0,pi) q0; cz q0,q1; u3(pi/2,pi/2,0) q1; }
gate c43b3 q0,q1,q2 { cz q1,q2; u3(0.29845685,0,pi/2) q2; u3(pi,-0.93081111,-2.5016074) q1; cz q1,q2; u3(0.29845685,-0.37047558,-pi) q2; u3(pi/2,0,-1.2009852) q1; cz q0,q2; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q2,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q2; cz q0,q2; u3(pi/2,-1.2003207,-pi) q0; u3(pi/2,0,pi) q2; }
gate c44b1 q0,q1 { cz q0,q1; u3(pi,-0.93081111,-2.5016074) q0; u3(1.4215679,0,pi/2) q1; cz q0,q1; u3(pi,1.696251,0.3918135) q0; u3(1.4215679,pi/2,0) q1; }
gate c45b0 q0,q1 { cz q0,q1; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q1,q0; u3(pi/2,0,pi) q0; u3(pi/2,0,pi) q1; cz q0,q1; u3(pi/2,pi/2,0) q1; }
gate c46b1 q0,q1 { cz q0,q1; u3(pi,-0.93081111,-2.5016074) q0; u3(0.86001238,0,pi/2) q1; cz q0,q1; u3(pi/2,0,-0.58444387) q0; u3(0.86001238,-0.37047558,-pi) q1; }
gate c47b3 q0,q1 { cz q1,q0; u3(1.1407901,-0.75006393,0.37047558) q0; cz q1,q0; u3(2.5816674,0.90252885,-pi) q0; u3(pi/2,0,-1.5288845) q1; }
qreg q[7];
c0b1 q[1],q[2],q[4];
c1b3 q[4],q[5];
c2b4 q[3],q[4],q[6];
c3b1 q[1],q[2],q[4];
c4b2 q[3],q[4];
c5b3 q[2],q[4],q[5];
c6b2 q[1],q[3],q[4];
c7b4 q[3],q[4],q[6];
c8b1 q[1],q[2],q[4];
c9b0 q[0],q[1],q[3];
c10b4 q[3],q[4],q[6];
c11b1 q[1],q[2],q[4];
c12b4 q[3],q[4],q[6];
c13b0 q[0],q[1],q[3];
c14b1 q[1],q[2],q[4];
c15b0 q[0],q[1],q[3];
c16b2 q[1],q[3],q[4];
c17b4 q[4],q[6];
c18b2 q[1],q[3],q[4];
c19b4 q[4],q[6];
c20b2 q[1],q[3],q[4];
c21b0 q[0],q[1],q[3];
c22b2 q[1],q[3],q[4];
c23b1 q[1],q[2];
c24b2 q[1],q[3],q[4];
c25b0 q[0],q[1],q[3];
c26b2 q[1],q[3],q[4];
c27b4 q[3],q[6];
c28b2 q[1],q[3],q[4];
c29b0 q[0],q[1],q[3];
c30b2 q[1],q[3],q[4];
c31b1 q[1],q[2],q[4];
c32b4 q[4],q[6];
c33b1 q[1],q[4];
c34b0 q[0],q[1],q[3];
c35b2 q[1],q[3],q[4];
c36b0 q[0],q[1],q[3];
c37b1 q[1],q[2],q[4];
c38b0 q[0],q[1],q[3];
c39b1 q[1],q[4];
c41b3 q[4],q[5];
c40b0 q[0],q[1];
c42b2 q[3],q[4];
c43b3 q[2],q[4],q[5];
c44b1 q[1],q[2];
c45b0 q[0],q[1];
c46b1 q[1],q[2];
c47b3 q[2],q[5];
