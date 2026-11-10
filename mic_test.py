
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Vision AI - Microphone Test")

st.write("Testing continuous microphone connection...")

def audio_callback(frame):
    print("Audio received:", frame.sample_rate)
    return frame

webrtc_streamer(
    key="mic-test",
    mode=WebRtcMode.SENDONLY,
    audio_frame_callback=audio_callback,
    media_stream_constraints={
        "audio": True,
        "video": False
    }
)
