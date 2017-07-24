from numpy import std, mean
myString = """5.4.2017;FILL 80 90;1.04;43.14;3.66;
5.4.2017;FILL 80 91;1.01;42.25;3.42;
5.4.2017;FILL 80 92;1.06;44.18;3.61;
5.4.2017;FILL 80 93;1.01;42.10;3.45;
5.4.2017;FILL 80 94;1.05;43.76;3.52;
5.4.2017;FILL 80 95;1.04;43.47;3.52;
5.4.2017;FILL 80 96;1.05;43.69;3.68;"""
infill = 0.8
area = 16 + infill*8
print("area is ", area)
myList = myString.split("\n")
forces = []
for x in myList:
    line = x.split(";")
    forces.append(float(line[2]))
strengths = []
for x in forces:
    strengths.append(x/area*1000)
print("Mean average strengths: ", mean(strengths))
print("Std strengths: ", std(strengths))
