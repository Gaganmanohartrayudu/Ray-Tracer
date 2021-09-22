class Vec3:
    def __init__(self,x1=0,y1=0,z1=0):
        self.x1=x1
        self.y1=y1
        self.z1=z1
    def dotprod(self,v2):
        print((self.x1 * v2.x1) + (self.y1 * v2.y1) + (self.z1 * v2.z1))
    def crossprod(self,v3):
        self.x= (self.y1 * v3.z1) - (v3.y1 * self.y1)
        self.y= (v3.x1 * self.z1) - (v3.z1 * self.x1)
        self.z= (self.x1 * v3.y1) - (self.y1 * v3.x1)
        print('(',self.x,')(i)+(',self.y,')(j)+(',self.z,')(k)')
    def length(self):
        self.l=((self.x1)**2 + (self.y1)**2 + (self.z1)**2)**(0.5)
        print(self.l)
    def normalize(self):
        print('(',(self.x1/self.l),')(i)+(',(self.y1/self.l),')(j)+(',(self.z1/self.l),')(k)')

v1=Vec3(3,4,5)
v2=Vec3(2,3,4)
v1.dotprod(v2)
v1.crossprod(v2)
v1.length()
v1.normalize()



