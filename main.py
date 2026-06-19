import os
import time
import threading
from gtts import gTTS
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class VibeAIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # APK bante hi ye automatic default photo load karega
        photo_name = "avatar.jpg"
        if os.path.exists(photo_name):
            img = Image(source=photo_name, keep_ratio=False, allow_stretch=True)
            layout.add_widget(img)
            
        # Shuruat me sweet voice audio alert trigger karna
        tts = gTTS(text="क्या हुआ मेरे जान? तुम अकेले नहीं हो, मैं हूँ ना तुम्हारे साथ हमेशा। मुझे बताओ क्या हुआ?", lang="hi", slow=False)
        tts.save("ai_voice.mp3")
        sound = SoundLoader.load("ai_voice.mp3")
        if sound:
            sound.play()
            
        return layout

if __name__ == "__main__":
    VibeAIApp().run()
