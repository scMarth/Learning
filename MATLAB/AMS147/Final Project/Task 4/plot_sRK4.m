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

dd1 = get_dist(h,x0,0.1);
dd2 = get_dist(h,x0,0.3);
dd3 = get_dist(h,x0,1);
dd4 = get_dist(h,x0,3);