import wrapper as w

x1 = 2
x2 = 3
y1 = 4.5
y2 = 6.3
r1 = -1
r2 = -1.0

resu_int_dir = w.add_int(x1,x2)
resu_float_dir = w.add_float(y1,y2)

aux_int = w.add_int_r(x1,x2)
resu1 = aux_int[0]
resu_int_ref = aux_int[1]

aux_float = w.add_float_r(y1,y2)
resu2 = aux_float[0]
resu_float_ref = aux_float[1]

print('\n')
print('Valores de Python Iniciales')
print('x1: %d | x2: %d | y1: %.2f | y2: %.2f | r1: %d | r2: %.2f' % (x1,x2,y1,y2,r1,r2))
print('\n')
print('Resultados con argumentos directos')
print('x1 + x2: %d' % (resu_int_dir))
print('y1 + y2: %f' % (resu_float_dir))
print('\n')
print('Resultados con argumentos por referencia')
print('x1 + x2: %d, r1: %d' % (resu_int_ref,resu1))
print('y1 + y2: %f, r2: %d' % (resu_float_ref,resu2))
print('\n')
 
