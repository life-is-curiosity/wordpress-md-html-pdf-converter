#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.6 (21G115) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.8 ('v3.10.8:aaaf517424', 'Oct 11 2022 10:14:40')
# Created By  : Jeromie Kirchoff (JayRizzo)
# Created Date: Tue Jul 13 20:52:32 2021 CST
# Last ModDate: Sat Nov 26 19:56:32 2022 CST
# =============================================================================
"""This Module Has Been Build For Downloading The Highest Quality Video & Audio Of A YouTube Video."""
# =============================================================================
from os import path as ospath
from pytube import YouTube
CURRENT_HOME = "C:\\Users\\alan9\\OneDrive\\桌面"
VIDEO_FILE_PATH = ospath.join(CURRENT_HOME, '', '')
AUDIO_FILE_PATH = ospath.join(CURRENT_HOME, '',  '')

def getYTVid(URL):
    """Get Highest Quality Video from YT URL."""
    YT = YouTube(URL)
    try:
        print(f"Downloading Video: {YT.title}")
        YTVIDEO_FILE_PATH = YT.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(VIDEO_FILE_PATH)
        print(f"Download Video Completed: {YTVIDEO_FILE_PATH}\\n")
    except Exception as e:
        print(f"Error: {e}")

def getYTAudio(URL):
    """Get Highest Quality Audio from YT URL."""
    YT = YouTube(URL)
    try:
        YTAUDIO_FILE_PATH = YT.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download(AUDIO_FILE_PATH)
        print(f"Download Video Completed: {YTAUDIO_FILE_PATH}\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    links = ["https://www.youtube.com/watch?v=MedrWQe7xn8"]
    for link in links:
        print("Downloading ", link)
        getYTAudio(link)