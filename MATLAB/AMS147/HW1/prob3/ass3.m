% plot points using data.txt as an import file and then create a best fit
% curve based on the points and the funtion f=cos(2*exp(c*x))

%CLEARING
%clears all the previous data
%clears all previously made functions
clc
clear
figure(3)
%
% call and load the file that you will use for data points
% assigning t the first column of the data and y as the other column
load -ascii data2.txt
t=data2(:,1);
y=data2(:,2);

%Plot the points and then run the function and plot the best fit line
plot(t,y,'b.');
hold all
% fit the data to the logistic population model
x=[0:0.01:1.7];
c=1.159;
y2=cos(2*exp(c*x));
%
plot(x,y2,'m');
%FUNCTION LAYOUT
xlabel('X'); 						%labels x-axis as X
ylabel('Y'); 						%labels y-axis as Y
title('Problem 3'); 					%gives our figure a title
h1=legend ('Data Points','Best Fit Line'); 	%makes legend
set(h1,'fontsize',13) 					%sets the font size in legend
hold off
%