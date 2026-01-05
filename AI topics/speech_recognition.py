import speech_recognition as sr

# recognizer object
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak something...")
    audio = r.listen(source)
    print("Processing...")

try:
    text = r.recognize_google(audio)
    print("📝 You said:", text)
except Exception as e:
    print("❌ Error:", str(e))
