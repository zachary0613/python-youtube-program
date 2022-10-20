from sys import argv

from pytube import YouTube

print("Would you like to download audio or video? 1 for audio, 2 for video")
choice = input()

if choice == "1":
    print("Please enter the link of the audio you would like to download")
    link = input()
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("audio")
    yd = yt.streams.get_audio_only()
    yd.download('youtube-audio/')

else:
    print("Please enter the link of the video you would like to download")
    link = input()
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("video")
    yd = yt.streams.get_highest_resolution()
    yd.download('youtube-vid/')





    
#link = argv[1]

#yt = YouTube(link)

#print("Title: ", yt.title)

#print("Views: ", yt.views)

#yd = yt.streams.get_highest_resolution()

#yd.download('youtube-vid/')




