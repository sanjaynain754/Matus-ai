"""
Matus AI Voice Input Module
यह module voice commands को text में convert करता है
Android पर Google Speech Recognition का use करता है
"""

import os

ANDROID = 'ANDROID_ARGUMENT' in os.environ

if ANDROID:
    try:
        from jnius import autoclass
        from android.permissions import request_permissions, Permission
        
        # Request microphone permission
        request_permissions([Permission.RECORD_AUDIO])
        
        # Android classes
        RecognizerIntent = autoclass('android.speech.RecognizerIntent')
        SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        VOICE_READY = True
    except Exception as e:
        print(f"Voice input error: {e}")
        VOICE_READY = False
else:
    VOICE_READY = False
    print("Voice input disabled on desktop")


class VoiceInput:
    """Voice commands को listen और process करने वाला class"""
    
    def __init__(self):
        self.activity = None
        self.recognizer = None
        if VOICE_READY:
            try:
                self.activity = PythonActivity.mActivity
                self.recognizer = SpeechRecognizer.createSpeechRecognizer(self.activity)
            except Exception as e:
                print(f"Recognizer init error: {e}")
    
    def listen_for_command(self, timeout_ms=5000):
        """
        Voice command सुनता है और text return करता है
        """
        if not VOICE_READY:
            return "Error: Voice input Android पर नहीं चल रहा"
        
        try:
            # Create intent for speech recognition
            intent = RecognizerIntent()
            intent.setAction(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, 
                          RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi-IN")  # Hindi + English
            intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
            
            # Start listening
            self.activity.startActivityForResult(intent, 1001)
            
            # Wait for result (simplified - in real app use callback)
            import time
            time.sleep(timeout_ms / 1000)
            
            return "Voice recognition started - implement callback for results"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def is_available(self):
        """Check करता है कि voice input available है या नहीं"""
        return VOICE_READY


# Test
if __name__ == "__main__":
    voice = VoiceInput()
    print(f"Voice input available: {voice.is_available()}")
