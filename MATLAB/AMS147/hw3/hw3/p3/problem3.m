clear
clc
%
a1 = 0; b1 = 1; %integral w.r.t. x from 0 to 1
a2 = 0; b2 = 1; %integral w.r.t. y from 0 to 1
%
iterations = 9;
%
first_approx = zeros(1,iterations);
second_approx = zeros(1,iterations);
error = zeros(1,iterations);
x_axis = zeros(1,iterations);
%
for k=1:iterations,
    N = 2^k;
    x_axis(k) = N;
    %
    h1 = 1/N; %x direction step size
    h2 = h1;  %y direction step size
    %
    x=a1+[0:N]*h1;
    x2=a2+[0:N]*h1+h1/2;
    %
    %calculate with step size h
    for i=1:N,
        s = a2+i*h2;
        y = f(x,s);
        y2= f(x2,s);
        first_approx(k) = ((y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*(h1*h2)/6) + first_approx(k);
    end
    %
    %calculate with step size h/2
    h1=h1/2;
    h2=h2/2;
    %
    %Use Z instead of N
    Z = 2^(k+1);
    %
    x_2=a1+[0:Z]*h1;
    x2_2=a2+[0:Z]*h1+h1/2;
    %
    for j=1:length(x_2),
        s_2 = a2+i*h2;
        y_2 = f(x_2,s_2);
        y2_2 =f(x2_2,s_2);
        second_approx(k) = ((y_2(1)+y_2(Z+1)+2*sum(y_2(2:Z))+4*sum(y2_2))*(h1*h2)/6) + second_approx(k);
    end
    %
    error(k) = abs(first_approx(k)-second_approx(k));
end
%
loglog(x_axis, error);
xlabel('N');
ylabel('Error');
legend('E(h) ~ T(h) - T(h/2)');
title('Problem 3');
%
disp(' ')
disp(['  The value of the double integral using N=2^9 using:'])
disp(['  step size h: ',num2str(first_approx(9), 7)])
disp(['  step size h/2: ',num2str(second_approx(9), 7)])
disp(' ')
