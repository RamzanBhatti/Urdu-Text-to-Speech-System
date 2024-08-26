import os
import streamlit as st
from tts import convert_to_audio

def main():
    st.header('Urdu Text To Speech')
    user_input = st.text_input('Enter your Urdu Text ...')
    if user_input:
        convert_to_audio(user_input)    
        # st.audio('/techno.wav')
        st.audio("techno.wav", format="audio/wav", loop=False)

if __name__ == '__main__':
    main()