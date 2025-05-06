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
        
numbers=input("How many inputs you want")
my_list=[]
for i in range(int(numbers)):
    numb=input("Input your temp here")
    my_list.append(int(numb))
    print(my_list)
 

calc_average(my_list,numbers)
min_max(my_list)