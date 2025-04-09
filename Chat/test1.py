import time
import threading
import sys

spinner = ['|', '/', '-', '\\']


flag = True
lock = threading.Lock()


def FLAG():
    i = 0
    global flag
    global lock
    while True:
        with lock:
            tmp_flg = flag
        if not tmp_flg:
            break
        sys.stdout.write(f'\rLoading {spinner[i % 4]}')
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1


def MAIN():
    #open a new process FLAG
    tr_flag = threading.Thread(target=FLAG)
    tr_flag.start()
    time.sleep(5)
    global flag
    global lock
    with lock:
        flag = False
    tr_flag.join()
    print("\r" + " "*15 + "\r" + "aaaaaaaaaaaaaaaaaaaaa")


#print("\nDone!")
if __name__ == "__main__":
    MAIN()
