from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile
import numpy as np

model = VitsModel.from_pretrained("Ramxan/syb-fyp-02")
tokenizer = AutoTokenizer.from_pretrained("Ramxan/syb-fyp-02")

# text = """
# خودی کو کر بلند اتنا کہ ہر تقدیر سے پہلے
# خدا بندے سے خود پوچھے، بتا تیری رضا کیا ہے

# """

def convert_to_audio(text):
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

    output_numpy = output.squeeze().cpu().numpy()
    # Save the waveform to a WAV file
    scipy.io.wavfile.write("techno.wav", rate=model.config.sampling_rate, data=output_numpy)