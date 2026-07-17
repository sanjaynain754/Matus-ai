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
# यहाँ सारी dependencies डालो
requirements = python3,kivy,requests,pyjnius,android

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
# यह बहुत important है - सारे permissions यहाँ डालो
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

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Android additional libraries to copy
#android.add_libs_armeabi = libs/android/armeabi/*.so
#android.add_libs_armeabi_v7a = libs/android/armeabi-v7a/*.so
#android.add_libs_arm64_v8a = libs/android/arm64-v8a/*.so
#android.add_libs_x86 = libs/android/x86/*.so
#android.add_libs_mips = libs/android/mips/*.so

# (bool) decides whether to use p4a or gradlew
#android.enableandroidx = True

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD
#p4a.commit = HEAD

# (str) python-for-android git clone directory
#p4a.source_dir =

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
