import ollama
import sys


def get_response(input_token):
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[
        {
            'role': 'user',
            'content': input_token
        },
    ])
    
    #if is_simplified:
    print(response['message']['content'].split("</think>")[1].lstrip())
    #else:
    #    print(response['message']['content'])
    
    

if __name__=="__main__":
    input_token = sys.argv[1]
#    is_simplified = sys.argv[2]
    get_response(input_token)
