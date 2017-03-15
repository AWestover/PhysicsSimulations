#Alek Westover
# graphics source code-http://mcsp.wartburg.edu/zelle/python/graphics.py
#you have to dig through the library if you want to understand a function
#little online help because graphics is an EXTENSION of tkinter o well... :(
#Fix pos and vel update(*dt)
                                                                            
import graphics as gr
import time
print(time.localtime()[3]%12)
import numpy as np
import random
print(np.sin(random.randint(0,3)))

screenDim=[1400,750]

win = gr.GraphWin('Physics Simulation', screenDim[0],screenDim[1])

fulcrumHeight=100
trP1=gr.Point(screenDim[0]/2,screenDim[1]/2)
trP2=gr.Point(screenDim[0]/2-fulcrumHeight/2,screenDim[1]/2+fulcrumHeight)
trP3=gr.Point(screenDim[0]/2+fulcrumHeight/2,screenDim[1]/2+fulcrumHeight)
triangle=gr.Polygon(trP1,trP2,trP3)
triangle.draw(win)
ground=gr.Line(gr.Point(screenDim[0]*0.15,screenDim[1]/2+fulcrumHeight),gr.Point(screenDim[0]*0.85,screenDim[1]/2+fulcrumHeight))
ground.setWidth(10)
ground.setFill("green")
ground.draw(win)

class Beam:
    def __init__(self,pos,th,angVel,angAcc,momentI,size,color):#pos is the midpoint
        self.pos=pos
        self.th=th
        self.angVel=angVel
        self.angAcc=angAcc
        self.momentI=momentI
        self.size=size
        self.color=color     
        leftBottomPt=gr.Point(self.pos[0]-self.size[1]*0.5*np.sin(self.th),self.pos[1]+self.size[1]*0.5*np.cos(self.th))
        rightTopPt=gr.Point(self.pos[0]+self.size[1]*0.5*np.sin(self.th),self.pos[1]-self.size[1]*0.5*np.cos(self.th))
        self.image=gr.Line(leftBottomPt,rightTopPt)
        
    def draw(self):
        self.image.setWidth(self.size[0])
        self.image.setFill(self.color)
        self.image.draw(win)
    
    def update(self,dt):
        critTh=np.arccos(2*fulcrumHeight/self.size[1])
        if((self.th<=(np.pi-critTh) or self.angAcc<=0) and (self.th>=critTh or self.angAcc>=0)):
            self.th+=self.angVel*dt
            self.angVel+=self.angAcc*dt
            leftBottomPt=gr.Point(self.pos[0]-self.size[1]*0.5*np.sin(self.th),self.pos[1]+self.size[1]*0.5*np.cos(self.th))
            rightTopPt=gr.Point(self.pos[0]+self.size[1]*0.5*np.sin(self.th),self.pos[1]-self.size[1]*0.5*np.cos(self.th))
            self.image.undraw()
            self.image=gr.Line(leftBottomPt,rightTopPt)
            self.draw()
        else:
            self.angVel=0
    
    def calculateATorque(self,f,pos2):
        dx=self.pos[0]-pos2[0]
        d= np.sqrt(dx**2+(self.pos[1]-pos2[1])**2)
        return(np.linalg.norm(f)*d*np.sin(self.th)*(-1*dx/abs(dx)))
        
    def applyNetTorque(self,t):
       self.angAcc=t/self.momentI
        
beam=Beam([screenDim[0]/2,screenDim[1]/2],np.pi/2,0,0,10000,[10,900],"black")
beam.draw()        

class BlobMass:
    def __init__(self,pos,vel,acc,mass,r,color):
        self.pos=pos
        self.vel=vel
        self.acc=acc
        self.mass=mass
        self.r=r
        self.color=color
        self.image=gr.Circle(gr.Point(self.pos[0],self.pos[1]),self.r)
        
    def draw(self):
        self.image.setFill(self.color)
        self.image.draw(win)   
        
    def update(self,dt):
        self.pos=np.sum((self.pos,np.multiply(self.vel,dt)),axis=0)
        self.vel=np.sum((self.vel,np.multiply(self.acc,dt)),axis=0)
        self.image.move(self.vel[0]*dt,self.vel[1]*dt)
        
    def applyNetForce(self,f):
        self.acc=[f[0]/self.mass,f[1]/self.mass]
        
bob= BlobMass([screenDim[0]/2+200,screenDim[1]/2.5],[0,0],[1,0],2000,20,"red")       
bob.draw()
joe= BlobMass([screenDim[0]/2-200,screenDim[1]/2.5],[0,0],[1,0],1500,15,"blue")       
joe.draw()
        
gravity=10000
dt=0.01#Pause time (kinda like the frame rate but not really. frame Period?)1Frame/0.01secs, so 100 frames/sec
playing=True
freeze=True

while playing==True:
    time.sleep(dt)
    rKey=win.checkKey()
    if(freeze==True):
        if(rKey=='s'):
            freeze=False
    if(freeze==False):
        
        fBobGravity=[0,bob.mass*gravity]
        fBobEngine=[0,0]
        fBobNormal=[0,0] 
        bobTorque=0
        
        if(abs(bob.pos[1]-screenDim[1]/2)<10 and abs(bob.pos[0]-beam.pos[0])<int(1.1*beam.size[1]/2)):
            if(rKey=='Left'):
                fBobEngine=[-100*bob.mass,0]
            elif(rKey=='Right'):
                fBobEngine=[bob.mass*100,0]
            elif(rKey=='Up'):
                fBobEngine=[0,-gravity*bob.mass*20]

            bobTorque=beam.calculateATorque(gravity*bob.mass,bob.pos)  

            if(bob.vel[1]>0):
                bob.vel[1]=0
        
            fBobNormal=[0,-1*bob.mass*gravity]
        
        bob.applyNetForce(np.sum((fBobEngine,fBobGravity,fBobNormal),axis=0))
        bob.update(dt)
        
        fJoeGravity=[0,gravity*joe.mass]
        fJoeEngine=[0,0]
        fJoeNormal=[0,0] 
        joeTorque=0
        
        #fix so that it says "if your basicly on the beam even if its slanted..." also normal force should be able to be prependicular to surface, not just always gravity. also add  friction
        if(abs(joe.pos[1]-screenDim[1]/2)<10 and abs(joe.pos[0]-beam.pos[0])<int(1.1*beam.size[1]/2)):
            if(rKey=='a'):
                fJoeEngine=[-100*bob.mass,0]
            elif(rKey=='d'):
                fJoeEngine=[100*bob.mass,0]
            elif(rKey=='w'):
                fJoeEngine=[0,-gravity*joe.mass*20]

            joeTorque=beam.calculateATorque(gravity*joe.mass,joe.pos) 

            if(joe.vel[1]>0):
                joe.vel[1]=0
            fJoeNormal=[0,-joe.mass*gravity]
        
        joe.applyNetForce(np.sum((fJoeEngine,fJoeGravity,fJoeNormal),axis=0))
        joe.update(dt)
        
        beam.applyNetTorque(bobTorque+joeTorque)
        beam.update(dt/130)
        
        if(rKey=='f'):
            freeze=True
        
    if(rKey=='e'):
        playing=False
            
    if(playing==False):
        win.close()    

