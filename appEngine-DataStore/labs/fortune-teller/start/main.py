#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
import os
import random
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader = template_loader)

def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['fortune1', 'fortune2', 'fortune3', 'fortune4' ,'fortune5']
    #use the random library to return a random element from the array
    random_fortune = random.choice(fortune_list)
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(template_env.get_template("./fortune-start.html").render())
        user_astro_sign = self.response.get('user_astrological_sign')
        user_age = self.response.get('user_age')
        user_name=self.response.get('user_name')


class FortuneHandler(webapp2.RequestHandler):
    """Tells your fortune"""
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        results_template = template_env.get_template("./fortune.html")
        dictionary = {"fortune":get_fortune()}
        self.response.write(results_template.render(dictionary))
    #add a post method
    #def post(self):

class GoodbyeHandler(webapp2.RequestHandler):
    """ Says goodbye to the user when they visit this page"""
    def get(self):
        self.response.write('My response is goodbye')

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/home', HomeHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/farewell', GoodbyeHandler),
], debug=True)
