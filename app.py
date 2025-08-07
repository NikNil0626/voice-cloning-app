import gradio as gr
from transformers import pipeline

pipe = pipeline("text-to-speech", model="suno/bark")

def clone_voice(text):
    audio = pipe(text)
    return audio["audio"]

gr.Interface(fn=clone_voice, inputs="text", outputs="audio", title="Father Voice Clone").launch()
