# point A
Ax = float(7)
Ay = (float(20)/float(3))

# point B
Bx = float(15)
By = float(20)

# point C
Cx = float(14)
Cy = float(14)

# find the slope from A to B
m = (Ay-By)/(Ax-Bx)

# solve for b in the equation y = mx + b
b = Ay - m * Ax

# find slope orthogonal to line AB
mp = -1 / m

# solve for b in the equation y = mpx + bp
bp = Cy + (1/m)*Cx

# find an x coordinate of point C orthogonally projected onto line AB
xp = (Ay - m*Ax - Cy + mp*Cx)/(mp-m)

# find the y coordinate of point C orthongonally projected onto line AB
yp = m*xp + Ay - m*Ax # (using equation for line AB)

print("Point A:")
print("\tx-coordinate: " + str(Ax))
print("\ty-coordinate: " + str(Ay))
print("")

print("Point B:")
print("\tx-coordinate: " + str(Bx))
print("\ty-coordinate: " + str(By))
print("")

print("Point C:")
print("\tx-coordinate: " + str(Cx))
print("\ty-coordinate: " + str(Cy))
print("")

print("Coordinates of Point C orthongonally projected onto line AB: ")
print("\tx-coordinate: " + str(xp))
print("\ty-coordinate: " + str(yp))





