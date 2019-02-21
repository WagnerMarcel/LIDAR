## Programm zum Bewegen eines Motors

#Bibliotheken
import sys

#Eigene Dateien
import Motor


# Motor 1, Nema 11
M1 = Motor.MOTOR(31,29,37,35,33)

# Motor 2, Nema 17
M2 = Motor.MOTOR(18,16,36,38,40)

if(len(sys.argv) < 3):
    print("""Aufruf wie folgt:
    python LIDAR_Bewegen.py <nummerMotor> <Schritte>
    <nummerMotor> = 1 oder 2
    <Schritte> = positiv fuer Uhrzeigersinn, negativ fuer gegen den Uhrzeigersinn
    """)
else:
    m = sys.argv[1]
    s = sys.argv[2]
    dir = True
    if(s > 0):
        dir = True
    else if(s < 0):
        dir = False
        s = s * -1
    else:
        print("Bitte Schritte angeben")

    if(m == 1):
        M1.moveMotor(dir, s, 0.001)
    else if(m == 2):
        M2.moveMotor(dir, s, 0.001)
    else:
        print("Bitte Motor angeben")
