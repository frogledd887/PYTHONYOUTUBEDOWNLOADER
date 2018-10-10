"""
from pytube import YouTube
link = 'https://www.youtube.com/watch?v=jG7dSXcfVqE'
yt = YouTube(link)
video = yt.filter("3gp")[-1]
video.download("D:\\tem")
"""

"""

import pytube

var link
link = input('address¡G')
#link = "https://www.youtube.com/watch?v=WCpHAWsnS-4&index=138&t=0s&list=WL"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()


"""



import pytube
link = input('address¡G')
yt = pytube.YouTube(link)
stream = yt.streams.first()
print("start")
stream.download()
print("finish")


"""
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=I6EDoKjS6Ok")
stream = yt.streams.first()

stream = yt.streams.filter(file_extension='mp4', res='720').first() this is wrong sentence
stream.download("D:\\tem")
"""
