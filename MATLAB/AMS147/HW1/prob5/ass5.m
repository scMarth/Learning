

clear all 
close all  
load data2.txt
x=data2(:,1); 
y=data2(:,2); 
c=linspace(0.5,1.5,200); %vector from 0 to 1 using 200 points 
dd=zeros(1,200); 
for i=1:1:length(c) %plugs in i for the values from 1 to 200 
 f=cos(2*exp(c(i)*x)); 
 dd(i)=norm(f-y); %sum of the distance between the points of the vectors 
end 
% 
plot(c,dd) 
xlabel('Parameter of c') 
ylabel('Sum of the distances between the function & data1') 
title('The Distances As We Vary c') 

%