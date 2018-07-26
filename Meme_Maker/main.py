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

#Get jinja ready to load html files
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader= template_loader)

class MemePageResult(webapp2.RequestHandler):
    """ A meme generator page, generates a meme with the info given
        and shows the result
    """
    def post(self):
        # Get info from the user/input boxes
        text1=self.request.get("text1")
        text2=self.request.get("text2")
        type=self.request.get("meme-type")
        self.response.headers['Content-Type'] = 'text/html'

        # Our api url
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            result = urlfetch.fetch(url)

            #Check that site could be reached
            if result.status_code == 200:

                #Change result.content from string to dictuionary and get a meme dictionary
                memeDictionary = json.loads(result.content)
                memes = memeDictionary["data"]["memes"]

                caption_url = 'https://api.imgflip.com/caption_image'
                if (type == "random"):
                    type = random.randint(1,100)

                #A dictionary to send to imgflip with all the data
                captionDictionary = {
                    "template_id":memes[int(type)]["id"],
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
                template=template_env.get_template('/memepage.html')
                #Add image to webpage
                self.response.write(template.render({"meemUrl":meemUrl}))
            #Set status code if not successful
            else:
                self.response.status_code = result.status_code

        #If connection doesn't work, log an error
        except urlfetch.Error:
            logging.exception("Caught error")

class MainPage(webapp2.RequestHandler):
    """Shows the meme page and sends info on
        available memes to html
    """
    def get(self):
        template = template_env.get_template('/home.html')
        memes={}
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            result = urlfetch.fetch(url)

            #Check that site could be reached
            if result.status_code == 200:

                #Change result.content from string to dictuionary and get a meme dictionary
                memeDictionary = json.loads(result.content)
                memes = memeDictionary["data"]["memes"]
                meme_names={}
                count=0
                for meme in memes:
                    meme_names[count]=meme["name"]
                    count+=1
                self.response.write(template.render({'meme_names': meme_names}))
        except urlfetch.Error:
            logging.exception("Error")

class MainPageTest(webapp2.RequestHandler):
    """Shows the meme page and sends info on
        available memes to html
    """
    def getDictionary(self):
        # Our api url
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            result = urlfetch.fetch(url)

            #Check that site could be reached
            if result.status_code == 200:

                #Change result.content from string to dictuionary and get a meme dictionary
                memeDictionary = json.loads(result.content)
                memes = memeDictionary["data"]["memes"]
                return memes
        except urlfetch.Error:
            logging.exception("Caught error")

    def post(self):
        template=template_env.get_template('/memepage.html')

        # Get info from the user/input boxes
        text1=self.request.get("text1")
        text2=self.request.get("text2")
        type=self.request.get("meme-type")
        self.response.headers['Content-Type'] = 'text/html'

        # Our api url
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            memes = self.getDictionary()

            caption_url = 'https://api.imgflip.com/caption_image'
            if (type == "random"):
                type = random.randint(1,100)

            #A dictionary to send to imgflip with all the data
            captionDictionary = {
                "template_id":memes[int(type)]["id"],
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
            self.response.write(template.render({"meemUrl":meemUrl}))

        #If connection doesn't work, log an error
        except urlfetch.Error:
            logging.exception("Caught error")
    def get(self):
        template = template_env.get_template('/home.html')
        url = 'https://api.imgflip.com/get_memes'

        #Try to access the internet to make a meme
        try:
            memes = self.getDictionary()
            meme_names={}
            count=0
            for meme in memes:
                meme_names[count]=meme["name"]
                count+=1
            self.response.write(template.render({'meme_names': meme_names}))
        except urlfetch.Error:
            logging.exception("Error")

class FourOhFour(webapp2.RequestHandler):
    """ Manual 404 page not found request handler
    """
    def get(self):
        self.response.write('<html><h1>404 Error: Page Not Found!</h1><body>We could not find the page you were looking for</body></html>')

app = webapp2.WSGIApplication([
    ('/home', MainPageTest),#MainPage),
    ('/meme_result', MainPageTest),#MemePageResult),
    ('/.*', FourOhFour)
], debug=True)
