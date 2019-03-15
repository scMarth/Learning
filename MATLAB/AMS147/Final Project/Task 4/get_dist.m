function [dist]=get_dist(h,x0,mu)
    [t x]=calc_sRK4(x0,h,mu);

%    td=t(1:12801);   % select interval t = [0,50]
%    yd=x(1:12801,1); % select interval t = [0,50]

    %for z=1:length(t)
%       fprintf('ind %d = %d\n', z, t(z)); 
%    end

    
    
    td = t(1:1601);
    yd =x(1:1601,2);   % select interval t = [0,50]
    xd  =x(1:1601,1); % select interval t = [0,50]

    str = sprintf('Task 4, mu = %d', mu);
    
    figure;
    plot(x(:,1),x(:,2));
    xlabel('y(t)');
    ylabel('y''(t)');
    title(str);
    
%    dist=norm([0,0]-[xt,yt]);
     
     for i=1:length(td)-1,
        dist(i)=sqrt((0-xd(i))^2 + (0-yd(i))^2);
     end
     
    length_of_td = length(td)
    length_of_dist = length(dist)     
    figure
    plot(td(1:1600), dist);
    xlabel('t');
    ylabel('distance from origin');
    title(str);