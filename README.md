# Farming Simulator 19 Mod Downloader
Simple tool made to automate the downloading of multiple mods for a server. No idea if this is needed for others but it was helpful for downloading a friend's 129 mod list without having to click each individually.

## How to use
- Download the tool from the `Releases` tab
- Launch Farming Simulator 19
- Proceed to join your server
- Select `Details`, then Download All Mods/DLCs
- Copy the URL from your browser
- Launch the FS19Downloader.exe
- Paste the URL into the application
- Once download is completed, mods will be located inside a mods/ folder
- Copy the mod zip files over to your My Games/FarmingSimulator2019/mods folder

## How to build from source
Source is just a single Python file. Building can be done with pyinstaller.

pip install pyinstaller
pyinstaller run.py --onefile