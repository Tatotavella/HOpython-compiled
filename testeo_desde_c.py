import ctypes as C
# Importamos la libreria de C a la variables math
math = C.CDLL('./src/libmymath.so')
# Fijamos los tipos de datos de entrada y de salida de cada funcion
# add_float
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
# add_int
math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]
# add_float_ref
math.add_float_ref.restype = C.c_int
#math.add_float_ref.argtypes = [,]
# add_int_ref
math.add_int_ref.restype = C.c_int
#math.add_int_ref.argtypes = [,]

# Valores de variables de Python
x1_int = 3
x2_int = 7
y1_float = 4.1
y2_float = 5.3
r1_int = -1
r2_float = -1.0

# Pointers para usar como argumento en funciones de C
x1_p = C.byref( C.c_int(x1_int))
x2_p = C.byref( C.c_int(x2_int))
y1_p = C.byref( C.c_float(y1_float))
y2_p = C.byref( C.c_float(y2_float))
r1_p = C.byref( C.c_int(r1_int))
r2_p = C.byref( C.c_float(r2_float))

# Funciones con int y float directos
resu_int_dir = math.add_int(x1_int,x2_int) 
resu_float_dir = math.add_float(y1_float,y2_float)

# Funciones con referencia
resu1 = math.add_int_ref(x1_p, x2_p, r1_p)
resu2 = math.add_float_ref(y1_p, y2_p, r2_p)

# Casteo del resultado (Se puede hacer de una manera mucho mas directa, ver implementacion del wrapper)
resu_int_ref = C.cast(r1_p,C.POINTER(C.c_int))
resu_int_ref = resu_int_ref.contents.value
resu_float_ref = C.cast(r2_p,C.POINTER(C.c_float))
resu_float_ref = resu_float_ref.contents.value

print('\n')
print('Valores de Python Iniciales')
print('x1: %d | x2: %d | y1: %.2f | y2: %.2f | r1: %d | r2: %.2f' % (x1_int,x2_int,y1_float,y2_float,r1_int,r2_float))
print('\n')
print('Resultados con argumentos directos')
print('x1 + x2: %d' % (resu_int_dir))
print('y1 + y2: %f' % (resu_float_dir))
print('\n')
print('Resultados con argumentos por referencia')
print('x1 + x2: %d, r1: %d' % (resu_int_ref,resu1))
print('y1 + y2: %f, r2: %d' % (resu_float_ref,resu2))
print('\n')
print('Posiciones de memoria')
print(x1_p, x2_p, y1_p, y2_p, r1_p, r2_p)
print('\n')
