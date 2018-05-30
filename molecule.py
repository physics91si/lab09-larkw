
# coding: utf-8

# In[2]:


import numpy as np
import particle as p


# In[7]:


class Molecule:
     """Create a molecule made of particle1 with Pos1 position(numpy array of\
 len 2) and M1 mass, and particle 2 with Pos2 position, M2 mass; their bond has spring constant k and equilibrium length L0"""

     def __init__(self, Pos1, Pos2, M1, M2, k, L0):
          self.p1 = p.Particle(Pos1, M1)
          self.p2 = p.Particle(Pos2, M2)
          self.k = k
          self.l = L0

     def get_disp(self):
          return np.array(self.p1.pos) - np.array(self.p2.pos)
    
     def get_force(self):
          """A function that calculates and returns the force on each particle from Hooke's Law, F = -kx """
          dir = np.linalg.norm(self.get_disp())
          mag = self.get_disp() - self.l
          f = (-1 * self.k) *  mag * dir
          return f
    
