import time

def task_2():
    print("start task_2")
    yield "abdulaziz"
    #yield "aa"

def task_3():
    print("start task_3")
    yield "shukurov"
    #yield "bb"

def task_4():
    print("start task_4")
    yield "python"
    #yield "abab"

def task_5():
    print("start task_5")
    yield "abdulaziz shukurov python"

def test():
    # a = yield task_2(2)
    # b = yield task_3(2)
    # yield task_4(2, 8)
    yield task_2()
    yield task_3()
    yield task_4()
    yield task_5()

for i in test():
    print("next")
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)
