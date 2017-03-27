import webapp2

INDEX_HTML = open('index.html').read()

LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];

def rot13(sourceString):
    resultString = "";
    for char in sourceString:
        if char.isupper():
            resultString += encrypt(char, UPPER_LETTERS);
        elif char.islower():
            resultString += encrypt(char, LOWER_LETTERS);
        else:
            resultString += char;
    return resultString
    #print("The rot13 string is:%s" % (resultString));

def encrypt(char, letterList):
    resultchar = '';
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    resultchar += letterList[newIndex % len(letterList)]
    return resultchar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(INDEX_HTML)
        #self.response.write('Hello world!')
        #self.render("index.html");

#class Rot13Handler(webapp2.RequestHandler):
    def post(self):
        text = self.request.get("text")
        #self.response.write(text)
        translated = rot13(text)
        #INDEX_HTML.replace("myText", translated)
        self.response.write("""<html>
          <head>
             <meta charset="utf-8">
        	<title>Rot13 Encoder/Decoder</title>
          </head>
          <body>
             <h2> Enter Some text to Rot13:</h2>
             <form action="/" method ="post">
                <textarea name ="text" style = "height:100px; width:400px;">""")
        self.response.write (translated)
        self.response.write("""</textarea>
                <br><input type ="submit">
               </form>
           </body>
        </html>""")
        #self.display_html("index.html",translated = translated)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
