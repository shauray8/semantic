from pytube import YouTube

# Ask the user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object from the URL
yt = YouTube(url)

# Get the highest resolution video stream
stream = yt.streams.get_lowest_resolution()

# Download the video
print("Downloading...")
stream.download()
print("Download complete!")

