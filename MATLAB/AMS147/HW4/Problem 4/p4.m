clear
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Part I

t1 = (2*pi*[0:500])/500;
curve_1 = sin(1.5 * t1);
curve_2 = sin(22.5 * t1);

t2 = (2*pi*[0:21])/21;
curve_3 = sin(22.5 * t2);

plot(t1, curve_1, 'b-');
hold all
plot(t1, curve_2, 'r--');
plot(t2, curve_3, 'bd');
title('Problem 4 Part I');
legend('sin(1.5*t) vs. t=2*pi*[0:N]/N, N=500', 'sin(22.5*t) vs. t=2*pi*[0:N]/N, N=500', 'sin(22.5*t) vs. t=2*pi*[0:N]/N, N=21')
xlabel('t')
ylabel('y')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Part II

t3=(2*pi*[0:198])/198;
curve_4=sin(200*t3);

t4=(2*pi*[0:199])/199;
curve_5=sin(200*t4);

t5=(2*pi*[0:201])/201;
curve_6=sin(200*t5);

figure
plot(t3, curve_4, 'b*');
hold all
plot(t4, curve_5, 'ko');
plot(t5, curve_6, 'rs');
title('Problem 4 Part II');
legend('N=198', 'N=199', 'N=201')
xlabel('t')
ylabel('y')