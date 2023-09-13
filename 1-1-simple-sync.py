import time
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# จำลองเวลาการทำงาน โดยหน่วงเวลา 1วินาที

def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name} : Computing {total} + {number}')
        sleep()
        total += number
    # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา 
    print(f'Task {name}: Sum = {total}\n ')


start = time.time()
# ส่วนนี้เป็นการเรียกใช้ sum function โดยที่กำหนดชื่อ Task เเละค่าจำนวน
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3])
]

end = time.time()
print(f'Time: {end-start:.2f} sec')
# ton@ton2534:~/work/asynconas$ /bin/python3 /home/ton/work/asynconas/class5-asyncio/1-1-simple-sync.py
# Task A : Computing 0 + 1
# Time: 0.00
# Task A : Computing 1 + 2
# Time: 1.00
# Task A: Sum = 3
 
# Task B : Computing 0 + 1
# Time: 2.00
# Task B : Computing 1 + 2
# Time: 3.00
# Task B : Computing 3 + 3
# Time: 4.00
# Task B: Sum = 6
 
# Time: 5.01 sec