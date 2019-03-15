%
n = 10^5;

single_pr = zeros(1,n);
double_pr = zeros(1,n);
Esp = zeros(1,n);
sum = 0;


for i=1:n,
    single_pr(i) = single(sin(i));      %single precision
    double_pr(i) = sin(i);              %double precision
    Esp(i) = single(sin(i)) - sin(i);   %round-off error approximation
    
    sum = sum + (Esp(i)).^2;
end

RMS = sqrt(sum/n)

%plot the histogram
hist(Esp);
hold all;
title('Problem 3');

