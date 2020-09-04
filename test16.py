#coding:utf-8
import time

#開始時刻
t1=time.time()

#３の300,000乗
x=1
for i in range(300000):
    x*=3

#計算の終了時刻
t2=time.time()

#計算結果をファイルへ出力
f =open('test16.txt','w')
f.write(str(x))
f.close()

#全処理の終了時刻
t3=time.time()
print(t3)


#経過時間の表示
print('計算時間：\t',t2-t1)
print('出力時間:\t',t3-t2)
print('全体の時間:\t',t3-t1)
