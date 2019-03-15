%
% This code first reads in data (x, y) from data2.txt.
% Then it uses the golden search method to find the value of c
% such that the distance between the data and the function
% f(x)=exp(-c*x) is minimized. 
% It estimates the standard deviation of noise.
% Finally, it plots the data along with the best fit.
%
clear
figure(1)
clf reset
axes('position',[0.16,0.16,0.72,0.70])
%
load -ascii data2.txt
x=data2(:,1);
y=data2(:,2);
%
a=0;
b=2;
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
c0=(a+b)/2;   % optimal value of c
N=size(y,1);
noise_std=dd(r2,x,y)/sqrt(N); % standard deviation of noise
disp('   optimal c    Standard deviation of noise')
disp([c0, noise_std])
%
fx=cos(2*exp(c0*x));
plot(x,fx,'b-','linewidth',2.0)
hold all
plot(x,y,'ko','markerfacecolor',[0.5,0.5,0.5])
axis([-.1,1.9,-1.5,1.3])
set(gca,'xtick',[-.05:0.5:3])
set(gca,'ytick',[-1.5:0.2:1.1])
set(gca,'fontsize',16)
xlabel('x')
ylabel('y')
title(['Best fit: c = ',num2str(c0,8)])
h1=legend('f(x)=cos(2*exp(c*x))','data');
set(h1,'fontsize',16)
%
%
