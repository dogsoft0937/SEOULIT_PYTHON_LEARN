import time
input('엔터를 입력 후 20초를 셉니다')
start=time.time()
input('20초 후에 다시 엔터를 누릅니다')
end=time.time()

delta=end-start
print('실제시간 :',delta,'초')
print('차이',abs(delta-20),'초')