#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#Title: git clone 体験用のpythonスクリプト
#Author: Issei Iida
#Date: 2019/09/25
#Memo: スクリプトを実行すると音楽が流れます。
#      ファイルたちに実行権限つけてね
#      曲は”Son of a preacher man”
#--------------------------------------------------------------------

#Python関係
from mutagen.mp3 import MP3 as mp3
import pygame.mixer
import time

filename = 'Sarah Connor - Son Of Preacher Man.mp3'
pygame.mixer.init()
pygame.mixer.music.load(filename)
mp3_length = mp3(filename).info.length
pygame.mixer.music.play(1)
time.sleep(mp3_length + 0.25)
pygame.mixer.music.stop()
