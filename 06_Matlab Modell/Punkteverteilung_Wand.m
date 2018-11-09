%% Matlab Modell zur Bestimmung von Punkteverteilung eines LIDAR Systems

clear all

%% Raumbedingungen
L_l = 600; % Länge der Wand in cm
L_h = 300; % Höhe der Wand in cm
L_b = 500; % Abstand zur Wand in cm

A_ges = 2*(L_l*L_h) + 2*(L_b*L_h) + 2*(L_l*L_b); % Gesamtfläche
A_wand = L_l*L_h; % Fläche der langen Wand
Verhaeltnis = A_wand/A_ges; % Verhälnis Fläche der langen Wand zu Gesamtfläche

W_l_l = (2*atan((L_l/2)/(L_b/2))*360)/(2*pi); % Winkel, in welchem die Wand horizontal ist
W_l_h = (atan((L_h)/(L_b/2))*360)/(2*pi); % Winkel, in welchem die Wand vertikal ist

%% Zeitbedingungen
T_max = 3600; % Maximale Messdauer in Sekunden

%% Sensor-/Mechanikbedingungen
F_sensor = 50; % Frequenz des Sensors
Microsteps = 4; % Microsteps des Schrittmotortreibers
Schrittmotor_winkel = 1.8;
Schrittmotor_kleinste_Aufloesung = Schrittmotor_winkel/16;

%% Rahmenberechnungen
P_t = T_max*F_sensor; % Punkte pro maximal Zeit

W_h = Schrittmotor_winkel / Microsteps; % Horizontale Winkelauflösung
S_h = 360/W_h; % Horizontale Schritte gesamt
S_h_w = floor(W_l_l/W_h); % Horizontale Schritte auf der Wand

S_v = P_t/S_h; % Vertikale Schritte
W_v = floor((180/S_v)/Schrittmotor_kleinste_Aufloesung)*Schrittmotor_kleinste_Aufloesung; % Vertikale Winkelauflösung
S_v_w = floor(W_l_h/W_v); % Vertikale Schritte auf der Wand
P_w = P_t * Verhaeltnis % Punkte auf der Wand

%% Berechnung
E_x=zeros(S_h_w,S_v_w); % Initialisieren der Matrix für die X-Werte
E_z=zeros(S_h_w,S_v_w); % Initialisieren der Matrix für die Z-Werte
M = zeros(floor(S_v_w*S_h_w),3);

figure();
hold on; % Festhalten der Werte
for i = -(S_h_w/2):1:(S_h_w/2)
    for j = 1:1:S_v_w
        E_x(i+1+(S_h_w/2),j)=tan(deg2rad(i*W_h))*L_b/2; % Berechnung der X-Werte
        E_z(i+1+(S_h_w/2),j)=tan(deg2rad(j*W_v))*(L_b/(2*cos(deg2rad(i*W_h)))); % Berechnung der Z-Werte
        M(S_v_w*(i+(S_h_w/2)) + j, 1) = deg2rad(i*W_h);
        M(S_v_w*(i+(S_h_w/2)) + j, 2) = deg2rad(j*W_v);
        M(S_v_w*(i+(S_h_w/2)) + j, 3) = sqrt((L_b/2)*(L_b/2) + E_x(i+1+(S_h_w/2),j)*E_x(i+1+(S_h_w/2),j) + E_z(i+1+(S_h_w/2),j)*E_z(i+1+(S_h_w/2),j));
        plot(E_x(i+1+(S_h_w/2),j),E_z(i+1+(S_h_w/2),j), '*r'); % Zeichnen der Punkte
    end
end
csvwrite('file4.txt',M);
axis([-L_l/2 L_l/2 0 2*L_h]); % Einstellen der Achsen

