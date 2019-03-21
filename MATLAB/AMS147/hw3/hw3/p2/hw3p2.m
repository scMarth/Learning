clear
clc

n = 10;
x_axis = zeros(1,n); %array for x-axis values
xaxis = zeros(1,n); %array for x-axis values

trap_error = zeros(1,n); %array for trapezoid error
simp_error = zeros(1,n); %array for simpson error

a = 1; b = 3;
%
for i=1:n,
    x_axis(i) = 2.^i;
    N = x_axis(i);
    h = (b-a)/N;
    x=a+[0:N]*h;
    y=f(x);

    %simpson rule with h
    x2=a+[0:N-1]*h+h/2;
    y2=f(x2);
    Tsimp1(i) =(y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*h/6;
    
    clear x;
    clear y;
    clear y2;

    N = x_axis(i);
    h = (b-a)/(2*N); %h/2
    N = (b-a)/h;
    x=a+[0:N]*h;
    y=f(x);

    %simpson rule with h/2
    x2=a+[0:N-1]*h+h/2;
    y2=f(x2);
    Tsimp2(i) =(y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*h/6;
    
    clear x;
    clear y;
    clear y2;

    N = x_axis(i);
    h = (b-a)/(4*N); %h/4
    N = (b-a)/h;
    x=a+[0:N]*h;
    y=f(x);

    %simpson rule with h/2
    x2=a+[0:N-1]*h+h/2;
    y2=f(x2);
    Tsimp3(i) =(y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*h/6;
    
    clear x;
    clear y;
    clear y2;
    
    %approximate order with p ~ [(T(h) - T(h/2))/(T(h/2) - T(h/4))]
    simp_order(i) = log2((Tsimp1(i) - Tsimp2(i))/(Tsimp2(i) - Tsimp3(i)));
    simp_error(i) = abs(Tsimp1(i) - Tsimp2(i));
end

semilogx(x_axis(1:8), simp_order(1:8), '-x');
%loglog(x_axis, simp_error);
legend('Order of Accuracy');
title('Problem 2');
ylabel('Order');
xlabel('N');