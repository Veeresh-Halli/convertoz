from django.shortcuts import render, redirect
from django.contrib import messages
import speech_recognition as sr

# Create your views here.

# def convertThread(uploaded_file, request):
#     r = sr.Recognizer()
#     audio_file = sr.AudioFile(uploaded_file)
#     with audio_file as source:
#         print("listing..")
#         audio = r.record(source)
#         try:
#             print("converting...")
#             text = r.recognize_google(audio)
#             print("Wrting to file.....")
#             print(text)
#             f = open('static/converted.txt','w')
#             f.write(text)
#             f.close()
#             context = {'text':text}
#             print(context)
#             return render(request,'index.html', context) 
#         except:
#             messages.error(request,"Sorry, Try again later.........")
    

def index(request):
    text = None
    if request.method == 'POST':
        
        uploaded_file = request.FILES.get('file')
        if uploaded_file is not None:
           wav_file = '.wav'
           if uploaded_file.name[-4:] == wav_file:
             r = sr.Recognizer()
             audio_file = sr.AudioFile(uploaded_file)
             with audio_file as source:
               print("listing..")
               audio = r.record(source)
               try:
                 print("converting...")
                 text = r.recognize_google(audio)
                 print("Wrting to file.....")
                 print(text)
                 f = open('static/converted.txt','w')
                 f.write(text)
                 f.close()
               except:
                 messages.error(request,"Sorry, Try again later.........")
            #  obj = threading.Thread(target=convertThread, args=(uploaded_file,request,))
            #  obj.start()
           else:
             messages.error(request,"We don't support {} files".format(uploaded_file.name[-4:]))
        else:
            messages.error(request, "Please upload a WAV file.....")

    context = {'text':text,}
    return render(request, 'index.html', context)

def aboutus(request):
    return render(request, 'about.html')