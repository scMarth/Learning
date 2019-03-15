%
% Script used to plot y(t) vs. t
%
clear all
clc
clf reset
axes('position',[0.15,0.13,0.75,0.75])
%
%a=2;
y0=1;
h=0.1/16;
%
n=4/h;
t=[0:n]*h;
y=zeros(1,n+1);
y(1)=y0;
%
for j=1:n,
  y(j+1)=y(j)+h*(-sin(y(j)/2)+exp(cos(2*t(j))));
end
%
plot(t,y,'bo','linewidth',1.0)
hold on
%
set(gca,'fontsize',14)
xlabel('t')
ylabel('y(t)')
title('Problem 4')
legend('Numerical solution')
%
%
