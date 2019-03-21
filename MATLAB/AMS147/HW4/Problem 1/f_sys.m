function [z]=f_sys(w,t)
% 
z=zeros(1,2); 
u=w(1); % y(t)
v=w(2); % y'(t)
z(1)=v; 
z(2)= -sin(u);
%
