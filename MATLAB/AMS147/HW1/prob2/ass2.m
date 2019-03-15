%
% f(i,j)=x(i,j)*sin(.5*x(i,j))-y(i,j)*sin(.5*y(i,j))
% for x in [-3,3] and y in [-4,4].
%
%CLEARING
%clears all the previous data
%clears all previously made functions
clear;
clf;

% DECLARATIONS
% create an array from 0-50 of zeros to populate, for x,y,and f
%
m=51;
n=51;
x=zeros(m,n);
y=zeros(m,n);
f=zeros(m,n);
dx=6/(n-1);
dy=8/(m-1);

% EQUATIONS 
% Populate the arrays with points for the the functions to use
% declares the equations for f1(i,j)

for i=1:m,
   for j=1:n,
      x(i,j)=-3+(j-1)*dx;
      y(i,j)=-4+(i-1)*dy;
      f(i,j)=x(i,j)*sin(.5*x(i,j))-y(i,j)*sin(.5*y(i,j));
   end
end

% FUNCTIONS
%Plot the graph using the surf funtion.
% lable the graph appropriately 
surf(x,y,f)
xlabel('x')
ylabel('y')
zlabel('f(x,y)')
%
title('Problem 3'); 					%gives our figure a title
