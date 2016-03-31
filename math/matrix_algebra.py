import numpy as np
from numpy import linalg as la

# Matrix Algebra

A=np.matrix([[1,2,3],[2,7,4]])
B=np.matrix([[1,-1],[0,1]])
C=np.matrix([[5,-1],[9,1],[6,0]])
D=np.matrix([[3,-2,-1],[1,2,3]])
u=np.matrix([6,2,-3,5])
v=np.matrix([3,5,-1,4])
w=np.matrix([[1],[8],[0],[5]])

def pmat(N,M):
	print(N+":\n"+str(M)+"\n\n")

pmat('A',A)
pmat('B',B)
pmat('C',C)
pmat('D',D)
pmat('u',u)
pmat('w',w)

""" 1. Matrix Dimensions 
  1.1) A 2x3
  1.2) B 2x2
  1.3) C 3x2
  1.4) D 2x3
  1.5) u 1x4
  1.6) w 4x1
"""

def pdim(N,M):
	print("dimensions of "+N+" are "+str(M.shape)+"\n")

pdim('A',A)
pdim('B',B)
pdim('C',C)
pdim('D',D)
pdim('u',u)
pdim('w',w)


""" 2. Vector Operations
#  2.1) u+v=[9 7 -4 9] :digraphs <ctrl>k u-  v? (closest option)
#  2.2) u-v=[3 -3 -2 1] 
#  2.3) au=[6a 2a -3a 5a] //  a*
#  2.4) udotv=[18 10 3 20]  // .M 
#  2.5) |u|=rt(74)~8.60      // !2(big) PP(sm) RT ?2
"""

print ("u+v="+str(u+v)+"\n")
print ("u-v="+str(u-v)+"\n")
print ('2u='+str(2*u)+"\n")
print ('udotv='+str(np.multiply(u,v))+"\n")
print ('|u|='+str(la.norm(u))+"\n\n")


""" 3. Matrix Operations
  3.1) Not Def 
  3.2) 4 -7 -3, 3 6 4
  3.3) 14 3 3, 2 7 9
  3.4) -1 -5 -1, 2 7 4
  3.5) Not Def
  3.6) Not Def
  3.7) 5 -6, 9 -8, 6 -6
  3.8) 1 -4 0 1
  3.9) 14 28 28 68
  3.10) 10 -4 0, -4 8 8, 0 8 10
"""

print "A+C="
try:
	print str(A+C)+"\n\n"
except:
	print "ndef\n"
print "A-C'=\n"+str(A-np.transpose(C))+"\n"
print "C'+3D=\n"+str(np.transpose(C)+3*D)+"\n"
print "BA=\n"+str(B.dot(A))+"\n"
print "BA'="
try:
	print str(B.dot(np.transpose(A)))+"\n"
except:
	print "ndef\n"




