import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.A = A

 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        Shape.translate(self, dx, dy)

        self.A_P = self.A

        self.x_old = []
        self.y_old = []

        for i in self.A_P:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_old.append(i[0])
            self.y_old.append(i[1])

        self.A = np.matmul(self.A,self.T_t)
        
        self.x_new = []
        self.y_new = []
        for i in self.A:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_new.append(i[0])
            self.y_new.append(i[1])

        return self.x_new,self.y_new

    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        Shape.scale(self, sx, sy)

        self.A_P = self.A

        self.x_old = []
        self.y_old = []

        for i in self.A_P:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_old.append(i[0])
            self.y_old.append(i[1])
       
        self.A = np.matmul(self.A,self.T_s)
        
        self.x_new = []
        self.y_new = []
        for i in self.A:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_new.append(i[0])
            self.y_new.append(i[1])

        return self.x_new,self.y_new

 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        Shape.rotate(self, deg)

        self.A_P = self.A

        self.x_old = []
        self.y_old = []

        for i in self.A_P:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_old.append(i[0])
            self.y_old.append(i[1])
        
        self.A = np.matmul(self.A,self.T_r)
        
        self.x_new = []
        self.y_new = []
        for i in self.A:
            i[0] = round(i[0],2)
            i[1] = round(i[1],2)
            self.x_new.append(i[0])
            self.y_new.append(i[1])

        return self.x_new,self.y_new
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        plt.plot(self.x_old,self.y_old,linestyle = 'dashed')
        plt.plot(self.x_new,self.y_new)
        a = max(self.x_old)
        if max(self.x_new) > a:
            a = max(self.x_new)
        b = max(self.y_old)
        if max(self.y_new) > b:
            b = max(self.y_new)            
        Shape.plot(self,a + 3,b + 3)        


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.x_cord = x
        self.y_cord = y 
        self.r = radius

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        Shape.translate(self, dx, dy)

        self.x_cord_p = self.x_cord
        self.y_cord_p = self.y_cord
        self.r_p = self.r

        self.centre_old = []

        self.x_cord_p = round(self.x_cord_p,2)
        self.y_cord_p = round(self.y_cord_p,2)
        self.centre_old.append(self.x_cord_p)
        self.centre_old.append(self.y_cord_p)

        self.centre_old = tuple(self.centre_old)

        self.A = np.array([self.x_cord,self.y_cord,self.r])
        self.A = np.matmul(self.A,self.T_t)

        self.x_cord = self.A[0]
        self.y_cord = self.A[1]
        self.r = self.A[2]

        self.centre_new = [self.x_cord,self.y_cord]
        self.centre_new = tuple(self.centre_new)


        return self.x_cord,self.y_cord,self.r
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        Shape.scale(self, sx, sx) 

        self.T_s_c = self.T_s
        self.T_s_c[0][0] = 1
        self.T_s_c[1][1] = 1
        self.T_s_c[2][2] = sx   

        self.x_cord_p = self.x_cord
        self.y_cord_p = self.y_cord
        self.r_p = self.r

        self.centre_old = []

        self.x_cord_p = round(self.x_cord_p,2)
        self.y_cord_p = round(self.y_cord_p,2)
        self.centre_old.append(self.x_cord_p)
        self.centre_old.append(self.y_cord_p)

        self.centre_old = tuple(self.centre_old)

        self.A = np.array([self.x_cord,self.y_cord,self.r])
        self.A = np.matmul(self.A,self.T_s_c)

        self.x_cord = self.A[0]
        self.y_cord = self.A[1]
        self.r = self.A[2]

        self.centre_new = [self.x_cord,self.y_cord]
        self.centre_new = tuple(self.centre_new)

        return self.x_cord,self.y_cord,self.r
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        Shape.rotate(self,deg)
        
        self.x_cord_p = self.x_cord
        self.y_cord_p = self.y_cord
        self.r_p = self.r

        self.centre_old = []

        self.x_cord_p = round(self.x_cord_p,2)
        self.y_cord_p = round(self.y_cord_p,2)
        self.centre_old.append(self.x_cord_p)
        self.centre_old.append(self.y_cord_p)

        self.centre_old = tuple(self.centre_old)

        self.A = np.array([self.x_cord,self.y_cord,self.r])
        self.A = np.matmul(self.A,self.T_r)

        self.x_cord = self.A[0]
        self.y_cord = self.A[1]
        self.r = self.A[2]

        self.centre_new = [self.x_cord,self.y_cord]
        self.centre_new = tuple(self.centre_new)


        return self.x_cord,self.y_cord,self.r
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        circle_1 = plt.Circle(self.centre_old,self.r_p,fill = False,linestyle='--')
        circle_2 = plt.Circle(self.centre_new,self.r,fill = False)
        fig, ax = plt.subplots()
        ax.add_patch(circle_1)
        ax.add_patch(circle_2)
        ax.set(xlim=(-2, 2), ylim = (-2, 2))
        ax.set_aspect(1)
        a = self.r
        Shape.plot(self,a + 3,a + 3)


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    
    choice = int(input('Verbose? 1 to plot and 0 otherwise'))
    testcases = int(input('Enter the number of test cases'))
    if choice == 1:
        for i in range(testcases):
            shape = int(input('Enter the shape. o for polygon, 1 for circle.'))
            if shape == 0:
                sides = int(input('Enter the number of sides'))
                x,y=0,0
                A = []
                for j in range(sides):
                    x,y = input('Enter x,y coordinate.Space Seperated').split()
                    a = [x,y,1]
                    A.append(a)
                A = np.array(A)
                P = Polygon(A)
                Queries = int(input("Enter number of Queries."))
                for j in range(Queries):
                    q = input('Enter Query Space Separated.')
                    if q[0] == 'R':
                        if len(q) == 3:
                            deg = q[2]
                            P.rotate(deg)
                        elif len(q) == 5:
                            deg = q[2]
                            rx = q[4]
                            P.rotate(deg,rx)
                        else:
                            deg = q[2]
                            rx = q[4]
                            ry = q[-1]
                            P.rotate(deg,rx,ry)
                        P.plot()
                    elif q[0] == 'T':
                        if len(q) == 3:
                            dx = q[2]
                            P.translate(dx,dx)
                        else:
                            dx = q[2]
                            dy = q[-1]
                            P.translate(dx,dy)
                        P.plot()
                    elif q[0] == 'S':
                        if len(q) == 3:
                            sx = q[2]
                            P.scale(sx,sx)
                        else:
                            sx = q[2]
                            sy = q[-1]
                            P.scale(sx,sy)
                        P.plot()
                    elif q[0] == P:
                        None
            elif shape == 1:
                x,y,r = input('Enter centre(x,y) and radius .Space Seperated').split()
                C = Circle(x,y,r)
                Queries = int(input("Enter number of Queries."))
                for j in range(Queries):
                    q = input('Enter Query Space Separated.')
                    if q[0] == 'R':
                        if len(q) == 3:
                            deg = q[2]
                            C.rotate(deg)
                        elif len(q) == 5:
                            deg = q[2]
                            rx = q[4]
                            C.rotate(deg,rx)
                        else:
                            deg = q[2]
                            rx = q[4]
                            ry = q[-1]
                            C.rotate(deg,rx,ry)
                        C.plot()
                    elif q[0] == 'T':
                        if len(q) == 3:
                            dx = q[2]
                            C.translate(dx,dx)
                        else:
                            dx = q[2]
                            dy = q[-1]
                            C.translate(dx,dy)
                        C.plot()
                    elif q[0] == 'S':
                        if len(q) == 3:
                            sx = q[2]
                            C.scale(sx)
                        C.plot()
                    elif q[0] == P:
                        None
    elif choice == 0:
        for i in range(testcases):
            shape = int(input('Enter the shape. o for polygon, 1 for circle.'))
            if shape == 0:
                sides = int(input('Enter the number of sides'))
                x,y=0,0
                A = []
                for j in range(sides):
                    x,y = input('Enter x,y coordinate.Space Seperated').split()
                    a = [x,y,1]
                    A.append(a)
                A = np.array(A)
                P = Polygon(A)
                Queries = int(input("Enter number of Queries."))
                for j in range(Queries):
                    q = input('Enter Query Space Separated.')
                    if q[0] == 'R':
                        if len(q) == 3:
                            deg = q[2]
                            x_c,y_c = P.rotate(deg)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        elif len(q) == 5:
                            deg = q[2]
                            rx = q[4]
                            x_c,y_c = P.rotate(deg,rx)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        else:
                            deg = q[2]
                            rx = q[4]
                            ry = q[-1]
                            x_c,y_c = P.rotate(deg,rx,ry)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        
                    elif q[0] == 'T':
                        if len(q) == 3:
                            dx = q[2]
                            x_c,y_c = P.translate(dx,dx)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        else:
                            dx = q[2]
                            dy = q[-1]
                            x_c,y_c = P.translate(dx,dy)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        
                    elif q[0] == 'S':
                        if len(q) == 3:
                            sx = q[2]
                            x_c,y_c = P.scale(sx,sx)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        else:
                            sx = q[2]
                            sy = q[-1]
                            x_c,y_c = P.scale(sx,sy)
                            for a in x_c:
                                print(a,end=' ')
                            print()
                            for a in y_c:
                                print(a,end=' ')
                            print()
                        
                    elif q[0] == P:
                        None
            elif shape == 1:
                x,y,r = input('Enter centre(x,y) and radius .Space Seperated').split()
                C = Circle(x,y,r)
                Queries = int(input("Enter number of Queries."))
                for j in range(Queries):
                    q = input('Enter Query Space Separated.')
                    if q[0] == 'R':
                        if len(q) == 3:
                            deg = q[2]
                            x_c,y_c,r_ = C.rotate(deg)
                            print(x_c,y_c,r_)
                        elif len(q) == 5:
                            deg = q[2]
                            rx = q[4]
                            x_c,y_c,r_ = C.rotate(deg,rx)
                            print(x_c,y_c,r_)
                        else:
                            deg = q[2]
                            rx = q[4]
                            ry = q[-1]
                            x_c,y_c,r_ = C.rotate(deg,rx,ry)
                            print(x_c,y_c,r_)
                    elif q[0] == 'T':
                        if len(q) == 3:
                            dx = q[2]
                            x_c,y_c,r_ = C.translate(dx,dx)
                            print(x_c,y_c,r_)
                        else:
                            dx = q[2]
                            dy = q[-1]
                            x_c,y_c,r_ = C.translate(dx,dy)
                            print(x_c,y_c,r_)
                    elif q[0] == 'S':
                        if len(q) == 3:
                            sx = q[2]
                            x_c,y_c,r_ = C.scale(sx)
                            print(x_c,y_c,r_)





'''p1 = Polygon([[1,2,1],[3,4,1],[5,6,1]])
a,b = p1.translate(1,1)
print(a)
print(b)'''
'''p1 = Polygon(np.array([[0,0,1],[3,0,1],[3,3,1],[0,3,1]]))
p1.scale(2,2)
p1.plot()'''

'''c1 = Circle(0,0,5)
c1.scale(9)
c1.rotate(45)
c1.plot()'''