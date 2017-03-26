import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.display.html("index.html")

	def post(self):
        text=self.request.get("text")
        translated =self.translate_to_rot13(text)
		self.display_html("index.html",translated = translated)

    def translate_to_rot13(self,untranslated):
        upper_cases="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJLMN"
        lower_cases= upper_cases.lower()
        new_string=""
        for char in untranslated:
            if char in upper_cases:
                location =upper_cases.index(char)
                location+=13
                new_char=upper_cases[location]
                new_string+=new_char
        elif char in lower_cases:
                location =lower_cases.index(char)
                location+=13
                new_char=lower_cases[location]
                new_string+=new_char
        else:
                new_string+=char
 return  new_string


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
