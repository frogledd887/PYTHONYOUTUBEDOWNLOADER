import pytube
link = input('address：')
yt = pytube.YouTube(link)
stream = yt.streams.first()
print("start")
stream.download()
print("finish")