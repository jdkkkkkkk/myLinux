import sys
import time
import itertools

# 模拟你的 response 流式数据（这里假设是字符流）
class MockResponse:
    def __iter__(self):
        for c in "Hello, this is streaming text from the server.":
            yield MockChunk(c)
            time.sleep(0.05)

class MockChunk:
    def __init__(self, content):
        self.choices = [type("Delta", (), {"delta": type("DeltaContent", (), {"content": content})()})]

response = MockResponse()

# 加载动画符号循环器
spinner = itertools.cycle(['|', '/', '-', '\\'])

text = ""

try:
    for chunk in response:
        # 获取字符
        text += chunk.choices[0].delta.content

        # 写文本 + 动画符号（不换行，刷新）
        sys.stdout.write(text + next(spinner) + '\r')  # \r 返回行首，覆盖上一次
        sys.stdout.flush()
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    # 输出结束后，删除动画符号（覆盖）
    sys.stdout.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    sys.stdout.write(text[:-10] + '\r')  # 清空当前行
    sys.stdout.flush()
    print("\n✓ Done.")  # 你可以换成你想要的结尾样式

