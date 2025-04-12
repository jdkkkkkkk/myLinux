import sys
import time
import threading
from globl import *
from openai import OpenAI



chat_flag_ = True
chat_lock = threading.Lock()


def chat_flag():
    i = 0
    global chat_flag_
    global chat_lock
    while True:
        with chat_lock:
            tmp_flag = chat_flag_
        if not tmp_flag:
            break
        sys.stdout.write(f'\rLoading {spinner[i % 4]}')
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1

def chat_main(line):
    content = ""   # to be used???
    subthread_chat_flag = threading.Thread(target=chat_flag)
    subthread_chat_flag.start()

    # 请将 "<deepseek api key>" 替换为您的DeepSeek API Key
    client = OpenAI(api_key="your-key-here", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": line},
        ],
        #stream=False  # 非流式输出，如果需要流式输出，设置为True
        stream=True
    )
    #print(response.choices[0].message.content) #非流式输出
    for chunk in response:
        content = chunk.choices[0].delta.content
        global chat_lock
        global chat_flag_
        if content != "" and chat_flag_:
            with chat_lock:
                chat_flag_ = False
            subthread_chat_flag.join()
            print("\r" + " "*15 + "\r")

        #sys.stdout.write(chunk.choices[0].delta.content)
        sys.stdout.write(content)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n\033[1;32m✓ Done\033[0m\n")


if __name__ == "__main__":
    line_tmp = sys.argv[1]
    line = str(line_tmp)
    if line == "":
        pass
    else:
        chat_main(line)
