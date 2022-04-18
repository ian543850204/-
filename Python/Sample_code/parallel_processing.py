# Python parallel_processing
# create by Ian
# 2022/4/18

#平行演算套件
import multiprocessing 
from multiprocessing import Process, Pool, freeze_support
from functools import partial
from itertools import repeat



def multiprocessing_funtion(a,b,c):

    return_A = a+b+c
    return_B = a*b*c
    return return_A,return_B

#設定為主涵式    
if __name__ == '__main__':
    #設定範例
    a=[3,6,6]
    b=[4,5,6]
    c=[5,3,6]

    #平行核心數      
    pool_cunt = 4
    #平行數設定
    pool = Pool(pool_cunt)
    #傳入的函數        
    return_from_funtion =pool.starmap(multiprocessing_funtion, zip(a,b,c))

    #取出結果
    for i in range(len(return_from_funtion)):
        return_A = return_from_funtion[i][0]
        return_B = return_from_funtion[i][1]
    
        #顯示
        print("第" +str(i)+ "輪結果:")
        print("a+b+c ="+str(return_A))
        print("a*b*c ="+str(return_B))