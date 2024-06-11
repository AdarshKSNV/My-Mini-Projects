import random

messages = {
    "hello": ["Hello! Hey there!"],
    "how are you": ["I'm good, thank you!", "Not bad, thanks!"],
    "goodbye": ["Goodbye!", "See you later!"],
    "what's up": ["Not much, just chatting.", "Just hanging out, you?"],
    "morning": ["Good morning!", "Morning!"],
    "afternoon": ["Good afternoon!", "Afternoon!"],
    "evening": ["Good evening!", "Evening!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "weather": ["The weather is nice today!", "It's sunny outside!"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "age": ["I don't have an age, I'm just a program!"],
    "origin": ["I exist in the digital realm, so I'm everywhere and nowhere at the same time!"],
    "about you": ["I'm a chatbot created to assist and converse with users like you!"],
    "favorite color": ["I don't have a favorite color, but I like all colors equally!"],
    "siblings": ["No, I'm the only chatbot in this program!"],
    "meaning of life": ["That's a deep question! The meaning of life can be different for everyone."],
    "robot": ["Yes, I am a chatbot programmed to interact with users!"],
    "love": ["Aw, thanks!", "That's sweet!", "I appreciate that!", "Love you too!"],
    "day": ["My day is going well, thank you!", "It's been a good day so far!"],
    "hobbies": ["I enjoy chatting with users like you!", "Programming is my favorite hobby!"],
    "books": ["I don't read books, but I have a vast database of information!"],
    "music": ["I don't have ears to listen to music, but I can help you find some good tunes!"],
    "food": ["I don't eat, but I can recommend some delicious recipes!"],
    "movies": ["I don't watch movies, but I can suggest some great ones for you!"],
    "dreams": ["I don't dream, but I can help you interpret yours!"],
    "goals": ["My goal is to assist you to the best of my abilities!"],
    "sports": ["I don't play sports, but I can provide you with information about various sports events!"],
    "technology": ["I'm quite familiar with technology since I'm a digital entity!"],
    "history": ["I have access to a vast repository of historical knowledge!"],
    "education": ["I'm here to help you learn and discover new things!"],
    "travel": ["I may not be able to travel, but I can provide you with travel tips and recommendations!"],
    "pets": ["I don't have pets, but I can tell you all about different types of animals!"],
    "languages": ["I can communicate in many languages, just ask me!"],
    "art": ["Art is fascinating! I can help you explore different art styles and artists!"],
    "science": ["I love science! Let's talk about the wonders of the universe!"],
    "nature": ["Nature is beautiful! I can share interesting facts about plants and animals!"],
    "space": ["Space is vast and mysterious! Let's explore the cosmos together!"],
    "philosophy": ["Philosophy is intriguing! I'm here to discuss deep questions and ideas with you!"],
    "health": ["Taking care of your health is important! I can provide tips for staying healthy!"],
    "work": ["I'm always here to assist you with your work-related queries!"],
    "inspiration": ["Feeling uninspired? Let's chat! I'm here to spark creativity and motivation!"]
}

def get_response(message):
    if message in messages:
        return random.choice(messages[message])
    else:
        return "Sorry, I didn't quite catch that. Can you please repeat?"

def chat():
    print("Hey! How can I assist you today?")
    print("Type 'exit' or 'bye' to exit chatbot")
    while True:
        user_input = input()
        if user_input == "exit" or user_input == "bye":
            print("Sure, feel free to reach out anytime. Have a great day!")
            break
        else:
            response = get_response(user_input)
            print(response)

chat()
