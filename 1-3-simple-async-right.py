import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
# จำลองเวลาการทำงาน โดยหน่วงเวลา 1วินาที
# เปลี่ยน การทำงานของ sleep เป็น อะซิงโครนัส


async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'task {name}: Computing {total}+{number}')
        # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา
        await sleep()
        # ใช้เพื่อเรียกฟังก์ชัน อะซิงโครนัส await เพื่อให้ทำงานอื่นขณะที่รอ sleep ทำงาน
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()

# สร้างลูปเพื่อรับค่า
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
# จะทำลูปจนกว่างานทั้งหมดจะเสร็จ
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')

# ton@ton2534:~/work/asynconas$ /bin/python3 /home/ton/work/asynconas/class5-asyncio/1-3-simple-async-right.py
# task A: Computing 0+1
# Time: 0.00
# task B: Computing 0+1
# Time: 0.00
# task A: Computing 1+2
# Time: 1.00
# task B: Computing 1+2
# Time: 1.00
# Task A: Sum = 3

# task B: Computing 3+3
# Time: 2.00
# Task B: Sum = 6

# Time: 3.00 sec