#include <math.h>

struct _atom {
  float x, y, z;
  float vx, vy, vz;
  float fx, fy, fz;
  float m;
};

typedef struct _atom Particula;

float rapidez(Particula part) {
  float v_2 =  part.vx * part.vx + part.vy * part.vy + part.vz * part.vz;  
  return sqrt(v_2);
}
