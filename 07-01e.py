##2020045070 김가현 ##
import random

data=[]
i,k=0,0

if __name__=="__main__" :
    for i in range(0,10) :
        tmp=hex(random.randrange(0,100000))
        data.append(tmp)

    print('정렬 전 데이터 :',end ='')
    [print(num,end='')for num in data]

    for i in range(0,len(data)-1) :
        for k in range(i+1,len(data)) :
            tmp=data[i]
            data[i]=data[k]
            data[k]=tmp

    print('\n 정렬 후 데이터 :',end='')
    [print(num,end='')for num in data]
