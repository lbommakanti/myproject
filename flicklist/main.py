import webapp2

form ="""
<form method ="post">
    What is your birthday?
    <br>
    <label>Month
    <input type ="text" name="month">
    </label>
    <label> Day
    <input type ="text" name="day">
    </label>
    <label>Year
    <input type="text" name ="year">
    </label>
    <br>
    <br>
    <input type ="submit">
</form>
"""
month_abbvs = dict((m[:3].lower(),m) for m in months)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
    def post(self):
        user_month = vaild.month(self.request.get('month'))
        user_day = valid.day(self.request.get('day'))
        user_year = valid.year(self.request.get('year'))
        self.response.out.write("Thanks, That's totally valid day")

app = webapp2.WSGIApplication([('/', MainPage)],
                                  debug=True)
