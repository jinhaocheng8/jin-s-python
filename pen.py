
import matplotlib.pyplot as plt
import math


class Pen():
    """a drawing class like turtle"""
    def __init__(self, a=0, x=0, y=0, wdh=1, pup=True):
        self.a = a
        self.x = x
        self.y = y
        self.wdh = wdh
        self.pup = pup

    def goto(self, x, y):
        """go to point(x,y)and draw a line"""
        ax = plt.gca()
        ax.set_aspect('equal')
        wdh = self.wdh
        ax.plot([self.x, x], [self.y, y], linewidth=wdh,color='k')
        self.x = x
        self.y = y
        return self

    def gofd(self, n):
        """go along for a lenth of n,and draw a line"""
        c = self.a / 360 * 2 * math.pi
        nx = math.cos(c) * n
        ny = math.sin(c) * n
        x = self.x + nx
        y = self.y + ny
        
        self.goto(x, y)
        return self

    def rt(self, n):
        """turn right for a degree of n"""
        self.a -= n
        return self
    def lt(self, n):
        """turn left for a degree of n"""
        self.a += n
        return self
    def angle(self,n):
        """set the angle of n(0 degree points to the right)"""
        self.a = n
        return self

    def width(self, n):
        """set the width of n"""
        self.wdh = n
        return self

    def jpto(self, x, y):
        """go to point(x,y)"""
        self.x = x
        self.y = y
        return self

    def jpfd(self, n):
        """go along for a lenth of n"""
        c = self.a / 360 * 2 * math.pi
        nx = math.cos(c) * n
        ny = math.sin(c) * n
        x = self.x + nx
        y = self.y + ny
        self.jpto(x, y)
        return self

    

    
    def ls(self,w,r,a,n,l):
        """
        use L-system to draw fractal shapes(w is the start string of the L-system;
        r is a dicomnary,the value can replace the key in it;
        a is the angle of '+'and'-'of the L-system;n is the time it fractals;
        l is the lenth of each'F'.)
        """
        for i in range(n):
            for k,v in r.items():
                w = w.replace(k, v)
        arr = []
        
        for s in w:
            if s == 'F':
                self.gofd(l)
            elif s == '+':
                self.rt(a)
            elif s == '-':
                self.lt(a)
            elif s == '[':
                arr.append([self.x, self.y, self.a])
            elif s == ']':
                state = arr.pop()
                self.jpto(state[0], state[1])
                self.angle(state[2])  
        return self        
    def cir(self,r):
        """draw a circle that randium=r"""
        self.jpfd(r)
        
        self.lt(90)
        self.lt(360/1000)
        for i in range (1000):
            self.gofd(r*2*math.pi/1000)
            self.lt(360/1000)
        self.lt(90)
        self.jpfd(r)
        self.lt(180)
        return self
    def rect(self,a,b=None):
        """draw a rectangle that the side in front=a and the on-the-left one=b"""
        if not b:
            b=a    
        self.jpfd(b/2)
        self.lt(90)
        for i in range(2):
            self.gofd(a/2)
            self.lt(90)
            self.gofd(b)
            self.lt(90)
            self.gofd(a/2)
        self.lt(90)
        self.jpfd(b/2)
        self.rt(180)
        return self
        
        
        
        
        
        
            
    