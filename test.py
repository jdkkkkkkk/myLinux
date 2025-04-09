import subprocess
output = subprocess.check_output(['bash', '-c', 'source .global; err Chat \"test 11\"'])
output = str(output)
test1 = output[2:-3]
test1 = test1.encode('utf-8').decode('unicode-escape')
print(test1)
print("\033[1m$1:\033[0m \033[1;31merror: \033[0m")
