import random
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize NLTK components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define a list of possible responses
greetings = ["Hello! Welcome to the Agriculture Chatbot. How can I assist you today?",
             "Hi there! What can I help you with today?",
             "Welcome to the Agriculture Chatbot! How may I assist you?"]

crop_management = ["What kind of crops are you interested in?",
                   "Which crop would you like to know more about?",]
                   
corn_management = ["The best time to plant corn is typically when soil temperatures reach at least 50°F at a depth of 2 inches.",
                   "There are a variety of fertilizers that can be used for corn, depending on the needs of your specific crop.",
                   "Common pests that affect corn include corn earworm, fall armyworm, and corn rootworm. Common diseases include northern corn leaf blight, gray leaf spot, and common rust.",
                   "For optimal corn growth, it's important to monitor soil moisture and temperature, as well as ensure that the crop receives adequate nutrients.",
                   "Crop rotation can be an effective strategy for reducing pests and diseases in corn fields."]

soil_management = ["Soil health is essential for successful crop growth. Factors that affect soil health include nutrient levels, pH, and soil structure.",
                   "Cover crops and compost can be effective ways to improve soil health and reduce erosion.",
                   "Soil testing is an important tool for monitoring soil health and determining nutrient needs for crops."]

fertilizer_management = ["When it comes to fertilizer management, it's important to consider factors such as soil nutrient levels, crop needs, and environmental impact.",
                         "Organic fertilizers can be effective alternatives to synthetic fertilizers, as they promote soil health and reduce environmental impact.",
                         "Overuse of fertilizers can lead to nutrient pollution in waterways, so it's important to apply them carefully and in appropriate amounts."]

pest_management = ["Integrated pest management (IPM) is a holistic approach to pest control that emphasizes preventative measures and minimal use of pesticides.",
                   "Crop rotation and intercropping can be effective ways to reduce pest pressure in fields.",
                   "Biological control methods, such as introducing natural predators of pests, can be effective and environmentally friendly ways to manage pests."]

goodbyes = ["Thank you for chatting with me. Goodbye!",
            "Have a great day! Goodbye!",
            "It was nice chatting with you. Goodbye!"]

# Define a function to preprocess the user's input


def preprocess_input(input_text):
    # Tokenization refers to the process of breaking a text into smaller units, such as words or sentences.
    words = nltk.word_tokenize(input_text.lower())
    # Remove stop words from the tokenized text. Stop words are common words in a language, such as "the", "a", "an", "in", "of", etc., 
    words = [word for word in words if word not in stop_words]
    # Lemmatization is the process of reducing words to their base or dictionary form, known as the lemma. For example, the lemmas of the words "running", "ran", and "runs" are all "run".
    words = [lemmatizer.lemmatize(word) for word in words]
    # Rejoin the words into a string
    preprocessed_text = ' '.join(words)
    return preprocessed_text

# Define a function to generate a response to the user's input


def generate_response(user_input):
    # Preprocess the user's input
    preprocessed_input = preprocess_input(user_input)
    # Determine the appropriate response based on the preprocessed input
    if any(greeting in preprocessed_input for greeting in ["hello", "hi", "hey"]):
        response = random.choice(greetings)
    elif any(crop in preprocessed_input for crop in ["crop", "farming"]):
        response = random.choice(crop_management)
    elif any(corn_keyword in preprocessed_input for corn_keyword in ["corn", "maize"]):
        response = random.choice(corn_management)
    elif any(soil_keyword in preprocessed_input for soil_keyword in ["soil", "land"]):
        response = random.choice(soil_management)
    elif any(fertilizer_keyword in preprocessed_input for fertilizer_keyword in ["fertilizer", "nutrient"]):
        response = random.choice(fertilizer_management)
    elif any(pest_keyword in preprocessed_input for pest_keyword in ["pest", "insect", "disease"]):
        response = random.choice(pest_management)
    elif any(goodbye in preprocessed_input for goodbye in ["bye", "goodbye", "see you"]):
        response = random.choice(goodbyes)
    else:
        response = "I'm sorry, I'm not sure how to help with that. Could you please provide more information?"
    return response

def run_chatbot():
    print("Welcome to the Agriculture Chatbot!")
    print("Type 'exit' at any time to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input)
        print("Chatbot:", response)
    print("Thank you for chatting with me. Goodbye!")

run_chatbot()
