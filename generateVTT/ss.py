from facebookWhisper import whisper

model = whisper.load_model("base.en")
audio = model.transcribe("../Data/2JAOTJxYqh8.mp4")
print(result)



