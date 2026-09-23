import asyncio

class Printer:
    @staticmethod
    async def print(text_queue: asyncio.Queue):
        while True:
            result = await text_queue.get()
            text_queue.task_done()

            print(result)