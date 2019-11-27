# mathSimulations
  visualize some math
 some linear and multi currently

 * main library I use is matplotlib
 `quiver(headX, headY, dx, dy)`
  is nice for drawing vectors!

# misc cool stuff

  * sgn (  det (a, b) ) can tell you if b is counterclockwise rotated from a

  pf:
  consider vectors
  a, b
  and
  R_theta (a,b )  where R_theta is a rotation matrix

  turns out that 
  det ((a,b), R_theta(a,b))  = (a^2 + b^ 2) * sin(theta)

  sin(theta)  > 0 -> det > 0
  qed
