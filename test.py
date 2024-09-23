import pywhatkit as kit

prompt = "play shape of you"
search_query = prompt.lower().replace("play ", "")
print(f"SYSTEM: Playing '{search_query}' on YouTube...")
kit.playonyt(search_query)
print(f"Playing '{search_query}' on YouTube.")