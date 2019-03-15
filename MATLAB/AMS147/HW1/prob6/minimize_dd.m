%
% This code first reads in data (x, y) from data2.txt.
% Then it uses the golden search method to find the value of c
% such that the distance between the data and the function
% f(x)=exp(-c*x) is minimized.
% Finally, it plots the data along with the best fit.
%
clear
clf reset
axes('position',[0.15,0.15,0.75,0.70])
%
load -ascii data2.txt
x=data2(:,1);
y=data2(:,2);
%
a=0.5;
b=1.5;
tol=1.0e-10;
n=0;
%
g=(sqrt(5)-1)/2;
r1=a+(b-a)*(1-g);
f1=dd(r1,x,y);
r2=a+(b-a)*g;
f2=dd(r2,x,y);
%
while (b-a) > tol,
  n=n+1;
  if f1 < f2,
    b=r2;
    r2=r1;
    f2=f1;
    r1=a+(b-a)*(1-g);
    f1=dd(r1,x,y);
  else
    a=r1;
    r1=r2;
    f1=f2;
    r2=a+(b-a)*g;
    f2=dd(r2,x,y);
  end
end
c0=(a+b)/2;
c_result = vpa(((a+b)/2), 10)
fx=cos(2*exp(c0*x));

plot(x,fx,'b-','linewidth',2.0)
hold all
plot(x,y,'ko','markerfacecolor',[0.5,0.5,0.5])
axis([0.5,1.5,0,1.1])
set(gca,'xtick',[0.5:0.5:1.5])
set(gca,'ytick',[0:0.2:1.1])
set(gca,'fontsize',14)
xlabel('x')
ylabel('y')
title(['Best fit: c = 1.17016997'])
h1=legend('f(x)=cos(2*exp(c*x))','data');
set(h1,'fontsize',14)
%
%
