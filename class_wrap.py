import ctypes as C

atlib = C.CDLL('./src/libmyatom.so')
atlib.rapidez.argtypes = [C.Structure]
atlib.rapidez.restype = C.c_float

class Particula(C.Structure):
  _fields_ = [("x", C.c_float),
              ("y", C.c_float),
	      ("z", C.c_float),
              ("vx", C.c_float),
              ("vy", C.c_float),
	      ("vz", C.c_float),
              ("fx", C.c_float),
              ("fy", C.c_float),
	      ("fz", C.c_float),
              ("m", C.c_float)]

  def __init__(self, x = 0, y = 0, z = 0,
                     vx = 0, vy = 0, vz = 0,
                     fx = 0, fy = 0, fz = 0,
                     m = 1.0):
    self.x = x
    self.y = y
    self.z = z
    self.vx = vx
    self.vy = vy
    self.vz = vz
    self.fx = fx
    self.fy = fy
    self.fz = fz
    self.m = m
    
  def rapidez(self):
    return atlib.rapidez(self)
