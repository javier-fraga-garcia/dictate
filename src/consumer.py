import asyncio


class Consumer:
    @staticmethod
    async def consume(audio_queue: asyncio.Queue, text_queue: asyncio.Queue):
        while True:
            chunks = []
            while True:
                chunk = await audio_queue.get()
                if chunk is None:
                    audio_queue.task_done()
                    break
                audio_queue.task_done()
                chunks.append(chunk)

            await text_queue.put(chunks)
