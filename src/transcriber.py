from faster_whisper import WhisperModel


class Transcriber:
    def __init__(
        self, model_size: str = "base", device: str = "cpu", compute_type: str = "int8"
    ):
        self.model = WhisperModel(model_size, device, compute_type=compute_type)

    def transcribe(self, audio: any) -> str:
        segments, _ = self.model.transcribe(audio)

        return " ".join([segment.text for segment in segments]).strip()
