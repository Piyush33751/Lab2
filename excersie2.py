def calc_average(x,numbe):
    print("calc_average")
    list_sum=sum(x)
    avg =  int(list_sum)/int(numbe)
    print(avg)
    return avg
def min_max(numbi):
        print("Opearation for max and min")
        numbisf=min(numbi)
        print(numbisf)
        numb_max=max(numbi)
        print(numb_max)
        return numb_max,numbisf
def median_temp(listi,numbers):
     print("Median calc")
     x=1
     gone=numbers-x
     median_position=int(gone)/2
     gor=listi[int(median_position)]
     print(gor)
     return gor
    


numbers=int(input("How many inputs you want"))
my_list=[]
for i in range(int(numbers)):
    numb=input("Input your temp here")
    my_list.append(int(numb))
    print(my_list)
 

calc_average(my_list,numbers)
min_max(my_list)
x=median_temp(my_list,numbers)
print(x)
#if i see this it means there is additions :)