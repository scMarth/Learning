%
clear all 
clc 


A_start = 0.05;
A_end = 1.5;
A_step = 0.05;

A_count = (A_end - A_start) / A_step + 2;

A_array = zeros(1, int64(A_count)-1);
T_of_A = zeros(1, int64(A_count)-1);

for i=1:A_count,
    A_array(i) = 0.05 + (i-1)*0.05;
    
    %
    %Declarations
    x0= [A_array(i),0]; % y(0), y'(0)
    y0= [-1.5,3.0];
    h = 0.05;
     [t x]=calc_sRK4(x0,h);

    % use golden search to get a more precise answer
    td=t;
    yd=x(:,1);
    %
    a=0;
    b=30;
    tol=1.0e-10;
    n=0;
    %
    g=(sqrt(5)-1)/2;
    r1=a+(b-a)*(1-g);
    f1=dd(r1,td,yd);
    r2=a+(b-a)*g;
    f2=dd(r2,td,yd);
    %
    while (b-a) > tol,
      n=n+1;
      if f1 < f2,
        b=r2;
        r2=r1;
        f2=f1;
        r1=a+(b-a)*(1-g);
        f1=dd(r1,td,yd);
      else
        a=r1;
        r1=r2;
        f1=f2;
        r2=a+(b-a)*g;
        f2=dd(r2,td,yd);
      end
    end
    T_of_A(i) = (a+b)/2;
    y_axis(i) = T_of_A(i) / (2*pi);
    %
end

plot(A_array, y_axis);
ylabel('T(A)/(2*pi)');
xlabel('A');
title('Problem 2');




