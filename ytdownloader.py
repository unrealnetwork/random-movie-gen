import pytube #pip install pytube (windows) / sudo pacman -S python-pytube (arch linux) / pipx install pytube (any other linux) / pip3 install pytube (mac)
from pytube import YouTube 
import os #pre-loaded in python so you dont have to install it externally

def download_youtube_video(video_link, save_path, quality):
    yt = YouTube(video_link)
    video_streams = yt.streams.filter(progressive=True)
    
    available_qualities = [stream.resolution for stream in video_streams]
    
    if quality not in available_qualities:
        print("Chosen quality is not available for this video.")
        return
    
    chosen_stream = video_streams[available_qualities.index(quality)]
    print(f"Downloading video in {quality}...")
    chosen_stream.download(output_path=save_path, filename="downloaded_video")
    print("Download completed!")

def main():
    print("------UNREAL YOUTUBE DOWNLOADER------")
    video_link = input("\nYour YouTube video link: ")

    save_path = "/home/aneek/Documents/"  # paste the correct path in which you want the video to be saved

    print("Choose your video quality:")
    yt = YouTube(video_link)
    video_streams = yt.streams.filter(progressive=True)
    
    available_qualities = [stream.resolution for stream in video_streams]
    
    for i, quality in enumerate(available_qualities, 1):
        print(f"{i}. {quality}")
    
    quality_choice = int(input("\nInput any quality: ")) - 1
    
    chosen_quality = available_qualities[quality_choice]

    download_youtube_video(video_link, save_path, chosen_quality)

if __name__ == "__main__":
    main()
