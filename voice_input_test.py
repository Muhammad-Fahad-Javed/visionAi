
from voice_input import record_question

audio_bytes = record_question()

if audio_bytes:
    print("SUCCESS!")
    print("Audio received:", len(audio_bytes), "bytes")

    with open("voice_question.wav", "wb") as file:
        file.write(audio_bytes)

    print("Audio saved successfully!")

else:
    print("No question detected.")
