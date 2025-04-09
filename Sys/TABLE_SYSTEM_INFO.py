import os
import sys
import signal

#--------tbs is here, you can change it to whatever you want--------
tbs="╚╩╝╠╬╣╔╦╗ ═══║║║"


#-------------------------------------------------------------------
def signal_handeler(signal, frame):
    print('\n' * len_name * 2)
    #print("\nYou pressed Ctrl+C!")
    sys.exit(0)



class _skeleton:
    def __init__(self):
        self.width_l = 0
        self.width_r = 0
        self.total_width = 0
        self.title_top = ""
        self.title_btm = ""
        self.mid_a = ""
        self.top = ""
        self.btm = ""

class _data:
    def __init__(self):
        self.name = []
        self.value = []


def preparation(_type, sh_path, info_path):
    #------draw skeleton begin------
    os.system("bash "+ sh_path)
    #name = []
    #value = []
    data = _data()
    skeleton = _skeleton()
    FILE = open(info_path, 'r')
    file = FILE.read()
    lines = file.split('\n')
    while '' in lines:
        lines.remove('')
    for tmp_line in lines:
        tmp_line_for_use = tmp_line.split(":", 1)
        data.name.append(str.strip(tmp_line_for_use[0]))
        data.value.append(str.strip(tmp_line_for_use[1]))
    if _type == "SYS":
        global val_0
        val_0 = data.value.pop(0)
        _ = data.name.pop(0)
    skeleton.width_l = len(max(data.name, key = len)) + 2
    skeleton.width_r = len(max(data.value, key = len)) + 2
    skeleton.total_width = skeleton.width_l + skeleton.width_r + 1
    skeleton.title_top=tbs[6] + tbs[10]*skeleton.total_width + tbs[8]
    skeleton.title_btm=tbs[3] + tbs[10]*skeleton.width_l + tbs[7] + tbs[10]*skeleton.width_r + tbs[5] 
    skeleton.mid_a=tbs[3] + tbs[10]*skeleton.width_l + tbs[4] + tbs[10]*skeleton.width_r + tbs[5]
    skeleton.top=tbs[6] + tbs[10]*skeleton.width_l + tbs[7] + tbs[10]*skeleton.width_r + tbs[8]
    skeleton.btm=tbs[0] + tbs[10]*skeleton.width_l + tbs[1] + tbs[10]*skeleton.width_r + tbs[2]
    #------draw skeleton end------
    return data, skeleton



def TABLE(_type, sh_path, info_path):
    if _type == "SYS":
        data, skeleton = preparation(_type, sh_path, info_path)
        print(skeleton.title_top)
        print(tbs[15], val_0.center(skeleton.total_width-2), tbs[15])
        print(skeleton.title_btm)
        for tmp_name, tmp_val in zip(data.name, data.value):
            print(tbs[15], '{0:^{width_1}}'.format(tmp_name, width_1=skeleton.width_l-2), tbs[15], '{0:^{width_2}}'.format(tmp_val, width_2=skeleton.width_r-2), tbs[15])
            if tmp_name != data.name[-1] and tmp_val != data.value[-1]:
                print(skeleton.mid_a)
            else:
                print(skeleton.btm)

    
    elif _type == "REALTIME":
        import time
        data, skeleton = preparation(_type, sh_path, info_path)
        global len_name
        len_name = len(data.name)
        ansi_escape = 2 * len_name + 1
        while True:
            data, skeleton = preparation(_type, sh_path, info_path)
            print(skeleton.top)
            for tmp_name, tmp_val in zip(data.name, data.value):
                print(tbs[15], '{0:^{width_1}}'.format(tmp_name, width_1=skeleton.width_l-2), tbs[15], '{0:^{width_2}}'.format(tmp_val, width_2=skeleton.width_r-2), tbs[15])
                if tmp_name != data.name[-1] and tmp_val != data.value[-1]:
                    print(skeleton.mid_a)
                else:
                    print(skeleton.btm)
            print(f"\033[{ansi_escape}A", end='')
            sys.stdout.write("\033[?25l")
            time.sleep(0.3)
            signal.signal(signal.SIGINT, signal_handeler)
            



if __name__ == "__main__":
    #sh_path = "/MY_TEST/Sys/MY_SYSTEM_INFO.sh"
    #info_path = "/MY_TEST/Sys/.sys_info"
    _type = sys.argv[1]
    sh_path = sys.argv[2]
    info_path = sys.argv[3]
    TABLE(_type, sh_path, info_path)
