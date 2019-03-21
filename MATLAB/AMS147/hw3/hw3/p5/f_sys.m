function [z]=f_sys(w,t)
% 
z=zeros(1,2); 
u=w(1); 
v=w(2); 
z(1)=v; 
z(2)= .5*(1-u^2)*v - u;
%
