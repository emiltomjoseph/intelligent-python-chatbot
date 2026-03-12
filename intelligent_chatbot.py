import re
import random
from datetime import datetime


# Response database

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "Glad I could help!", "Anytime 😊"],
    "name": ["I am an intelligent Python chatbot.", "You can call me PyBot."],
    "time": [f"Current time is {datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"],
    "positive": ["That sounds great!", "I'm happy to hear that 😊"],
    "negative": ["I'm sorry to hear that 😔", "Hope things get better soon."],
    "neutral": ["I see.", "Okay, tell me more."],
    "default": [
        "Sorry, I didn't understand that.",
        "Could you please rephrase?",
        "I'm still learning 🤖"
    ]
}


# Intent keywords

intents = {
    "greeting": ["hi", "hello", "hey"],
    "farewell": ["bye", "exit", "quit"],
    "thanks": ["thanks", "thank you"],
    "name": ["your name", "who are you"],
    "time": ["time"],
    "date": ["date", "day"]
}



# Sentiment word lists

positive_words = ["good", "happy", "great", "awesome", "nice", "excellent"]
negative_words = ["bad", "sad", "angry", "worst", "poor", "hate"]


# NLP Preprocessing

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


# Intent Detection

def detect_intent(text):
    for intent, keywords in intents.items():
        for word in keywords:
            if word in text:
                return intent
    return None


# Sentiment Analysis

def detect_sentiment(text):
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"


# Chat History Logger

def save_chat(user, bot):
    with open("chat_history.txt", "a") as file:
        file.write(f"You: {user}\nBot: {bot}\n\n")


# Chatbot Engine

def chatbot():
    print("🤖 Intelligent Chatbot Started!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        processed = preprocess(user_input)

        intent = detect_intent(processed)

        if intent == "farewell":
            reply = random.choice(responses["farewell"])
            print("Bot:", reply)
            save_chat(user_input, reply)
            break

        if intent:
            reply = random.choice(responses[intent])
        else:
            sentiment = detect_sentiment(processed)
            reply = random.choice(responses[sentiment])

        print("Bot:", reply)
        save_chat(user_input, reply)


# Run Program

chatbot()
