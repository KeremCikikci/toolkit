from pytube import YouTube, Playlist
import ffmpeg

from subprocess import run
import os

def download_video(url, res=None, dir=''):
    yt = YouTube(url)
    
    banned = ['/', '\\', '|', '<', '>', '*', ':', '"', '?']
    
    # bu alttaki satir calisiyormu test edilmedi
    title = ''.join([yt.title.replace(x, '') for x in banned])

    yt.streams.filter(only_audio=True).first().download(filename= dir + title + '_audio.mp4')    
    
    if res == None:
        yt.streams.get_highest_resolution().download(filename=title + '_video.mp4')

    elif res == 'low':
        yt.streams.get_lowest_resolution().download(filename=title + '_video.mp4')

    elif res != None and res != 'audio' and res != 'low':
        yt.streams.filter(res=res).first().download(filename=title + '_video.mp4') # ex: "240p"

    if res != 'audio':
        audio_stream = ffmpeg.input(title + '_audio.mp4')
        video_stream = ffmpeg.input(title + '_video.mp4')

        ffmpeg.output(audio_stream, video_stream, dir + title + '.mp4').run()

        os.remove(title + '_audio.mp4')
        os.remove(title + '_video.mp4')

def download_playlist(url, dir, res=None):
    try:
        os.makedirs(dir)
    except FileExistsError:
        pass

    play_list = Playlist(url)
    
    for yt in play_list:
        download_video(yt, res=res, dir=dir + '/')