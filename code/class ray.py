class Ray:
    def __init__(self,l,m,n,x1=0,y1=0,z1=0):
        self.x1=x1
        self.y1=y1
        self.z1=z1
        self.l=l
        self.m=m
        self.n=n
        return (('x-',self.x1)/self.l,'=',('y-',self.y1)/self.m,'+',('z-',self.z1)/(self.n))
    def origin(self):
        return(self.x1,',',self.y1,',',self.z1)
    def direction(self):
        return('The direction ratios of the ray are: ',self.l,',',self.m,',',self.n)


b=Ray(2,3,4)
