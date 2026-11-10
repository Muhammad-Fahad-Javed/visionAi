
import streamlit as st

from PIL import Image

from ai_engine import (
    describe_scene,
    ask_question,
    ask_question_by_voice,
    text_to_speech
)

from voice_input import record_question


# Page configuration
st.set_page_config(
    page_title="Vision AI",
    page_icon="👁️",
    layout="centered"
)


# Application heading
st.title("👁️ Vision AI")

st.subheader("A Second Pair of Eyes")

st.write(
    "Your AI-powered visual assistant "
    "for understanding your surroundings."
)


# Accessibility information
st.info(
    "Vision AI is an assistive tool. "
    "Do not rely on it alone for navigation or safety."
)


# Camera section
st.header("Camera")

camera_image = st.camera_input(
    "Capture your surroundings"
)


# Process captured image
if camera_image is not None:

    image = Image.open(camera_image).convert("RGB")

    st.image(
        image,
        caption="Captured Image",
        width="stretch"
    )

    st.success("Image captured successfully!")


    # Scene description
    st.header("Describe My Surroundings")

    if st.button("Describe Scene"):

        with st.spinner("Vision AI is analyzing..."):

            try:

                description = describe_scene(image)

                st.subheader("AI Description")

                st.write(description)

            except Exception as error:

                st.error(
                    "Unable to analyze image. "
                    "Please check your API key and internet connection."
                )

                st.exception(error)


    # Ask a question using text
    st.header("Ask Vision AI")

    question = st.text_input(
        "Ask a question about your surroundings",
        placeholder="What is in front of me?"
    )

    if st.button("Ask Question"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                try:

                    answer = ask_question(
                        image,
                        question
                    )

                    st.subheader("Vision AI Response")

                    st.write(answer)

                except Exception as error:

                    st.error(
                        "Unable to answer your question. "
                        "Please check your API configuration."
                    )

                    st.exception(error)


    # Hands-free Voice Assistant
    st.header("🎙️ Hands-Free Voice Assistant")

    st.write(
        "Click the button once, speak your question, "
        "and remain silent when you finish."
    )

    if st.button("Start Voice Question"):

        try:

            with st.spinner("Vision AI is listening..."):

                audio_bytes = record_question()

            if audio_bytes is None:

                st.warning("No speech detected. Please try again.")

            else:

                with st.spinner("Vision AI is thinking..."):

                    answer = ask_question_by_voice(
                        image,
                        audio_bytes
                    )

                st.subheader("Vision AI Response")

                st.write(answer)

                speech = text_to_speech(answer)

                st.audio(
                    speech,
                    format="audio/mp3",
                    autoplay=True
                )

        except Exception as error:

            st.error(
                "Unable to process your voice question."
            )

            st.exception(error)


else:

    st.info(
        "Please capture an image to start using Vision AI."
    )
