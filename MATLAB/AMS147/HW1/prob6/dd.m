function [dist]=dd(c,x,y)
%
% This function calculates the distance between the data
% and the function f(x)=cos(2*exp(c*x)
%
fx=cos(2*exp(c*x));
dist=norm(fx-y);
%
%
