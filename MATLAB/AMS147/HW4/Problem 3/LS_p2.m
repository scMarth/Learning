clear
figure(1)
clf reset
clc
%
load data6.txt
x=data6(:,1);
y=data6(:,2);
%
g1=ones(size(x));
g2=x;
g3=x.^2;
g4=x.^3;
g5=x.^4;

% p2(x)
G=[g1, g2, g3];
%
GG=G'*G;
Gy=G'*y;
b=GG\Gy;
%
xp=[0:0.01:1];
g=b(1)+b(2)*xp+b(3)*xp.^2;

% p3(x)
G1=[g1, g2, g3, g4];
%
G1G1=G1'*G1;
G1y=G1'*y;
b=G1G1\G1y;
%
xp=[0:0.01:1];
g_1=b(1)+b(2)*xp+b(3)*xp.^2+b(4)*xp.^3;

% p4(x)
G2=[g1, g2, g3, g4, g5];
%
G2G2=G2'*G2;
G2y=G2'*y;
b=G2G2\G2y;
%
xp=[0:0.01:1];
g_2=b(1)+b(2)*xp+b(3)*xp.^2+b(4)*xp.^3+b(5)*xp.^4;
% Plot
plot(xp,g,'b-','linewidth',2.0)
hold all
plot(xp,g_1,'co-','linewidth',2.0)
plot(xp,g_2,'m-','linewidth',2.0)
plot(x,y,'ko','markerfacecolor',[0.5,0.5,0.5])
axis([0,1,-1.0,3.5])
set(gca,'xtick',[0:0.2:1])
set(gca,'ytick',[-1:1:3])
set(gca,'fontsize',14)
xlabel('x')
ylabel('y')
title('Problem 3')
legend('p^(^2^)(x)', 'p^(^3^)(x)', 'p^(^4^)(x)')
%

