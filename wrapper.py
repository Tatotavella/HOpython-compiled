import ctypes as C
math = C.CDLL('./src/libmymath.so')

def add_float(y1,y2):
    math.add_float.restype = C.c_float
    math.add_float.argtypes = [C.c_float, C.c_float]
    resu = math.add_float(y1,y2)
    return resu

def add_int(x1,x2):
    math.add_int.restype = C.c_int
    math.add_int.argtypes = [C.c_int, C.c_int]
    resu = math.add_int(x1,x2)
    return resu

def add_float_r(y1,y2):
    r = -1
    math.add_float_ref.restype = C.c_int
    y1_p = C.byref( C.c_float(y1))
    y2_p = C.byref( C.c_float(y2))
    r_p = C.byref( C.c_int(r))
    r = math.add_float_ref(y1_p, y2_p, r_p)
    resu = C.cast(r_p,C.POINTER(C.c_float))
    resu = resu.contents.value
    return (r,resu)

def add_int_r(x1,x2):
    r = -1
    math.add_int_ref.restype = C.c_int
    x1_p = C.byref( C.c_int(x1))
    x2_p = C.byref( C.c_int(x2))
    r_p = C.byref( C.c_int(r))
    r = math.add_int_ref(x1_p, x2_p, r_p)
    resu = C.cast(r_p,C.POINTER(C.c_int))
    resu = resu.contents.value
    return (r,resu)

