[app]
title = Matus AI Controller
package.name = matusai
package.domain = org.matus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
orientation = portrait

# CRITICAL FIX: Exact syntax for python-for-android
requirements = python3==3.11,kivy==2.3.0,cython==0.29.33,requests,pyjnius,android

android.permissions = INTERNET, RECORD_AUDIO, VIBRATE, WRITE_SETTINGS, READ_SETTINGS, ACCESS_NETWORK_STATE, WAKE_LOCK, FOREGROUND_SERVICE
android.allow_unknown_sources = True
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a

# THE MAGIC BULLET: Force stable branch to prevent Python 3.14 download
p4a.branch = develop
p4a.version = 2024.01.21

log_level = 2
warn_on_root = 0

[buildozer]
log_level = 2
warn_on_root = 0
