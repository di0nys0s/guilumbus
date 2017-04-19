import numpy as np
import matplotlib.pyplot as plt
import os
xmax=6
zmax=6
x=np.arange(-xmax,xmax,0.1)
z=np.arange(-zmax,zmax,0.1)
orbc1s=np.zeros((len(x),len(z)))
orbc2s=np.zeros((len(x),len(z)))
orbc3s=np.zeros((len(x),len(z)))
orbc2px=np.zeros((len(x),len(z)))
orbc2py=np.zeros((len(x),len(z)))
orbc2pz=np.zeros((len(x),len(z)))
orbc3px=np.zeros((len(x),len(z)))
orbc3py=np.zeros((len(x),len(z)))
orbc3pz=np.zeros((len(x),len(z)))
orbc3s=np.zeros((len(x),len(z)))
orbO1_1s=np.zeros((len(x),len(z)))
orbO1_2s=np.zeros((len(x),len(z)))
orbO1_3s=np.zeros((len(x),len(z)))
orbO1_2px=np.zeros((len(x),len(z)))
orbO1_2py=np.zeros((len(x),len(z)))
orbO1_2pz=np.zeros((len(x),len(z)))
orbO1_3px=np.zeros((len(x),len(z)))
orbO1_3py=np.zeros((len(x),len(z)))
orbO1_3pz=np.zeros((len(x),len(z)))


orbO2_1s=np.zeros((len(x),len(z)))
orbO2_2s=np.zeros((len(x),len(z)))
orbO2_3s=np.zeros((len(x),len(z)))
orbO2_2px=np.zeros((len(x),len(z)))
orbO2_2py=np.zeros((len(x),len(z)))
orbO2_2pz=np.zeros((len(x),len(z)))
orbO2_3px=np.zeros((len(x),len(z)))
orbO2_3py=np.zeros((len(x),len(z)))
orbO2_3pz=np.zeros((len(x),len(z)))

MO1=np.zeros((len(x),len(z)))
MO2=np.zeros((len(x),len(z)))
MO=np.zeros((27,len(x),len(z)))
mocoeff=np.zeros((27,27))

fname='mocoef_scf.sp'
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]
norb=0
morb=0
ncont=10
while morb<27:
 while norb<27:
  for number in content[ncont].split():
    mocoeff[morb][norb]=number
    norb=norb+1
  ncont=ncont+1
 morb=morb+1
 norb=0
#pos=1
#dpos=19
#mocoeff[0][0]=content[10][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][1]=content[10][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][2]=content[10][pos:pos+dpos]
#pos=pos+dpos
#print(content[10][pos:])
#mocoeff[0][3]=content[10][pos:]

#pos=1
#mocoeff[0][4]=content[11][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][5]=content[11][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][6]=content[11][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][7]=content[11][pos:]
#
#pos=1
#mocoeff[0][8]=content[12][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][9]=content[12][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][10]=content[12][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][11]=content[12][pos:]
#
#pos=1
#mocoeff[0][12]=content[13][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][13]=content[13][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][14]=content[13][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][15]=content[13][pos:]
#
#pos=1
#mocoeff[0][16]=content[14][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][17]=content[14][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][18]=content[14][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][dpos]=content[14][pos:]
#pos=pos+dpos
#
#pos=1
#mocoeff[0][20]=content[15][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][21]=content[15][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][22]=content[15][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][23]=content[15][pos:]
#pos=pos+dpos
#
#pos=1
#mocoeff[0][24]=content[16][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][25]=content[16][pos:pos+dpos]
#pos=pos+dpos
#mocoeff[0][26]=content[16][pos:]

# TODO read the argosls as defined here :
#https://www.univie.ac.at/columbus/docs_COL70/documentation_main.html

print(str(mocoeff[1]))

gridX=np.zeros((len(x),len(z)))
gridZ=np.zeros((len(x),len(z)))
r=0
for nx in range(len(x)):
    for nz in range(len(z)):
        r=np.sqrt(x[nx]**2.0+z[nz]**2.0)
        gridX[nx,nz]=x[nx]
        gridZ[nx,nz]=z[nz]
        orbc1s[nx,nz]=1.8347002E-03*np.exp(-3047.525*r**2)+1.4037301E-02*np.exp(
-457.3695*r**2)+6.8842606E-02*np.exp(-103.9487*r**2)+0.2321844*np.exp(-29.21016*
r**2)+0.4679413*np.exp(-9.286663*r**2)+0.3623120*np.exp(-3.163927*r**2)
        orbc2s[nx,nz]=-0.1193324*np.exp(-7.868272*r**2)-0.1608542*np.exp(-1.8812
88*r**2)+1.143456*np.exp(-0.5442493*r**2)
        orbc3s[nx,nz]=np.exp(-0.1687144*r**2)
        orbc2px[nx,nz]=6.8999096E-02*np.exp(-7.868272*r**2)+0.3164240*np.exp(-1.
881288*r**2)+0.7443083*np.exp(-0.5442493*r**2)*x[nx]
        orbc2pz[nx,nz]=6.8999096E-02*np.exp(-7.868272*r**2)+0.3164240*np.exp(-1.
881288*r**2)+0.7443083*np.exp(-0.5442493*r**2)*z[nz]
        orbc3px[nx,nz]=np.exp(-0.1687144*r**2)*x[nx]
        orbc3pz[nx,nz]=np.exp(-0.1687144*r**2)*z[nz]
        orbc3s[nx,nz]=1.8310998E-03*np.exp(-5484.672*r**2)+1.3950099E-02*np.exp(
-825.2350*r**2)+6.8445093E-0*np.exp(-188.0470*r**2)+0.2327143*np.exp(-52.96450*r
**2)+0.4701930*np.exp(-16.89757*r**2)+0.3585209*np.exp(-5.799635*r**2)
        rO1=np.sqrt(x[nx]**2.0+(z[nz]+2.19208232)**2.0)
        orbO1_1s[nx,nz]=1.8310998E-03*np.exp(-5484.672*rO1**2)+1.3950099E-02*np.
exp(-825.2350*rO1**2)+6.8445093E-02*np.exp(-188.0470*rO1**2)+0.2327143*np.exp(-5
2.96450*rO1**2)+0.4701930*np.exp(-16.89757*rO1**2)+0.3585209*np.exp(-5.799635*rO
1**2)
        orbO1_2s[nx,nz]=-0.1107775*np.exp(-15.53962*rO1**2)-0.1480263*np.exp(-3.
599934*rO1**2)+1.130767*np.exp(-1.013762*rO1**2)
        orbO1_3s[nx,nz]=np.exp(-0.2700058*rO1**2)
        orbO1_2px[nx,nz]=7.0874300E-02*np.exp(-15.53962*rO1**2)+0.3397528*np.exp
(-3.599934*rO1**2)+0.7271586*np.exp(-1.013762*rO1**2)*x[nx]
        orbO1_2pz[nx,nz]=7.0874300E-02*np.exp(-15.53962*rO1**2)+0.3397528*np.exp
(-3.599934*rO1**2)+0.7271586*np.exp(-1.013762*rO1**2)*(z[nz]+2.19208232)
        orbO1_3px[nx,nz]=np.exp(-0.2700058*rO1**2)*x[nx]
        orbO1_3pz[nx,nz]=np.exp(-0.2700058*rO1**2)*(z[nz]+2.19208232)

        rO2=np.sqrt(x[nx]**2.0+(z[nz]-2.19208232)**2.0)
        orbO2_1s[nx,nz]=1.8310998E-03*np.exp(-5484.672*rO2**2)+1.3950099E-02*np.
exp(-825.2350*rO2**2)+6.8445093E-02*np.exp(-188.0470*rO2**2)+0.2327143*np.exp(-5
2.96450*rO2**2)+0.4701930*np.exp(-16.89757*rO2**2)+0.3585209*np.exp(-5.799635*rO
2**2)
        #*np.exp(-*rO2**2)
        orbO2_2s[nx,nz]=-0.1107775*np.exp(-15.53962*rO2**2)-0.1480263*np.exp(-3.
599934*rO2**2)+1.130767*np.exp(-1.013762*rO2**2)
        orbO2_3s[nx,nz]=np.exp(-0.2700058*rO2**2)
        #*np.exp(-*rO1**2)
        orbO2_2px[nx,nz]=7.0874300E-02*np.exp(-15.53962*rO2**2)+0.3397528*np.exp
(-3.599934*rO2**2)+0.7271586*np.exp(-1.013762*rO2**2)*x[nx]
        orbO2_2pz[nx,nz]=7.0874300E-02*np.exp(-15.53962*rO2**2)+0.3397528*np.exp
(-3.599934*rO2**2)+0.7271586*np.exp(-1.013762*rO2**2)*(z[nz]-2.19208232)
        orbO2_3px[nx,nz]=np.exp(-0.2700058*rO2**2)*x[nx]
        orbO2_3pz[nx,nz]=np.exp(-0.2700058*rO2**2)*(z[nz]-2.19208232)
        MO1[nx,nz]=mocoeff[0][0]*orbc1s[nx,nz]+mocoeff[0][1]*orbc2s[nx,nz]+mocoe
ff[0][2]*orbc3s[nx,nz]+mocoeff[0][3]*orbc2px[nx,nz]+mocoeff[0][4]*orbc2py[nx,nz]
+mocoeff[0][5]*orbc2pz[nx,nz]+mocoeff[0][6]*orbc3px[nx,nz]+\
        mocoeff[0][7]*orbc3py[nx,nz]+\
        mocoeff[0][8]*orbc3pz[nx,nz]+\
        mocoeff[0][9]*orbO1_1s[nx,nz]+\
        mocoeff[0][10]*orbO1_2s[nx,nz]+\
        mocoeff[0][11]*orbO1_3s[nx,nz]+\
        mocoeff[0][12]*orbO1_2px[nx,nz]+\
        mocoeff[0][13]*orbO1_2py[nx,nz]+\
        mocoeff[0][14]*orbO1_2pz[nx,nz]+\
        mocoeff[0][15]*orbO1_3px[nx,nz]+\
        mocoeff[0][16]*orbO1_3py[nx,nz]+\
        mocoeff[0][17]*orbO1_3pz[nx,nz]+\
        mocoeff[0][18]*orbO2_1s[nx,nz]+\
        mocoeff[0][19]*orbO2_2s[nx,nz]+\
        mocoeff[0][20]*orbO2_3s[nx,nz]+\
        mocoeff[0][21]*orbO2_2px[nx,nz]+\
        mocoeff[0][22]*orbO2_2py[nx,nz]+\
        mocoeff[0][23]*orbO2_2pz[nx,nz]+\
        mocoeff[0][24]*orbO2_3px[nx,nz]+\
        mocoeff[0][25]*orbO2_3py[nx,nz]+\
        mocoeff[0][26]*orbO2_3pz[nx,nz]
        
        
        for n in range(27):
          MO[n,nx,nz]=mocoeff[n][0]*orbc1s[nx,nz]+mocoeff[n][1]*orbc2s[nx,nz]+mo
coeff[n][2]*orbc3s[nx,nz]+mocoeff[n][3]*orbc2px[nx,nz]+mocoeff[n][4]*orbc2py[nx,
nz]+mocoeff[n][5]*orbc2pz[nx,nz]+mocoeff[n][6]*orbc3px[nx,nz]+\
          mocoeff[n][7]*orbc3py[nx,nz]+\
          mocoeff[n][8]*orbc3pz[nx,nz]+\
          mocoeff[n][9]*orbO1_1s[nx,nz]+\
          mocoeff[n][10]*orbO1_2s[nx,nz]+\
          mocoeff[n][11]*orbO1_3s[nx,nz]+\
          mocoeff[n][12]*orbO1_2px[nx,nz]+\
          mocoeff[n][13]*orbO1_2py[nx,nz]+\
          mocoeff[n][14]*orbO1_2pz[nx,nz]+\
          mocoeff[n][15]*orbO1_3px[nx,nz]+\
          mocoeff[n][16]*orbO1_3py[nx,nz]+\
          mocoeff[n][17]*orbO1_3pz[nx,nz]+\
          mocoeff[n][18]*orbO2_1s[nx,nz]+\
          mocoeff[n][19]*orbO2_2s[nx,nz]+\
          mocoeff[n][20]*orbO2_3s[nx,nz]+\
          mocoeff[n][21]*orbO2_2px[nx,nz]+\
          mocoeff[n][22]*orbO2_2py[nx,nz]+\
          mocoeff[n][23]*orbO2_2pz[nx,nz]+\
          mocoeff[n][24]*orbO2_3px[nx,nz]+\
          mocoeff[n][25]*orbO2_3py[nx,nz]+\
          mocoeff[n][26]*orbO2_3pz[nx,nz]        
        


#*np.exp**(*r**2)
plt.contourf(gridX,gridZ ,orbc1s)
plt.savefig('orbc1s.png')
plt.contourf(gridX,gridZ ,orbc2s)
plt.savefig('orbc2s.png')
plt.contourf(gridX,gridZ ,orbc3s)
plt.savefig('orbc3s.png')
plt.contourf(gridX,gridZ ,orbc2px)
plt.savefig('orbc2px.png')
plt.contourf(gridX,gridZ ,orbc2pz)
plt.savefig('orbc2pz.png')
plt.contourf(gridX,gridZ ,orbc3px)
plt.savefig('orbc3px.png')
plt.contourf(gridX,gridZ ,orbc3pz)
plt.savefig('orbc3pz.png')
plt.contourf(gridX,gridZ ,orbO1_1s)
plt.savefig('orbO1_1s.png')
plt.contourf(gridX,gridZ ,orbO1_2s)
plt.savefig('orbO1_2s.png')
plt.contourf(gridX,gridZ ,orbO1_3s)
plt.savefig('orbO1_3s.png')
plt.contourf(gridX,gridZ ,orbO1_2px)
plt.savefig('orbO1_2px.png')
plt.contourf(gridX,gridZ ,orbO1_2pz)
plt.savefig('orbO1_2pz.png')
plt.contourf(gridX,gridZ ,orbO1_3px)
plt.savefig('orbO1_3px.png')
plt.contourf(gridX,gridZ ,orbO1_3pz)
plt.savefig('orbO1_3pz.png')
plt.contourf(gridX,gridZ ,orbO2_1s)
plt.savefig('orbO2_1s.png')
plt.contourf(gridX,gridZ ,orbO2_2s)
plt.savefig('orbO2_2s.png')
plt.contourf(gridX,gridZ ,orbO2_3s)
plt.savefig('orbO2_3s.png')
plt.contourf(gridX,gridZ ,orbO2_2px)
plt.savefig('orbO2_2px.png')
plt.contourf(gridX,gridZ ,orbO2_2pz)
plt.savefig('orbO2_2pz.png')
plt.contourf(gridX,gridZ ,orbO2_3px)
plt.savefig('orbO2_3px.png')
plt.contourf(gridX,gridZ ,orbO2_3pz)
plt.savefig('orbO2_3pz.png')
plt.contourf(gridX,gridZ ,MO1)
plt.savefig('orbMO1.png')
plt.contourf(gridX,gridZ ,MO2)
plt.savefig('orbMO2.png')
for n in range(27):
    plt.contourf(gridX,gridZ ,MO[n,:,:])
    plt.savefig('orbMO'+str(n)+'.png')
