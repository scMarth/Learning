%
clear all 
clc 
%
%Declarations
x0= [0.7,0.7];
y0= [-1.5,3.0];
h = 0.05;
 [t x]=calc_sRK4(x0,h); 
 [t y]=calc_sRK4(y0,h); 
plot(x(:,1),x(:,2),'b-o') 
hold all 
plot(y(:,1),y(:,2),'m-x')  
%Titles,labels, legend
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('Set 1', 'Set 2');
title('Problem 5'); 

