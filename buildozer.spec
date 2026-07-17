# Matus AI Controller - Complete Buildozer Configuration
# यह फाइल Buildozer को बताती है कि APK कैसे बनाना है
# हर एक सेटिंग को ध्यान से कॉन्फ़िगर किया गया है

[app]

# (str) Title of your application
# यह नाम APK और इंस्टॉल होने के बाद दिखेगा
title = Matus AI Controller

# (str) Package name
# यह Android का internal package name है (unique होना चाहिए)
package.name = matusai

# (str) Package domain (needed for android/ios packaging)
# यह तुम्हारी organization या project का domain है
package.domain = org.matus

# (str) Source code where the main entry live
# यह बताता है कि main.py कहाँ है (current directory में)
source.dir = .

# (list) Source files to include (let empty to include all the files)
# यह बताता है कि कौन सी फाइलें APK में शामिल करनी हैं
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,html,css,js

# (str) Application versioning (method 1)
# APK का version number
version = 1.0.0

# (list) Application requirements
# यह सबसे IMPORTANT लाइन है - यहाँ सारी dependencies लिखी हैं
# CRITICAL FIX: python3==3.11 force किया गया है ताकि Python 3.14 download न हो
# Kivy 2.3.0 stable version है जो Python 3.11 के साथ perfectly काम करता है
# Cython 0.29.33 Kivy 2.3.0 के साथ compatible है
requirements = python3==3.11,kivy==2.3.0,cython==0.29.33,requests,pyjnius,android

# (str) Presplash of the application
# यह वह image है जो app लोड होते समय दिखता है (optional)
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# यह app का icon है (optional)
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
# App किस orientation में चलेगा
orientation = portrait

# (bool) Fullscreen mode
# App fullscreen में चलेगा या नहीं
fullscreen = 0

# (list) Permissions
# यह सभी permissions हैं जो app को चाहिए
# INTERNET - Web search के लिए
# RECORD_AUDIO - Voice input के लिए
# VIBRATE - Vibration feedback के लिए
# WRITE_SETTINGS - Brightness change करने के लिए
# READ_SETTINGS - Battery level read करने के लिए
# ACCESS_NETWORK_STATE - Network check करने के लिए
# WAKE_LOCK - Background में चलने के लिए
# FOREGROUND_SERVICE - Service चलाने के लिए
# RECEIVE_BOOT_COMPLETED - Phone restart के बाद auto-start के लिए
android.permissions = \
    INTERNET, \
    RECORD_AUDIO, \
    VIBRATE, \
    WRITE_SETTINGS, \
    READ_SETTINGS, \
    ACCESS_NETWORK_STATE, \
    WAKE_LOCK, \
    FOREGROUND_SERVICE, \
    RECEIVE_BOOT_COMPLETED

# (bool) Allow installation from unknown sources
# यह allow करता है कि app unknown sources से install हो सके
android.allow_unknown_sources = True

# (int) Target Android API, should be as high as possible
# यह latest Android version को target करता है
android.api = 33

# (int) Minimum API your APK / AAB will support
# यह minimum Android version है जिस पर app चलेगा (Android 5.0+)
android.minapi = 21

# (int) Android SDK version to use
# यह Android SDK का version है
android.sdk = 33

# (str) Android NDK version to use
# यह Android NDK का version है (C/C++ compilation के लिए)
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# यह automatic SDK update को रोकता है
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# यह SDK license को automatically accept करता है
android.accept_sdk_license = True

# (str) The Android arch to build for
# यह बताता है कि APK किस processor architecture के लिए बनेगा
# arm64-v8a - 64-bit phones के लिए (modern phones)
# armeabi-v7a - 32-bit phones के लिए (older phones)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX
# यह modern Android libraries को enable करता है
android.enableandroidx = True

#
# Python-for-Android (p4a) specific settings
# यह सबसे CRITICAL section है - यहाँ Python version force किया गया है
#

# (str) Force python-for-android to use this Python version
# यह line Buildozer को जबरदस्ती Python 3.11 use करने पर मजबूर करती है
# यह Python 3.14 download होने की problem को 100% fix करती है
p4a.python_version = 3.11

# (str) python-for-android branch to use
# यह stable master branch use करता है (develop branch Python 3.14 लाता है)
p4a.branch = master

# (str) python-for-android version to use
# यह specific stable version use करता है
p4a.version = 2024.01.21

# (str) python-for-android fork to use
# यह default Kivy fork use करता है
p4a.fork = kivy

# (str) python-for-android URL to use for checkout
# यह default URL use करता है
#p4a.url = https://github.com/kivy/python-for-android.git

# (str) python-for-android specific commit to use
# यह latest commit use करता है (HEAD)
#p4a.commit = HEAD

# (str) python-for-android git clone directory
# यह default directory use करता है
#p4a.source_dir =

# (list) python-for-android extra arguments
# यह extra arguments pass करता है (अगर जरूरत हो)
#p4a.extra_args =

#
# Logging
#

# (str) Log level (0 = error only, 1 = info, 2 = debug (with command output))
# यह build के दौरान कितना detail दिखाना है (2 = full debug)
log_level = 2

# (str) Display warning if buildozer is run as root (0 = False, 1 = True)
# यह root user पर warning दिखाता है
warn_on_root = 0

#
# Version-specific settings
#

# (str) Path to a custom kivy-ios folder (iOS only, ignore for Android)
#ios.kivy_ios_dir = ../kivy-ios

# (str) Path to a custom kivy-ios checkout (iOS only, ignore for Android)
#ios.kivy_ios_branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
# यह buildozer का own log level है
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
# यह root user पर warning दिखाता है
warn_on_root = 0

# (str) Path to buildozer storage directory
# यह build files कहाँ store होंगी
#build_dir = .buildozer

# (str) Path to build output (i.e. .apk) directory
# यह APK कहाँ save होगा
#bin_dir = bin
