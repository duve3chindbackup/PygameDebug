import urllib.request

def retrieve_font():
    # google fonts git RAW url for robotomono.ttf
    font_url = "https://github.com/google/fonts/raw/refs/heads/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    
    urllib.request.urlretrieve(font_url, "./PYGAME_DEBUG_FONT.ttf")
    
    return "./PYGAME_DEBUG_FONT.ttf"
    