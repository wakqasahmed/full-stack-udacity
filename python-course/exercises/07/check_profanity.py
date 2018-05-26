import urllib.request
import urllib.parse

def read_text(file_path):
    file = open(file_path)
    content = file.read()
    file.close()
    check_profanity(content)
    
def check_profanity(content):
    params = urllib.parse.urlencode({'q': content})
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?%s" % params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    print(result)
    if result == 'true':
        print("Profanity Alert!")
    else:
        print("No curse word found.")

read_text("/Users/waqasahmed/Documents/Udacity/full-stack-nanodegree/python-course/exercises/07/motivational_quotes.txt")
