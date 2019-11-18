import in_place

n0=n1=n2=n3=n4=n5=n6=n7=n8=0
dgain=85
igain=88
with in_place.InPlace('data.xml') as file:
    for line in file:
        if n0<1:
            line = line.replace('<ctl name="RX0 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX0 Digital Volume" value="'+str(igain)+'" />')
            n0=n0+1
        elif n1<1:
            line = line.replace('<ctl name="RX1 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX1 Digital Volume" value="'+str(igain)+'" />')
            n1=n1+1
        elif n2<1:
            line = line.replace('<ctl name="RX2 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX2 Digital Volume" value="'+str(igain)+'" />')
            n2=n2+1
        elif n3<1:
            line = line.replace('<ctl name="RX3 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX3 Digital Volume" value="'+str(igain)+'" />')
            n3=n3+1
        elif n4<1:
            line = line.replace('<ctl name="RX4 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX4 Digital Volume" value="'+str(igain)+'" />')
            n4=n4+1
        elif n5<1:
            line = line.replace('<ctl name="RX5 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX5 Digital Volume" value="'+str(igain)+'" />')
            n5=n5+1
        elif n6<1:
            line = line.replace('<ctl name="RX6 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX6 Digital Volume" value="'+str(igain)+'" />')
            n6=n6+1
        elif n7<1:
            line = line.replace('<ctl name="RX7 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX7 Digital Volume" value="'+str(igain)+'" />')
            n7=n7+1
        elif n8<1:
            line = line.replace('<ctl name="RX8 Digital Volume" value="'+str(dgain)+'" />', '<ctl name="RX8 Digital Volume" value="'+str(igain)+'" />')
            n8=n8+1
        file.write(line)
