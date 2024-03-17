import cv2
from moviepy.editor import *
#from pytube import YouTube

'''
video_url = "https://www.youtube.com/watch?v=sunVrbz2lAw"

def download_youtube_video(video_url, output_path):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path=output_path, filename='youtube_video')

def load_youtube_video(video_url):
    download_youtube_video(video_url, './')
    return VideoFileClip("youtube_video.mp4")
'''

vid_clip = VideoFileClip("test.mp4")
bg_vidclip = VideoFileClip("test.mp4")
clip_duration = 210
count = 1

target_width = bg_vidclip.size[0]
target_height = int(target_width * 16 / 9)
bg_vidclip = bg_vidclip.resize((target_width, target_height))

vid_clip = vid_clip.resize(width = vid_clip.w, height = vid_clip.w)
'''
subtitles = [
    {'text': 'Subtitle 1', 'font_size': 30, 'color': 'white', 'font': 'C:\Windows', 'position': ('center', 'bottom')},
    {'text': 'Subtitle 2', 'font_size': 30, 'color': 'white', 'font': 'C:\Windows', 'position': ('center', 'top')}
]
'''
if bg_vidclip.size[1] < target_height:
    # Padding is required
    padding = ((0, target_height - bg_vidclip.size[1]), (0, 0))  # Padding only on height
    bg_vidclip = bg_vidclip.pad(width=target_width, height=target_height, padding=padding, color=(255, 255, 255))
elif bg_vidclip.size[1] > target_height:
    # Cropping is required
    crop_y = (bg_vidclip.size[1] - target_height) // 2
    bg_vidclip = bg_vidclip.crop(y1=crop_y, y2=crop_y + target_height)

'''
def add_subtitles(video_clip, subtitles):
    subtitle_clips = []
    for subtitle in subtitles:
        subtitle_clip = TextClip(subtitle['text'], fontsize=subtitle['font_size'], color=subtitle['color'], font=subtitle['font'])
        subtitle_clip = subtitle_clip.set_position(subtitle['position']).set_duration(video_clip.duration)
        subtitle_clips.append(subtitle_clip)
    return CompositeVideoClip([video_clip] + subtitle_clips)
'''

def blur_frame(frame):
    blurred_frame = cv2.GaussianBlur(frame, (0,0), sigmaX=20)
    return blurred_frame

#final_clip = add_subtitles(bg_vidclip, subtitles)
bg_vidclip = bg_vidclip.fl_image(blur_frame)
final_clip = CompositeVideoClip([bg_vidclip.set_duration(vid_clip.duration), vid_clip.set_position(('center', 'center'))])
total_duration = final_clip.duration

for i in range(0, int(total_duration), clip_duration):
    video_part = final_clip.subclip(i, min(i+clip_duration, total_duration))
    video_part.write_videofile(r'C:\Lavan\TikTok Edit Automator_{}.mp4'.format(count), codec="libx264", audio_codec="aac")
    count += 1

vid_clip.close()

