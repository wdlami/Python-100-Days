import asyncio

async def display(num):
    await asyncio.sleep(5)
    print(num)

def main():
    async def run_async():
        tasks = [asyncio.create_task(display(i)) for i in range(1, 10)]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        print("Completed tasks:")
        for t in done:
            print(await t)

        # await asyncio.create_task(display(100))
        # await asyncio.gather(*tasks)
        # results = await asyncio.gather(*tasks)
        # print("Results:", results)

    # 使用 asyncio.run() 来运行异步函数
    asyncio.run(run_async())

if __name__ == '__main__':
    main()