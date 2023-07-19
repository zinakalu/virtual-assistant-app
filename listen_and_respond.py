import speech_recognition as sr
import nltk
import os
import yelp
import music_download 

from nltk.corpus import stopwords
from gtts import gTTS
from playsound import playsound
from ask_gpt3 import ask_gpt3
from news import get_news
from weather import kelvin_to_celsius_fahrenheit, get_weather
from location import get_location


nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

r = sr.Recognizer()

def get_keywords(text):
    words = nltk.word_tokenize(text)
    keywords = [word for word in words if word not in stop_words]
    return keywords


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)



def listen_and_respond():
    with sr.Microphone() as source:
        speak("Talk")
        audio_text = r.listen(source)
    
    try:
        recognized_text = r.recognize_google(audio_text)
        print("Recognized Text:", recognized_text)

        question = recognized_text.lower()

        if "weather" in question:
            respond_to_weather_request(question)

        elif "news" in question:
            respond_to_news_request(question)

        elif "restaurant" in question or "food" in question or "to eat" in question or "eat" in question or "drink" in question or "restaurants" in question:
            yelp.respond_to_yelp_request(question, speak)

        elif "where am I" in question or "what is my current location" in question or "location" in question:
            current_location = get_location()
            speak(f"Your current location is {current_location}.")

        elif "play" in question:
            song_name = extract_song_name(question)
        
        elif "download" in question:
            song_name = extract_song_name(question)

        else:
            respond_to_general_request(question)

    except sr.UnknownValueError:
        print("Speech Recongition could not understand audio")

def respond_to_weather_request(question):
    city = question.split("in")[-1].strip()
    weather_info = get_weather(city)
    speak(weather_info)


def respond_to_news_request(question):
    topic = None

    if "sports" in question:
        topic = "sports"
    elif "news" in question:
        topic = "news"
    

    if topic:
        news_data = get_news(topic)
        print("News Data:", news_data)  # Check the retrieved news data

        if news_data["totalResults"] > 0:
            articles = news_data["articles"]
            speak(f"Here are the top 3 news articles related to your question:")
            for i, article in enumerate(articles[:3], start=1):
                speak(f"News {i}: {article['title']}")
        else:
            speak(f"There are no news articles about {topic} today.")

    else:
        speak("I'm sorry, I currently don't have news information available for that topic.")

        

def respond_to_general_request(question):
    response = ask_gpt3(question)
    speak(response)
    

listen_and_respond()