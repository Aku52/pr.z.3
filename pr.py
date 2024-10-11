input_data = open('input.txt','r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if (a >= b) and (a >= c):
    more = a
elif (b >= c) and (b >= a) :
    more = b
elif (c >= b) and (c >= a):
    more = c

more = str(more)

output_data = open('input.txt','w')
output_data.write(more)

input_data.close()
output_data.close()