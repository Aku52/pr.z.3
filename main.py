input_data = open('input.txt','r')
data = input_data.read()
a = int(data)
b= a**2
c=str(b)
output_data = open('input.txt','w')
output_data.write(c)

input_data.close()
output_data.close()