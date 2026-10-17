# PyKivy — Kivy starter (python-for-android / Buildozer)

Separate from the Kotlin PyIDE app: Kivy needs its own SDL2 runtime, so it is built with Buildozer.

## Build on GitHub
Push this folder, open **Actions -> Build Kivy APK**, download **PyKivy-apk**.
The first build takes 20-40 minutes (it compiles Python and Kivy).

## Customize
- Your image: replace `data/presplash.png` (and `data/icon.png`). The app shows it for 3 seconds.
- Libraries: edit `requirements` in `buildozer.spec` (numpy, opencv, pillow, requests...).
  They are compiled into the APK; there is no runtime `pip install` here.
- Your app code: edit `main.py`.
