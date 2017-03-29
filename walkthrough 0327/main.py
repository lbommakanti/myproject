#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class Index(webapp2.RequestHandler):
    "Handles requests coming intp '/' (the for )"
    www.flicklist.com/

def getCurrentListOfMovies():
    return ['star Wars','Arrival','Princess Wars',]

def get(self):
    edit_header ="<h3>Edit My Watchlist</h3>"
    moviesOptions =''
    for movie in getCurrentListOfMovies():
        moviesOptions += '<option value="{0}">{0}</option>'.format(movie)
# a form for adding new moviesOptions
add_form ="""
<form action ="/add" method ="post">
    <label>
       I want to add
       <input type ="text" name ="new-movie"/>
       to my Watchlist
"""

def post(self):
    crossed_off_movie =self.request.get("crossed_off_movie")
    if crossed_off_movie not in getCurrentListOfMovies():
        seld.redirect("/?error ={0}is not in your list of movies".format(crossed_off_movie))

       #build response content
       crossed_off_movie_element ="<strike>"+crossed_off_movie +"</strike>"
       confirmation = crossed_off_movie_element




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
