from Demo_CaoDuLieu import *
import threading
import time

# Demo Sync
time_start = time.time()
scrape_pnj_price()
tra_cuu_lich_mat_dien('PE04000246146')
time_stop = time.time()
print(f"Tong thoi gian chay: ", time_stop - time_start)


# Demo Async
time_start = time.time()
threadLock = threading.Lock()
threads = []
thread1 = threading.Thread(target=scrape_pnj_price, )
thread2 = threading.Thread(target=tra_cuu_lich_mat_dien,args=('PE04000246146', ))
thread3 = threading.Thread(target=scrap_gold_price_pnj, )
thread1.start()
thread2.start()
thread3.start()
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
# Cho cho tat ca deu complete
for item in threads:
    item.join()
time_stop = time.time()
print(f"Tong thoi gian chay: ", time_stop - time_start)