import random
import moviepy.editor as mp
from moviepy.audio.AudioClip import concatenate_audioclips, CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

#texts = ["FACT 1 ABOUT PSICOLOGY", "FACT 2 ABOUT PSICOLOGY", "FACT 3 ABOUT PSICOLOGY"]
texts=['1. Psicology is the science of the mind and behavior, exploring how our experiences shape our thoughts, feelings, and behaviors.', '2. It looks at how our biology, environment, and culture shape our mental and emotional states.', '3. Psicology can help us understand ourselves and others']

def add_captions(texts):
    video = mp.VideoFileClip("./background/test.mp4")
    height = int(video.w * 16 / 9)
    top_crop = int((video.h - height) / 2)
    bottom_crop = video.h - height - top_crop

    video = video.crop(y1=top_crop, y2=video.h-bottom_crop)

    tm=0

    audio_clips = []
    audio_folder = "audio"
    audio_files = [f for f in os.listdir(audio_folder)]
    for audio_file in audio_files:
        audioFileName = os.path.join(audio_folder, audio_file)
        audio_clips.append(AudioFileClip(audioFileName))

    for i, audio in enumerate(audio_clips):
        caption = mp.TextClip(texts[i], fontsize=70, color='white', stroke_width=2, stroke_color='black', method='label', font='Nimbus-Sans-L-Bold')
        caption = caption.set_duration(audio.duration)
        caption = caption.set_start(tm).set_pos("center")
        tm+=audio.duration
        video = mp.CompositeVideoClip([video, caption])
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])
    video.audio = audio_composite
    video = video.set_duration(tm)
    video.write_videofile("output.mp4")

add_captions(texts)
