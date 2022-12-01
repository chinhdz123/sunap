""" import torch
from transformers import Wav2Vec2ForCTC,Wav2Vec2Processor
import speech_recognition as sr
import io
from pydub import AudioSegment


tokenizer = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-960h')
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')
r = sr.Recognizer()
with sr.Microphone(sample_rate=16000) as source :
    print("You can speak now...")
    while True:
        audio = r.listen(source)
        data = io.BytesIO(audio.get_wav_data())
        clip = AudioSegment.from_file(data)
        x = torch.FloatTensor(clip.get_array_of_samples())

        inputs = tokenizer(x, sampling_rate = 16000, return_tensors = 'pt', padding = 'longest').input_values
        logits = model(inputs).logits
        tokens = torch.argmax(logits,axis=-1)
        text =tokenizer.batch_decode(tokens)
        print('You said: ',str(text).lower())
 """
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import torch
import speech_recognition as sr
import io
from pydub import AudioSegment
AudioSegment.converter = "/usr/local/bin/ffmpeg"
 # load model and tokenizer
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

r = sr.Recognizer()
with sr.Microphone(sample_rate=16000) as source :
    print("You can speak now...")
    while True:
        # load dummy dataset and read soundfiles
        #ds = load_dataset("patrickvonplaten/librispeech_asr_dummy", "clean", split="validation")
        audio = r.listen(source)
        data = io.BytesIO(audio.get_wav_data())
        clip = AudioSegment.from_file(data)
        print("a")
        x = torch.FloatTensor(clip.get_array_of_samples())
        # tokenize
        input_values = processor(x, return_tensors="pt", padding="longest").input_values  # Batch size 1

        # retrieve logits
        logits = model(input_values).logits

        # take argmax and decode
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)
        print('You said: ',str(transcription).lower())