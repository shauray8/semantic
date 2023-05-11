from pytube import YouTube, StreamQuery
import re

def filter(
        fps=None,
        res=None,
        resolution=None,
        mime_type=None,
        type=None,
        subtype=None,
        file_extension=None,
        abr=None,
        bitrate=None,
        video_codec=None,
        audio_codec=None,
        only_audio=True,
        only_video=None,
        progressive=None,
        adaptive=None,
        is_dash=None,
        custom_filter_functions=None,
    ):
        filters = []
        if res or resolution:
            if isinstance(res, str) or isinstance(resolution, str):
                filters.append(lambda s: s.resolution == (res or resolution))
            elif isinstance(res, list) or isinstance(resolution, list):
                filters.append(lambda s: s.resolution in (res or resolution))

        if fps:
            filters.append(lambda s: s.fps == fps)

        if mime_type:
            filters.append(lambda s: s.mime_type == mime_type)

        if type:
            filters.append(lambda s: s.type == type)

        if subtype or file_extension:
            filters.append(lambda s: s.subtype == (subtype or file_extension))

        if abr or bitrate:
            filters.append(lambda s: s.abr == (abr or bitrate))

        if video_codec:
            filters.append(lambda s: s.video_codec == video_codec)

        if audio_codec:
            filters.append(lambda s: s.audio_codec == audio_codec)

        if only_audio:
            filters.append(
                lambda s: (
                    s.includes_audio_track and not s.includes_video_track
                ),
            )

        if only_video:
            filters.append(
                lambda s: (
                    s.includes_video_track and not s.includes_audio_track
                ),
            )

        if progressive:
            filters.append(lambda s: s.is_progressive)

        if adaptive:
            filters.append(lambda s: s.is_adaptive)

        if custom_filter_functions:
            filters.extend(custom_filter_functions)

        if is_dash is not None:
            filters.append(lambda s: s.is_dash == is_dash)

        return StreamQuery._filter(filters).order_by("abr").first()

def regex_search(pattern: str, string: str, group: int) -> str:
    regex = re.compile(pattern)
    results = regex.search(string)
    if not results:
        assert ("No such valid URL exits")
    return results.group(group)


## define a function which will get imported from some other file 
def callaback():
    pass

if __name__ == "__main__":
    urls = []
    with open("urls.txt", "r") as file:
        urls.append(file.read().split("\n"))
    print(urls)

    for rl in urls[0][:-1]:
        st = YouTube(rl)
        watch_url = regex_search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", rl, group=1)
        audio_file = st.streams.filter(only_audio=True, subtype="mp4").order_by("abr").first().download(filename = "../Data/"+ watch_url+".mp4")
        print(audio_file)
        author = st.author
        title = st.title
#StreamQuery(st.fmt_streams).get_audio_only()
