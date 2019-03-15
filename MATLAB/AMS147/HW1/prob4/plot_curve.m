%
% Consider the non-linear equation exp(-x) - c - x = 0.
% Here "c" is a parameter in the equation. The root of the equation varies
% with "c" and thus the root is a function of "c". 
% The code "calc_data.m" calculates the root for "c" in [0,10] and 
% stores the data in data1.mat. 
% This code loads in data1.mat and plots the root as a function of "c".
%
clear
clf
axes ('position',[0.15,0.13,0.75,0.75])
%
load data1.mat
plot(c_v, r_v,'m-o','linewidth',1.0)
set(gca,'xtick',[-2:.5:2])
set(gca,'ytick',[-2:.1:2])
set(gca,'fontsize',14)
xlabel('c')
ylabel('r(c)')
title('The root of exp(x)-1.5 -cos(x+c) = 0')
%

