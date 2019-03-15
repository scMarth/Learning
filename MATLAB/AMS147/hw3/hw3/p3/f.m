function [z]=f(x, y);
%
% This function calculates f(x).
%
z=sqrt(exp(sin(x*pi - y*pi)) + exp(cos(x*y*pi)));
%