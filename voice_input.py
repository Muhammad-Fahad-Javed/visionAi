
import sounddevice as sd
import numpy as np
import wave
from io import BytesIO


def record_question():

    device_id = 1

    sample_rate = int(
        sd.query_devices(device_id)["default_samplerate"]
    )

    block_duration = 0.2
    silence_limit = 1.5
    volume_threshold = 500
    max_wait = 15

    block_size = int(sample_rate * block_duration)

    recorded_audio = []
    speaking = False
    silence_duration = 0
    wait_duration = 0

    print("Vision AI is listening... Speak now!")

    with sd.InputStream(
        device=device_id,
        channels=1,
        samplerate=sample_rate,
        blocksize=block_size,
        dtype="int16"
    ) as stream:

        while True:

            audio, overflowed = stream.read(block_size)

            volume = np.sqrt(
                np.mean(audio.astype(np.float32) ** 2)
            )

            if volume > volume_threshold:

                speaking = True
                silence_duration = 0
                recorded_audio.append(audio.copy())

            elif speaking:

                recorded_audio.append(audio.copy())
                silence_duration += block_duration

                if silence_duration >= silence_limit:
                    break

            else:

                wait_duration += block_duration

                if wait_duration >= max_wait:
                    print("No speech detected.")
                    return None

    if not recorded_audio:
        return None

    audio_data = np.concatenate(recorded_audio)

    audio_buffer = BytesIO()

    with wave.open(audio_buffer, "wb") as file:

        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(sample_rate)
        file.writeframes(audio_data.tobytes())

    print("Question recorded successfully!")

    return audio_buffer.getvalue()
