def average(*args):
    avg = sum(args)/len(args)
    return avg

def average2(**kwargs):
    values = list(kwargs.values())
    avg = sum(values)/len(values)
    return avg



avg1 = average(1,2,3,4,5,6,7,8,9)
print(avg1)
avg2 = average2(num1=35,num2=56,num3=78,num4=90,num5=80,num6=70)
print(avg2)
