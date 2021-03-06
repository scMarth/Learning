%
% Consider the non-linear system
%   exp(u) - cos(v) + u - v - c = 0
%   exp(v) + sin(u) + v + u = 0
% This code calculates the root vector (u, v) for c = 10
%
clear
%
c=5.8;
r=[1 1]';
tol=1.0e-10;

j = 101;
u_array = zeros(1,j);
v_array = zeros(1,j);
c_array = zeros(1,j);

dc = 4.2/(j-1);
%

for i=1:j,
    c_array(i)=5.8+(i-1)*dc;
    [r, n]=newton_sys('g', 'fp_2', c_array(i), r, tol);
    u_array(i) = r(1);
    v_array(i) = r(2);
    % n is number of iterations, not used
end


plot(c_array, u_array, 'bo');
hold all
plot(c_array, v_array, 'ko');
axis([5.8, 10, .5, 1.2])
xlabel('c')
set(gca,'xtick',[5.8:0.5:10]);
legend('u(c)', 'v(c)');
title('Problem 1');
