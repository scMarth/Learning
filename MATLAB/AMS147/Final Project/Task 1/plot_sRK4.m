%
clear all 
clc 
%
%Declarations
x0= [4,0]; % y(0), y'(0)
%h = 0.05;

index = 1;

for i=3:9,
%for i=3,
	h = 1/(2^i);   
 
	% run calculation with h
	[t1 x1]=calc_sRK4(x0,h,3); % q=3

	% run calculation with h/2
	[t2 x2]=calc_sRK4(x0,h/2,3); % q=3

    norm_of_error(index) = (16/15)*norm(x1(length(x1)) - x2(length(x2)));
    x_axis(index) = h;
    
    index = index + 1;

end

loglog(x_axis, norm_of_error);
title('Task 1');
xlabel('h');
ylabel('2-norm of estimated error');
%axis([0, .126, 0, 0.4]);
