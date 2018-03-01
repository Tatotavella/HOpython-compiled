import class_wrap as cw
molecula_1 = cw.Particula(2.0,1,3,1,1.0,1,m = 20)
molecula_2 = cw.Particula()

print('\n')
print('Molecula 1')
print('m: %.2f' % (molecula_1.m))
print('x: %.2f, y: %.2f, z: %.2f' % (molecula_1.x,molecula_1.y,molecula_1.z))
print('vx: %.2f, vy: %.2f, vz: %.2f' % (molecula_1.vx,molecula_1.vy,molecula_1.vz))
print('fx: %.2f, fy: %.2f, fz: %.2f' % (molecula_1.fx,molecula_1.fy,molecula_1.fz))
print('rapidez: %.5f' % (molecula_1.rapidez())) 
print('\n')
print('Molecula 2')
print('m: %.2f' % (molecula_2.m))
print('x: %.2f, y: %.2f, z: %.2f' % (molecula_2.x,molecula_2.y,molecula_2.z))
print('vx: %.2f, vy: %.2f, vz: %.2f' % (molecula_2.vx,molecula_2.vy,molecula_2.vz))
print('fx: %.2f, fy: %.2f, fz: %.2f' % (molecula_2.fx,molecula_2.fy,molecula_2.fz))
print('rapidez: %.5f' % (molecula_2.rapidez())) 
print('\n')




