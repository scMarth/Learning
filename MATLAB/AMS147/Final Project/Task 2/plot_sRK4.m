
%
clear all 
close all
clc 
%
%Declarations
x0= [4,0]; % y(0), y'(0)

h = 0.031250000000000; % h is found from Task 1

axis_index = 1;
fig_num = 1;

for i=0.1:0.1:3, %i is u
%for i=.4,   
%for i = 2.7:2.7,
	% run calculation with h
	[t x]=calc_sRK4(x0,h,i); % q=i
    
    td=t(2241:3201);   % select interval t = [70,100]
    yd=x(2241:3201,1); % select interval t = [70,100]
    
    ind = 1;

    while yd(ind) <= 0, %find a positive part of the wave
        ind = ind + 1;
    end

    prev = yd(ind);
    while yd(ind)>= 0, %go to negative part of wave
        ind = ind + 1;
    end
    
    while yd(ind) <= prev, %find minimum
       prev = yd(ind);
       ind = ind + 1;
    end
    
    first_minimum = ind;
    
    while yd(ind) <= 0, %go to positive
       ind = ind + 1;
    end
    
    while yd(ind)>= 0, %go to negative part of wave
        ind = ind + 1;
    end
    
    prev = yd(ind-1);
    while yd(ind) <= prev, %find minimum
       prev = yd(ind);
       ind = ind + 1;
    end
    
    next_minimum = ind;
    period(axis_index) = td(next_minimum) - td(first_minimum);
    x_axis(axis_index) = i;
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Debug
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %figure(fig_num);
    %fig_num = fig_num + 1;
    
    %plot(td, yd,'b*');
    %hold on
    %plot(td-period(axis_index), yd,'m*');
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    axis_index = axis_index + 1;

    %
end

figure
 plot(x_axis, period);
% axis([0, 3.2, 3, 7]);
 xlabel('mu');
 ylabel('period of limit cycle');
 title('Task 2');