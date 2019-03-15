function [y]=g(s, x)
%
% This function calculates f(x).
%
y=log(5/2 + 2*cos((s*x)/2) - sin(s-1));
%
