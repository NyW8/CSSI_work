# Copyright 2016 Google Inc.
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

#Import statements! Will be using Google's app engine
import webapp2
from google.appengine.api import urlfetch
import json
import random
import urllib
import jinja2


templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader = templateLoader)

class MemePage(webapp2.RequestHandler):
    """ A meme generator page, generates a random meme picture with
        a random caption or specified captions through the url
    """

    def get(self):
        # text1 and text2 can be specified through the url
        text1 = self.request.get("text1")
        text2 = self.request.get("text2")
        self.response.headers['Content-Type'] = 'text/html'

        # Our api url
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            result = urlfetch.fetch(url)

            #Random top and bottom text in case one or both is not specified
            random1=["Sand", "Fruit Juice", "Programming", "My Oyster", "Kleenex", "Google?", "hamburgers", "and then i said"]
            random2=["is delicious", "sucks", "grows on trees", "needs to be fired", "My oyster", "Rocks", "for the win"]

            #Check that site could be reached
            if result.status_code == 200:

                #Change result.content from string to dictuionary and get a meme dictionary
                memeDictionary = json.loads(result.content)
                memes = memeDictionary["data"]["memes"]

                #Choose random meme and get the url of it
                url = random.choice(memes)["url"]
                caption_url = 'https://api.imgflip.com/caption_image'

                #Assign text if not already assigned
                if text1=="":
                    text1=random.choice(random1)
                if text2=="":
                    text2=random.choice(random2)

                #A dictionary to send to imgflip with all the data
                captionDictionary = {
                    "template_id":memes[random.randint(1,100)]["id"],
                    "username":"ded0fd30",
                    "password":"ded0fd30@maskedmail.net",
                    "text0":text1,
                    "text1":text2,
                }

                #Use post to return img url
                result= urlfetch.fetch(
                    url=caption_url,
                    payload=urllib.urlencode(captionDictionary),
                    method=urlfetch.POST,)
                meemUrl = json.loads(result.content)["data"]["url"]

                #Add image to webpage
                self.response.write("<html><img src="+meemUrl+"></html>")
            #Set status code if not successful
            else:
                self.response.status_code = result.status_code

        #If connection doesn't work, log an error
        except urlfetch.Error:
            logging.exception("Caught error")

class MainPage(webapp2.RequestHandler):
    """Shows the main (home) page """
    def get(self):
        template = templateEnv.get_template('/home.html')
        #home_html=open('home.html').read()
        self.response.write(template.render())

class Recipe(webapp2.RequestHandler):
    """Shows a recipe html page"""
    def get(self):
        template = templateEnv.get_template('/recipe.html')
        recipe = {"ingredients": ["cottage cheese", "pineapple"], "cuisine":"nixonian"}
        self.response.write(template.render(recipe))

class FourOhFour(webapp2.RequestHandler):
    """ Manual 404 page not found request handler
    """
    def get(self):
        self.response.write('<html><h1>404 Error: Page Not Found!</h1><body>We could not find the page you were looking for</body></html>')

app = webapp2.WSGIApplication([
    ('/memes.*', MemePage),
    ('/home', MainPage),
    ('/recipies', Recipe),
    ('/.*', FourOhFour)
], debug=True)
