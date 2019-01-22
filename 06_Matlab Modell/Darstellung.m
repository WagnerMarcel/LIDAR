% Anwendung zur Darstellung einer 3D Punktewolke aus einem LIDAR System
clear all;
file = 'data2019-01-22_14-36-07.csv';

data = importdata(file,';',1); 
data = data.data;

distance = data(:,2);
azimuth = data(:,3);
elevation = data(:,4);


for i = 1:1:120049
    if(distance(i) < 2000)
        x(i) = -distance(i)*cos(deg2rad(elevation(i)))*cos(deg2rad(azimuth(i)));
        y(i) = distance(i)*cos(deg2rad(elevation(i)))*sin(deg2rad(azimuth(i)));
        z(i) = distance(i)*sin(deg2rad(elevation(i)));
    else
    end
end


plot3(x,y,z, '.')
axis([-400 400 -400 400 0 240])
pbaspect([1 1 0.3])