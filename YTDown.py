from pytube import YouTube


#Get youtube link from user
link = input("Paste the YouTube video url you wish to download: ")
yt = YouTube(link)

#show video details
print("Title:", yt.title)
print("View count:", yt.views)
print("Video Rating:", yt.rating)

#Get high res copy
ys = yt.streams.get_highest_resolution()

#Download video
print("Starting to download....")
ys.download()
print("Download Finished!")