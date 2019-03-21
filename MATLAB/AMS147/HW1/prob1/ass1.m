%
%This is to plot the functions( below), on one graph.
%f1(i)=sqrt((1+(2*x(i)))/(1+x(i)));  
%f2(i)=1+(1/2)*x(i)-(5/8)*x(i).^2+(13/15)*x(i).^3;
%
%CLEARING
%clears all the previous data
%clears all previously made functions

clear;  
clf;    

% DECLARATIONS
%create an array from 0-200 of zeros to populate, for x ,f1, and f2

n=200;
x=zeros(1,n);           
f1=zeros(1,n);          
f2=zeros(1,n);          
dx=.6/(n-1);

% EQUATIONS 
%Populate the arrays with points for the the functions to use
%declares the equations for f1 & f2

for i=1:n,
    x(i)=0+(i-1)*dx;
    f1(i)=sqrt((1+(2*x(i)))/(1+x(i))); 
    f2(i)=1+(1/2)*x(i)-(5/8)*x(i).^2+(13/15)*x(i).^3;   
end

% FUNCTIONS
%Plot the graphs using "hold all"
%setup the legand 

plot(x,f1,'k')
hold all
plot(x,f2,'g-o')
hold off
h1=legend('f1(x)=sqrt((1+(2*x(i)))/(1+x(i)))','f2(x)=1+(1/2)*x(i)-(5/8)*x(i).^2+(13/15)*x(i).^3');
set(h1,'fontsize',12)
%
