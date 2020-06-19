import in_place
import sys
import os

n0=n1=n2=n3=n4=n5=n6=n7=n8=0
d0=c0=l0=r0=a0=0
dh0=ch0=0
dgain=84
igain=88
dgainh=20
igainh=24
istype=0
mixer = sys.argv[1]
print("Project Duality - v2")
print("\n \n")
print("Selected File : "+mixer)
print("\n")
boost=(input("Would you like to increase the speaker gain? Y or N \n"))
boost=boost.lower()
boosth=(input("Would you like to increase the headphone gain? Y or N \n"))
boosth=boost.lower()
duals=(input("Would you like to enable dual speaker? Y or N \n"))
duals=duals.lower()
if boost=="y":
    dgain=int(input("Enter the default headphone gain (84 in most cases) : \n"))
    igain=int(input("How much would you like to increase the speaker gain (0-10) : \n"))
    if igain>6:
        print("Warning : Reduce the gain if you hear distortions")
    igain=igain+dgain
	
if boosth=="y":
    dgainh=int(input("Enter the default gain (20 in most cases) : \n"))
    igainh=int(input("How much would you like to increase the headphone gain (0-10) : \n"))
    if igainh>6:
        print("Warning : Reduce the gain if you hear distortions")
    igainh=igainh+dgainh
with in_place.InPlace(mixer) as file:
    for line in file:
        if boost=="y":
            if (n0<1) and ('<ctl name="RX0 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX0 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX0 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n0=n0+1
            elif n1<1 and ('<ctl name="RX1 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX1 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX1 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n1=n1+1
            elif n2<1 and ('<ctl name="RX2 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX2 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX2 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n2=n2+1
            elif n3<1 and ('<ctl name="RX3 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX3 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX3 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n3=n3+1
            elif n4<1 and ('<ctl name="RX4 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX4 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX4 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n4=n4+1
            elif n5<1 and ('<ctl name="RX5 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX5 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX5 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n5=n5+1
            elif n6<1 and ('<ctl name="RX6 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX6 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX6 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n6=n6+1
            elif n7<1 and ('<ctl name="RX7 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX7 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX7 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n7=n7+1
            elif n8<1 and ('<ctl name="RX8 Digital Volume" value="'+str(dgain)+'" />' in line):
                line = line.replace('<ctl name="RX8 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX8 Digital Volume" value="'+str(igain)+'" /> <!--Volume Boost-->')
                n8=n8+1
        if duals=="y":
            if (d0<1) and ('<path name="deep-buffer-playback speaker">' in line):
                line = line.replace('<path name="deep-buffer-playback speaker">','<path name="deep-buffer-playback speaker"> \n \t    <ctl name="SLIMBUS_0_RX Audio Mixer MultiMedia1" value="1" /> <!--Dual Speaker-->')
                d0=d0+1
            if (c0<1) and ('<path name="compress-offload-playback speaker">' in line):
                line = line.replace('<path name="compress-offload-playback speaker">','<path name="compress-offload-playback speaker"> \n \t    <ctl name="SLIMBUS_0_RX Audio Mixer MultiMedia4" value="1" /> <!--Dual Speaker-->')
                c0=c0+1
            if (l0<1) and ('<path name="low-latency-playback speaker">' in line):
                line = line.replace('<path name="low-latency-playback speaker">','<path name="low-latency-playback speaker"> \n \t    <ctl name="SLIMBUS_0_RX Audio Mixer MultiMedia5" value="1" /><!--Dual Speaker-->')
                l0=l0+1
            if (r0<1) and ('<ctl name="RX INT0_1 MIX1 INP0" value="ZERO" />' in line):
                line = line.replace('<ctl name="RX INT0_1 MIX1 INP0" value="ZERO" />','<ctl name="RX INT0_1 MIX1 INP0" value="RX0" /> <!--Dual Speaker-->')
                r0=r0+1
            if (a0<1) and ('<ctl name="SLIM RX0 MUX" value="ZERO" />' in line):
                line = line.replace('<ctl name="SLIM RX0 MUX" value="ZERO" />','<ctl name="SLIM RX0 MUX" value="AIF1_PB" /> <!--Dual Speaker-->')
                a0=a0+1
        if boosth=="y":
            if (dh0<1) and ('<ctl name="HPHL Volume" value="'+str(dgainh)+'" />' in line):
                line = line.replace('<ctl name="HPHL Volume" value="'+str(dgainh)+'" />', '<ctl name="HPHL Volume" value="'+str(igainh)+'" /> <!--Headphone Boost(Left)-->')
                dh0=dh0+1
            if (ch0<1) and ('<ctl name="HPHR Volume" value="'+str(dgainh)+'" />' in line):
                line = line.replace('<ctl name="HPHR Volume" value="'+str(dgainh)+'" />', '<ctl name="HPHR Volume" value="'+str(igainh)+'" /> <!--Headphone Boost(Right)-->')
                ch0=ch0+1
        if ('<mixer>' in line):
                                    line=line.replace('<mixer>','<mixer> <!--Patched with Project Duality-->')
                                    
        file.write(line)
print(" \n \n")
if boost=="y":
    if n0==1:
        print("Speaker Gain Patched!")
    else:
        print("Speaker Gain Patch Failed!")
        print("Visit the project wiki and follow the instructions on Troubleshoot page")
		
if boosth=="y":
    if dh0==1:
        print("Headphone Gain Patched!")
    else:
        print("Headphone Gain Patch Failed!")
        print("Visit the project wiki and follow the instructions on Troubleshoot page")

if duals=="y":
    if d0==1:
        print("Dual Speaker Patched!")
    else:
        print("Dual Speaker Patch Failed!")
        print("Visit the project wiki and follow the instructions on Troubleshoot page")

print("")
print("Don't forget to visit the thread on XDA and drop your feedback")
print("")
print("By acervenky@XDA")
print("")
print("")

os.system('pause')


