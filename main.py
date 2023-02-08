import GenerateTexts
import CreateVideo
import audio
import upload_video
import sys

topic = sys.argv[1]

texts = GenerateTexts.get_facts(topic)
audio.generate_audio(texts)
CreateVideo.add_captions(texts)
upload_video.simple_upload("output.mp4", topic+"Facts")