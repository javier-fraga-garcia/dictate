import sys
import queue

import sounddevice as sd

SAMPLE_RATE = 16_000
CHANNELS = 1
BLOCK_SIZE = 1024

audio_queue = queue.Queue(maxsize=100)


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)

    audio_queue.put(indata.copy())


if __name__ == "__main__":
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        blocksize=BLOCK_SIZE,
        callback=callback,
    ) as stream:
        try:
            while True:
                print(audio_queue.get())
        except KeyboardInterrupt:
            print("Deteniendo grabación")
