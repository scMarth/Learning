clear
clc

n = 11;
trap = zeros(1,n); %array for trapezoid results
simp = zeros(1,n); %array for simpson results
x_axis = zeros(1,n); %array for x-axis values

trap_error = zeros(1,n); %array for trapezoid error
simp_error = zeros(1,n); %array for simpson error

a = 0; b = 5;

for i=1:n,
    x_axis(i) = 2.^i;
    N = x_axis(i);
    h = (b-a)/N;
    x=a+[0:N]*h;
    y=f(x);
    
    I=128*(sin(b/2) - sin(a/2));
    
    %trapezoid rule
    Ttrap(i)=(y(1)+y(N+1)+2*sum(y(2:N)))*h/2;
    trap_error(i) = abs(Ttrap(i) - I);
    
    %simpson rule
    x2=a+[0:N-1]*h+h/2;
    y2=f(x2);
    Tsimp(i)=(y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*h/6;
    simp_error(i) = abs(Tsimp(i) - I);
end

loglog(x_axis, trap_error);
hold all;
loglog(x_axis, simp_error);
legend('Trapezoidal rule error', 'Simpson''s rule error');
title('Problem 5');
ylabel('Error');
xlabel('N');
