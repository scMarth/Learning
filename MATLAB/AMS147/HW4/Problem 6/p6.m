clear all 
clc 
% 
L=2*pi; 
c0=4*pi^2/L^2; 
% 
N=1024; 
dx=L/N; 
x=[0:N-1]*dx; 
u0=zeros(1,N); 
%512, 
%for the interval [0, 2)0 to 1
for a=1:166, 
u0(1,a)=0; 
end 

%for the interval [2, 3)1 to 3 
for b=167:490, 
u0(1,b)=2; 
end 

%for the interval [3, 5) 
for c=491:815, 
u0(1,c)=-1; 
end 
%for the interval [5, 2*pi] 

for d=816:1024, 
u0(1,d)=0; 
end 

y=fft(u0); 
ind=[0:N/2,-N/2+1:-1]; 
% 
t=0.01; 
y2=y.*exp(-c0*ind.^2*t); 
u_01=real(ifft(y2)); 
% 
t=0.03; 
y2=y.*exp(-c0*ind.^2*t); 
u_05=real(ifft(y2)); 
% 
t=0.1; 
y2=y.*exp(-c0*ind.^2*t); 
u_06=real(ifft(y2));
%
plot(x,u0,'k-','linewidth',1.0) 
hold on 
plot(x,u_01,'g--','linewidth',1.0) 
plot(x,u_05,'r--','linewidth',1.0)
plot(x,u_06,'b--','linewidth',1.0)
% 

axis([0,7,-1.2,2.3]) 
set(gca,'fontsize',10) 
set(gca,'xtick',[0:1:6]) 
set(gca,'ytick',[-1.5:0.2:2.1]) 
xlabel('x') 
ylabel('u0') 
legend('t = 0.01','t = 0.03','t = 0.1') 
title('Heat Equation Through Fourier Transform')
