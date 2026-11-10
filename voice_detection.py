
import sounddevice as sd
import numpy as np
import wave
import time

device_id = 1

sample_rate = int(
    sd.query_devices(device_id)["default_samplerate"]
)

block_duration = 0.2
silence_limit = 2
volume_threshold = 500

block_size = int(sample_rate * block_duration)

print("Vision AI Voice Detection")
print("Start speaking...")

recorded_audio = []
speaking = False
silence_duration = 0

try:
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

                if not speaking:
                    print("Speech detected!")
                    speaking = True

                silence_duration = 0
                recorded_audio.append(audio.copy())

            elif speaking:

                recorded_audio.append(audio.copy())
                silence_duration += block_duration

                if silence_duration >= silence_limit:
                    print("Speech completed!")
                    break

    if recorded_audio:

        audio_data = np.concatenate(recorded_audio)

        with wave.open("detected_question.wav", "wb") as file:
            file.setnchannels(1)
            file.setsampwidth(2)
            file.setframerate(sample_rate)
            file.writeframes(audio_data.tobytes())

        print("Question saved successfully!")

except KeyboardInterrupt:
    print("Stopped by user.")
