import asyncio
import threading

from producer import Producer


class Controller:
    def __init__(
        self,
        loop: asyncio.BaseEventLoop,
        audio_queue: asyncio.Queue,
        recording_event: threading.Event,
        shutdown_event: asyncio.Event,
        producer: Producer,
    ):
        self.loop = loop
        self.audio_queue = audio_queue
        self.recording_event = recording_event
        self.shutdown_event = shutdown_event
        self.producer = producer
        self.audio_thread = None

    def toggle_recording(self):
        self.recording_event.set() if not self.recording_event.is_set() else self.recording_event.clear()

        if self.recording_event.is_set():
            print("Grabando...")
            if not self.audio_thread or not self.audio_thread.is_alive():
                self.audio_thread = threading.Thread(target=self.producer.produce, args=(self.recording_event, self.audio_queue, self.loop))
                self.audio_thread.start()
        else:
            print("Grabación pausada...")

    def exit_gracefully(self):
        print("\nCerrando programa...")
        if self.recording_event.is_set():
            self.recording_event.clear()
        self.shutdown_event.set()

    async def wait_for_audio_thread(self):
        if self.audio_thread:
            await asyncio.to_thread(self.audio_thread.join)
