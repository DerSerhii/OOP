def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="да"):
        return word.lower() + "..."
    
    # ... и сразу же её использовать!
    print(whisper())