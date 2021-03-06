
%
% This code demonstrates that the Fourier transform can be used to
% filter out the noise and reconstruct the original function.
%
clc
clear
clf reset
%
load data8.txt
%
N=size(data8,1);
t=data8(:,1);
f=data8(:,2);
%
y=fft(f);
ind=[0:N/2,-N/2+1:-1]';
%

for m=4:128,
    m_array(m) = m;
    y2=y.*(abs(ind)<=m);
    f2=real(ifft(y2));  %modes with |k|<=m ; recovered from data
    %
    fe=exp(-cos(2*t)+sin(7*t)); %3. exact f(x)

    err(m) = (norm(f2 - fe))/(sqrt(N));
end

plot(m_array(4:128), err(4:128))
title('Problem 5')
xlabel('m')
ylabel('err(m)')