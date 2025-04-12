#globl.py

#python format

#global
is_offline = False
spinner = ['|', '/', '-', '\\']

#settings
offline_model_options = ["deepseek-r1:1.5b"]
online_model_options = ["deepseek-chat", "deepseek-reasoner"]
simplify_options = ["yes", "no"]

offline_settings = {
    "model": offline_model_options[0],
    "simplify": simplify_options[0]
}

online_settings = {
    "model": online_model_options[0],
    "simplify": simplify_options[0]
}

selected_index = {
    "model": 0,
    "simplify": 0
}

menu_items = ["model", "simplify"]
current_item = 0  # 当前高亮的选项

#help
hint_content = "type /? for help"
help_content = "Available Commands:\n  /?\t\tshow this message\n  /exit\t\texit\n  /setup\tset mode\n  Ctrl+C\texit"

def abnormal_output(_type, content):
    import subprocess
    output = subprocess.check_output(['bash', '-c', f"source ../.global; {_type} chat {content}"])
    output = str(output)
    real_output = output[2:-3]
    real_output = real_output.encode('utf-8').decode('unicode-escape')
    print("\n" + real_output)

def get_help():
        print(help_content)
