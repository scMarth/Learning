clear
clc

N=256;
hs = 4/N;

num_steps = 513; % (5 - 1)/((4/256)/2)
                 % since s goes from 1 to 5
g_of_s = zeros(1,num_steps);
s_array = zeros(1,num_steps);
g_of_t_y = zeros(1, 257);
g_of_t_y2 = zeros(1, 257);
a = 0; b = 5;

got_index = 1;
got2_index = 1;
%Calculate G(s) for s = [1:hs/2:5]
%iterate over possible values of s
for i=1:num_steps,
    s_array(i) = 1 + (hs*(i-1)/2);
    
    h = (b-a)/N;
    x=a+[0:N]*h;
    y=g(s_array(i), x);
    
    %simpson rule
    x2=a+[0:N-1]*h+h/2;
    y2=g(s_array(i), x2);
    Tsimp=(y(1)+y(N+1)+2*sum(y(2:N))+4*sum(y2))*h/6;
    
    g_of_s(i) = Tsimp;

    if mod(i,2) == 0 %if index i is even
        g_of_t_y2(got2_index) = Tsimp;
        got2_index = got2_index + 1;
    elseif mod(i,2) == 1 %if index i is odd
        g_of_t_y(got2_index) = Tsimp;
        got_index = got_index + 1;
    end
end

%calculate G(t) for all possible t = [1:hs:5]

g_of_t = zeros(1,257);
g_of_t(1) = 0;
for i=1:256,
    % N=1          (h/6)*(gos(1) + 4*gos(2) + gos(3)
    % N=2          (h/6)*(gos(1) + 4*gos(2) + gos(3) + (h/6)*(gos(3) + 4*gos(4) + gos(5))                   gos(3) is added twice
    % N=3          (h/6)*(gos(1) + 4*gos(2) + gos(3) + (h/6)*(gos(3) + 4*gos(4) + gos(5)) + (h/6)*(gos(5) + 4*gos(6) + gos(7))
    %
    %                            odd numbers equal to or above 3
    % (h/6)*[4*sum(gos(2:2:i*2)) + gos(1) + sum(gos(3:2:(2*i + 1))) + sum(gos(3:2:(2*i + 1))) - gos(2*i+1)]
    
    g_of_t(i+1) = (h/6)*(4*sum(g_of_s(2:2:i*2)) + g_of_s(1) + sum(g_of_s(3:2:(2*i + 1)))  + sum(g_of_s(3:2:(2*i + 1))) - g_of_s(2*i+1));
end

plot(1:hs:5, g_of_t);
title('Problem 6');
ylabel('G(t)');
