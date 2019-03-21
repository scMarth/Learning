%
clear all 
clc 
%
%Declarations
x0= [3,0]; % y(0), y'(0)
h = 0.05;
 [t x]=calc_sRK4(x0,h,0.1); % q=0.1
 [t y]=calc_sRK4(x0,h,0.3); % q=0.3
 [t z]=calc_sRK4(x0,h,1);   % q=1
 [t w]=calc_sRK4(x0,h,3);   % q=3
 
%plot all on one figure
plot(x(:,1),x(:,2),'b-o') 
hold all 
plot(y(:,1),y(:,2),'g-+') 
plot(z(:,1),z(:,2),'c-*') 
plot(w(:,1),w(:,2),'m-x') 
%Titles,labels, legend
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('q=0.1', 'q=0.3', 'q=1', 'q=3');
title('Problem 6'); 
figure



plot(x(:,1),x(:,2),'b-o') 
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('q=0.1');
title('Problem 6'); 
figure
plot(y(:,1),y(:,2),'g-+') 
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('q=0.3');
title('Problem 6'); 
figure
plot(z(:,1),z(:,2),'c-*') 
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('q=1');
title('Problem 6'); 
figure
plot(w(:,1),w(:,2),'m-x') 
xlabel('y(t)'); 
ylabel('dy/dt'); 
legend('q=3');
title('Problem 6'); 

