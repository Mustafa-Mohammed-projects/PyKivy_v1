[app]
title = PyKivy
package.name = pykivy
package.domain = org.pyide
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Libraries are compiled INTO the APK at build time (no runtime pip on this path).
# Add more here, e.g.:  python3,kivy==2.3.0,numpy,opencv,pillow,requests
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png
presplash.color = #0E1018

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
