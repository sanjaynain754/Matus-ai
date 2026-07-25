[app]
title = Matus AI
package.name = matusai
package.domain = org.matus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0.0
orientation = portrait
icon.filename = %(source.dir)s/icon.png

# Python 3.14 with Kivy from master branch (Python 3.14 support added)
# Cython 3.1.4+ supports Python 3.14 (cgi module fix)
requirements = python3==3.14.2,kivy,cython==3.1.4,requests

android.permissions = INTERNET, RECORD_AUDIO, VIBRATE, ACCESS_NETWORK_STATE, WAKE_LOCK, FOREGROUND_SERVICE
android.allow_unknown_sources = True
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a

# Use stable p4a master branch
p4a.branch = master

log_level = 2
warn_on_root = 0

[buildozer]
log_level = 2
warn_on_root = 0
