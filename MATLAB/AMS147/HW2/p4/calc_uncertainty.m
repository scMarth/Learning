%
% This code first generates 3000 artificial data sets based on
% the fitting function at the optimal value of c and using
% the standard deviation of noise. 
% For each data set, it runs the golden search method to find 
% the optimal value of c corresponding to that data set. 
% The statistical uncertainty is calculated from the 3000 
% estimated values of c.
% Finally, it plots a histogram of the estimated value of c. 
%
% First call calc_c_optimal to calculate c0 and noise_std
calc_c_optimal
drawnow
%
figure(2)
clf reset
axes('position',[0.16,0.16,0.72,0.70])
%
m=3000;
c_v=zeros(1,m);
%
for k=1:m,
%y=exp(-c0*x)+noise_std*randn(N,1);  % artificial data set
y=cos(2*exp(c0*x))+noise_std*randn(N,1); % artificial data set
%
a=0;
b=2;
tol=1.0e-10;
n=0;
%
g=(sqrt(5)-1)/2;
r1=a+(b-a)*(1-g);
f1=dd(r1,x,y);
r2=a+(b-a)*g;
f2=dd(r2,x,y);
%
while (b-a) > tol,
  n=n+1;
  if f1 < f2,
    b=r2;
    r2=r1;
    f2=f1;
    r1=a+(b-a)*(1-g);
    f1=dd(r1,x,y);
  else
    a=r1;
    r1=r2;
    f1=f2;
    r2=a+(b-a)*g;
    f2=dd(r2,x,y);
  end
end
c_v(k)=(a+b)/2;
end
%
disp('   Mean         Standard deviation of estimated c')
disp([mean(c_v), std(c_v)])
hist(c_v,40)
set(gca,'fontsize',16)
xlabel('Estimated value of c')
ylabel('Count')
title('Histogram of estimated value of c')
%
