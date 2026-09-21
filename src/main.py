import os
import asyncio
import threading
import signal

from producer import Producer
from controller import Controller


async def main():
    loop = asyncio.get_event_loop()
    shutdown_event = asyncio.Event()
    recording_event = threading.Event()
    queue = asyncio.Queue(maxsize=100)
    producer = Producer()

    controller = Controller(loop, queue, recording_event, shutdown_event, producer)

    loop.add_signal_handler(signal.SIGUSR1, controller.toggle_recording)
    loop.add_signal_handler(signal.SIGTERM, controller.exit_gracefully)
    loop.add_signal_handler(signal.SIGINT, controller.exit_gracefully)

    print(f"Programa activo, identificador del proceso: {os.getpid()}")
    print("Esperando señales...")

    await shutdown_event.wait()

    print("Limpieza finalizada, cerrando programa")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCerrando programa...")
