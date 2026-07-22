[app]

# App title
title = Matus AI Controller

# Package name
package.name = matusai

# Package domain
package.domain = org.matus

# Source code location
source.dir = .

# Files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

# Version
version = 1.0.0

# Supported orientation
orientation = portrait

# App requirements
requirements = python3,kivy==2.3.0,cython==0.29.33,requests,pyjnius,android

# Permissions
android.permissions = INTERNET,RECORD_AUDIO,VIBRATE,WRITE_SETTINGS,READ_SETTINGS,ACCESS_NETWORK_STATE,WAKE_LOCK,FOREGROUND_SERVICE

# Android API / SDK / NDK
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Architectures
android.archs = arm64-v8a

# Accept SDK license automatically
android.accept_sdk_license = True

# Keep SDK update enabled
android.skip_update = False

# Stable python-for-android version
p4a.version = 2024.01.21

# Logging
log_level = 2
warn_on_root = 0


[buildozer]

log_level = 2
warn_on_root = 0
