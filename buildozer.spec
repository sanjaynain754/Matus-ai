[app]

# (str) Title of your application
title = Matus AI Controller

# (str) Package name
package.name = matusai

# (str) Package domain (needed for android/ios packaging)
package.domain = org.matus

# (str) Source code where the main entry live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# IMPORTANT: Python 3.11.10 specify किया है (3.14 बहुत नया है)
requirements = python3==3.11.10,kivy==2.4.0,requests,pyjnius,android

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# Android specific
#

# (list) Permissions
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
android.allow_unknown_sources = True

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

#
# Logging
#

# (str) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

#
# Version-specific settings
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
