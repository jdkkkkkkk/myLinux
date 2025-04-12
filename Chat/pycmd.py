import sys
import termios
import tty
import signal
import os
import subprocess

from offline import get_response
from online import chat_main
from globl import *



class MyCmd:
    real_prompt = ">>> "
    hint_text = "\033[90m" + hint_content +"\033[0m"

    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        self.run()

    def chat(self, user_input):
        print("\n")
        if is_offline:
            get_response(user_input)
        else:
            chat_main(user_input)

    def cmd(self, cmd):
        if cmd == "?":
            print("\n")
            get_help()
        elif cmd == "exit":
            print("\n\033[1;32mGoodbye!\033[0m\n")
            sys.exit(0)
        elif cmd == "setup":
            if is_offline:
                os.system("python3 offline_setup.py")
            else:
                os.system("python3 online_setup.py")
        else:
            abnormal_output("err", f"\"unrecognized option \'{cmd}\'\"")


    def run(self):
        """主循环"""
        while True:
            user_input = self.show_hint_and_get_input()
            if user_input.strip() != "" and user_input.strip()[0] == "/":
                self.cmd(user_input.strip()[1:])
                continue


            self.chat(user_input)

       
    def show_hint_and_get_input(self):
        """显示 `>>> hint`，并等待用户输入"""
        sys.stdout.write(f"\r{self.real_prompt}{self.hint_text} \033[5G")  # 显示提示
        sys.stdout.flush()
        return self.get_user_input()  # 监听输入并返回用户输入

    def get_user_input(self):
        """监听用户输入，并在第一个字符输入后清除 `hint`"""
        user_input = ""
        first_char = True

        # 获取终端文件描述符
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)  # 使用 cbreak 模式，避免终端锁死
            while True:
                char = sys.stdin.read(1)  # 读取一个字符
                if char == "\n":  # 遇到回车，结束输入
                    break
                elif char == "\x7f":    #处理backspace
                    if user_input and len(user_input) > 0:
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                        user_input = user_input[:-1]
                else:
                    if first_char:  # 第一次输入时，清除 `hint`
                        sys.stdout.write(f"\r{self.real_prompt}" + len(hint_content)*" " + "\033[4G")  # 用空格覆盖 `hint`
                        sys.stdout.write(f"\r{self.real_prompt}{char}")  # 只保留 `>>> 用户输入`
                        sys.stdout.flush()
                        first_char = False
                    else:
                        sys.stdout.write(char)  # 继续显示输入内容
                        sys.stdout.flush()
                    user_input += char
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # 恢复终端模式

        return user_input

    #handle Ctrl+C
    def signal_handler(self, sig, frame):
        abnormal_output("warning", "\"better use /exit\"")
        sys.exit(0)

if __name__ == "__main__":
    MyCmd()

