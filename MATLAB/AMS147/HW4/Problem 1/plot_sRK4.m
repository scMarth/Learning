%
clear all 
clc 
%
%Declarations
x0= [1.5,0]; % y(0), y'(0)
y0= [-1.5,3.0];
h = 0.05;
 [t x]=calc_sRK4(x0,h);
plot(t,x(:,1),'b-o') 
hold all
%Titles,labels, legend
xlabel('t'); 
ylabel('y(t)'); 
legend('Set 1');
title('Problem 1'); 


% use golden search to get a more precise answer
td=t;
yd=x(:,1);
%
a=0;
b=30;
tol=1.0e-10;
n=0;
%
g=(sqrt(5)-1)/2;
r1=a+(b-a)*(1-g);
f1=dd(r1,td,yd);
r2=a+(b-a)*g;
f2=dd(r2,td,yd);
%
while (b-a) > tol,
  n=n+1;
  if f1 < f2,
    b=r2;
    r2=r1;
    f2=f1;
    r1=a+(b-a)*(1-g);
    f1=dd(r1,td,yd);
  else
    a=r1;
    r1=r2;
    f1=f2;
    r2=a+(b-a)*g;
    f2=dd(r2,td,yd);
  end
end
T=(a+b)/2
%
figure
clf reset
axes('position',[0.15,0.13,0.75,0.75])
%
plot(td,yd,'bo','linewidth',2.0)
hold on
plot(td-T,yd,'rx','linewidth',2.0)
legend('y vs. t', 'y vs. t-T')
axis([0,20,-2.5,2.5])
set(gca,'fontsize',14)
set(gca,'xtick',[0:5:20])
set(gca,'ytick',[-2.0:1:2.0])
xlabel('t')
ylabel('y(t)')
title('Problem 1'); 
%
%


