import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
	recognizer.pause_threshold = 1
	with microphone as source:
		recognizer.adjust_for_ambient_noise(source) # analyze the audio source for 1 second
		audio = recognizer.listen(source)

	response = {
				'success' : True,
				'error' : None,
				'transcription' : None
				}

	try:
		response['transcription'] = recognizer.recognize_google(audio, language='ko-KR')
		return response['transcription']
	except sr.RequestError:
		# API was unreachable or unresponsive
		response['success'] = False
		response['error'] = 'Error - API unavailable/unresponsive'
		return response['error']
	except sr.UnknownValueError:
		# speech was unintelligible
		response['error'] = 'Error - Unable to recognize speech'
		return response['error']


if __name__ == '__main__':
	recognizer = sr.Recognizer()
	mic = sr.Microphone(device_index=1)
	#response = recognize_speech_from_mic(recognizer, mic)