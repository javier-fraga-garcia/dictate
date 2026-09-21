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

    def toggle_recording(self):
        self.recording_event.set() if not self.recording_event.is_set() else self.recording_event.clear()

        if self.recording_event.is_set():
            print("Grabando...")
        else:
            print("Grabación pausada...")

    def exit_gracefully(self):
        print("\nCerrando programa...")
        self.shutdown_event.set()
