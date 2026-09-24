import asyncio
import numpy as np

from transcriber import Transcriber


class Consumer:
    def __init__(
        self,
        transcriber: Transcriber,
        audio_queue: asyncio.Queue,
        text_queue: asyncio.Queue,
    ):
        self.transcriber = transcriber
        self.audio_queue = audio_queue
        self.text_queue = text_queue

    async def consume(self):
        while True:
            chunks = []
            while True:
                chunk = await self.audio_queue.get()
                if chunk is None:
                    self.audio_queue.task_done()
                    break
                self.audio_queue.task_done()
                chunks.append(chunk)
            audio_array = np.concatenate(chunks).squeeze()
            transcription = self.transcriber.transcribe(audio_array)
            await self.text_queue.put(transcription)
