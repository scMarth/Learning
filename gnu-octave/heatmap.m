graphics_toolkit("gnuplot");

a1 = csvread("/home/vincent/github/Learning/gnu-octave/full.csv");

x = a1(:,1);
y = a1(:,2)
z = a1(:,3)
n = 256;
[X, Y] = meshgrid(linspace(min(x),max(x),n), linspace(min(y),max(y),n));
Z = griddata(x,y,z,X,Y);
%// Remove the NaNs for imshow:
Z(isnan(Z)) = 0;
imshow(Z);