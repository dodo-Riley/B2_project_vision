# # -*- coding: utf-8 -*-
# """
# Created on Wed Mar 16 16:46:28 2022

# @author: rkdtk
# """
# ## 구글
# from gtts import gTTS
# import playsound

# def speak(text): 
#     tts = gTTS(text=text, lang='ko') 
#     tts.save('./voice.mp3') 
      
# speak("안녕하세요, 저는 구글이에요.")
# playsound.playsound('voice.mp3')


## 카카오
import requests

REST_API_KEY = "711abd7d0f4635604fd74ee3e3c6305f"

class KakaoTTS:

	def __init__(self, text, API_KEY=REST_API_KEY):
		self.resp = requests.post(
			url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
			headers={
				"Content-Type": "application/xml",
				"Authorization": f"KakaoAK {API_KEY}"
			},
			data=f"<speak>{text}</speak>".encode('utf-8')
		)

	def save(self, filename="output.mp3"):
		with open(filename, "wb") as file:
			file.write(self.resp.content)


if __name__ == '__main__':
    tts = KakaoTTS("안녕하세요, 저는 카카오에요.")
    tts.save("output.mp3")
    playsound.playsound('output.mp3')