#Imported Packages
import os
import glob
import subprocess

#Allows the user to pick the directory they want to execute the files from
directory = input("Enter the directory path where you would like to execute your files: ").strip()

#Detects if the directory is valid or not
if not os.path.isdir(directory):
    print("Error: This directory doesn't exist")
    exit()

#Allows the user to pick what type of files they want to execute
file_extension = input("Enter the file extension of the files you would like to execute (.mp3, .mp4, .exe, etc) ").strip()

#Detects if the file type is valid or not
if not file_extension.startswith("."):
    print("Error: Please enter a valid file extension (.mp3, .mp4, .exe)")

#The rest of this is checks and balances to execute the requested file types in the requested directory
files = [f for f in os.listdir(directory) if f.endswith(file_extension)]

if not files:
    print(f"No {file_extension} files found in directory")
else:
    print(f"Found {len(files)} {file_extension} files. Executing them now")

for file in files:
    print(f"Playing {file}...")
    subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Tells the user the files have been executed
print("All files played.")