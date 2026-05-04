import pyttsx3

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Sana")

    engine = pyttsx3.init()

    while True:
        text = input("Enter what you want me to speak (type 'exit' to stop): ")

        if text.lower() == "exit":
            print("bye user")
            break

        engine.say(text)
        engine.runAndWait()