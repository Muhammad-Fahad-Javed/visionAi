
import sounddevice as sd
import wave

device_id = 1
sample_rate = int(sd.query_devices(device_id)["default_samplerate"])

print("Microphone:", sd.query_devices(device_id)["name"])
print("Recording started... Speak now!")

recording = sd.rec(
    int(5 * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    device=device_id
)

sd.wait()

print("Recording completed!")

with wave.open("mic_test.wav", "wb") as file:
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setframerate(sample_rate)
    file.writeframes(recording.tobytes())

print("Audio saved as mic_test.wav")
