import os
import threading
import time

path = os.path.split(os.path.realpath(__file__))[0]


# print(path)
def img_server():
    os.system(r"python {}\img_server.py".format(path))


def flask_mock_server():
    time.sleep(2)
    print("flask_mock_server will start!")
    print("按两下ENTER键，启动flask_mock_server")
    os.system(r"python {}\flask_mock_server.py".format(path))


thread = []
t1 = threading.Thread(target=img_server)
t2 = threading.Thread(target=flask_mock_server)
thread.append(t1)
thread.append(t2)
print(thread)
if __name__ == '__main__':
    for t in thread:
        t.start()
