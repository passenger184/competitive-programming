import math
input_list = input().split(" ")
num = list(map(int , input_list))
l = math.ceil(num[0] / num[2])
w = math.ceil(num[1] / num[2])
print(l * w)    
