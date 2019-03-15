function [t w]=calc_sRK4(y0,h,q) 
%
% This code implements the classical four stage fourth order
% Runge Kutta method to solve an ODE system.
%
m=2;
nstep=150/h;
%
w=zeros(nstep+1,m);
t=zeros(nstep+1,1);
t(1)=0;
w(1,1:m)=y0;
%
p=4;
d=[0,   1/2, 1/2, 1  ];
c=[0,   0,   0,   0  ;
   1/2, 0,   0,   0  ;
   0,   1/2, 0,   0  ;
   0,   0,   1,   0  ];
b=[1/6, 1/3, 1/3, 1/6];
k=zeros(p,m);
%
for j=1:nstep,
  for i=1:p,
    k(i,1:m)=h*f_sys(w(j,1:m)+c(i,1:i-1)*k(1:i-1,1:m), t(j)+d(i)*h, q);
  end
  w(j+1,1:m)=w(j,1:m)+b*k;
  t(j+1)=t(j)+h;
end
%


