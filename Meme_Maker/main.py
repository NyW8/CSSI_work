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

import webapp2
from google.appengine.api import urlfetch
import json
import random
import urllib


class MainPage(webapp2.RequestHandler):
    def get(self):
        text1 = self.request.get("text1")
        text2 = self.request.get("text2")
        self.response.headers['Content-Type'] = 'text/html'
        #self.response.write('Hello, Programmers!')
        #result = requests.get('https://api.imgflip.com/get_memes')
        #self.response.write('Hello, Programmers! '+result)
        #self.
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            random1=["Sand", "Fruit Juice", "Programming", "My Oyster", "Kleenex", "Google?", "hamburgers", "and then i said"]
            random2=["is delicious", "sucks", "grows on trees", "needs to be fired", "My oyster", "Rocks", "for the win"]
            if result.status_code == 200:
                #self.response.write(result.content)
                memeDictionary = json.loads(result.content)
                memes = memeDictionary["data"]["memes"]
                url = random.choice(memes)["url"]
                caption_url = 'https://api.imgflip.com/caption_image'
                if text1=="":
                    text1=random.choice(random1)
                if text2=="":
                    text2=random.choice(random2)
                captionDictionary = {
                    "template_id":memes[random.randint(1,100)]["id"],
                    "username":"ded0fd30",
                    "password":"ded0fd30@maskedmail.net",
                    "text0":text1,
                    "text1":text2,
                }
                result= urlfetch.fetch(
                    url=caption_url,
                    payload=urllib.urlencode(captionDictionary),
                    method=urlfetch.POST,)
                meemUrl = json.loads(result.content)["data"]["url"]
                self.response.write("<html><img src="+meemUrl+"></html>")

            else:
                self.response.status_code = result.status_code

        except urlfetch.Error:
            logging.exception("Caught error")



class FourOhFour(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<html><h1>404 Error: Page Not Found!</h1><body>We could not find the page you were looking for</body></html>')
        #self.response.write('404 Error: Page Not Found')

app = webapp2.WSGIApplication([
    ('/memes.*', MainPage),
    ('/.*', FourOhFour)
], debug=True)
