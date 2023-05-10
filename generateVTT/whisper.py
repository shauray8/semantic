import whisper 

model = whisper.load_model("base")
result = model.transcribe("../Data/Testing if Sharks Can Smell a Drop of Blood.mp4")
print(result["text"])
