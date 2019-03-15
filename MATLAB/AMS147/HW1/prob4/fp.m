function [y]=fp(x,c)
%
% This function calculates df(x)/dx for a given x and a parameter c.
%
y=sin(c+x)+exp(x);
%
