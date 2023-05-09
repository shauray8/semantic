import requests

# Replace with your own API key
api_key = '{f}'

# Replace with the ID of the YouTube video you want to convert
video_id = '42QuXLucH3Q'

# Make a request to the YouTube API to retrieve the captions or subtitles
url = f'https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId={video_id}&key={api_key}'
response = requests.get(url)
captions = response.json()['items'][0]
caption_track_url = captions['snippet']['trackKind']
caption_track_response = requests.get(caption_track_url)
text = caption_track_response.text

# Convert the captions or subtitles to the .vtt format
lines = text.strip().split('\n\n')
vtt = 'WEBVTT\n\n'
for i, line in enumerate(lines):
    parts = line.strip().split('\n')
    start = parts[0]
    end = parts[1]
    text = '\n'.join(parts[2:])
    start = start.replace('.', ',')  # Convert from YouTube time format to VTT time format
    end = end.replace('.', ',')  # Convert from YouTube time format to VTT time format
    vtt += f'{i+1}\n{start} --> {end}\n{text}\n\n'

# Write the .vtt file to disk
with open('output.vtt', 'w') as f:
    f.write(vtt)
