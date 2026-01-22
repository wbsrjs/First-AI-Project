import os, sys; os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips # type: ignore
import os

# 1. 6 张图 + 1 首 30s 音乐已上传，确认文件名
clips = [ImageClip(f"img{i}.jpg").set_duration(5).fadein(0.5).fadeout(0.5)
         for i in range(1, 7)]

video = concatenate_videoclips(clips, method="compose")
audio = AudioFileClip("bgm.mp3").subclip(0, 30)
final = video.set_audio(audio)

out = "emoMV.mp4"
final.write_videofile(out, fps=24, audio_codec="aac", logger=None)
print("✅ 完成！左侧出现 emoMV.mp4，右键 Download 下载到本地")