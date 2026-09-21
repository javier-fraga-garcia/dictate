import asyncio
import threading
import sounddevice as sd


class Producer:
    @staticmethod
    def produce(
        recording_event: threading.Event,
        queue: asyncio.Queue,
        loop: asyncio.BaseEventLoop,
    ):

        print("Iniciando lectura de micrófono...")
        try:
            with sd.InputStream(
                samplerate=16_000, blocksize=1024, channels=1, dtype="float32"
            ) as stream:
                while recording_event.is_set():
                    chunk, overflowed = stream.read(1024)
                    if overflowed:
                        print("Overflow del sistema")
                    loop.call_soon_threadsafe(queue.put_nowait, chunk)
        except Exception as e:
            print(f"Error de hardware: {e}")
