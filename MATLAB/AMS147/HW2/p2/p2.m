clear;
clf;
clc;
%
n=81;
h=zeros(1,n);
e1=zeros(1,n);
e2=zeros(1,n);
e4=zeros(1,n);
dx=8/(n-1);
%
for i=1:n,
   temp=(i-1)*dx;
   h(i)=10.^(-temp);
   e1(i)=h(i)+(10.^(-8))/h(i);
   
   e2(i)=((h(i)).^2)+(10.^(-8))/h(i);
   e4(i)=((h(i)).^4)+(10.^(-8))/h(i);   
    
end
%
loglog(h, e1,'g','linewidth', 1.0);
hold all
loglog(h, e2,'linewidth', 2.0);
loglog(h, e4,'r','linewidth', 2.0);

xlabel('h')
legend('E1(h)', 'E2(h)', 'E4(h)');
title('Problem 2');
%
