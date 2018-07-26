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
import jinja2
import random
import snap


template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader= template_loader)

def get_fortune():
    fortune_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/fortune_welcome.html")
        self.response.write(start_template.render())

    def post(self):
        random_fortune = get_fortune()
        astro_sign = self.request.get('user_astrological_sign')
        my_dict={'the_fortune':random_fortune, 'the_astro_sign':astro_sign}
        end_template=jinja_current_directory.get_template("templates/fortune_results.html")
        #astro_sign = request.form.get('user_astrological_sign')
        self.response.write(end_template.render(my_dict))
class Main(webapp2.RequestHandler):
    def get(self):
        template=template_env.get_template('/data.html')
        #Add image to webpage
        self.response.write(template.render())


class TestDataHandler(webapp2.RequestHandler):
    def get(self):
        template=template_env.get_template('/data.html')
        query = snap.Users.query().order().fetch()[0]
        dict1 = {"bitmoji":query.bitmoji,"location":query.location, "phone":query.phone}
        dict2 = {"email":query.email,"first name":query.first_name,"last name":query.last_name, "password":query.password, "username":query.username}
        self.response.write(template.render({"deletable": dict1, "changeable":dict2}))#["Users"])#template.render({"query":query}))
    def post(self):
        first = self.request.get('First')
        last = self.request.get('Last')
        username = self.request.get('User')
        password = self.request.get('Pass')
        email = self.request.get('Email')
        bitmoji = self.request.get('Bitmoji')
        location = self.request.get('Location')
        phone = self.request.get('Phone')
        pickle = self.request.get('Pickle')
        if bitmoji=="on":
            bitmoji=True
        else:
            bitmoji=False
        new_user=snap.Users(bitmoji=bitmoji,phone=phone,location=location,first_name=first, last_name=last, username=username, email=email, password = password)
        new_user.put()
        self.get()

class DataDeleteHandler(webapp2.RequestHandler):
    def post(self):
        first = self.request.get('first name')
        last = self.request.get('last name')
        username = self.request.get('username')
        password = self.request.get('password')
        email = self.request.get('email')
        bitmoji = self.request.get('bitmoji')
        location = self.request.get('location')
        phone = self.request.get('phone')
        all = self.request.get('all')
        key1 = self.request.get('key')
        data_to_delete = snap.Users.query().filter(snap.Users.email=="a").fetch()[0]
        setattr(data_to_delete,key1, "")
        data_to_delete.put()
        self.response.write("Your "+key1+ " data has been deleted. Please go back to /test_data now!")
        #data_to_delete.put()

class DeleteConfirmation(webapp2.RequestHandler):
    def post(self):
        first = self.request.get('first name')
        last = self.request.get('last name')
        username = self.request.get('username')
        password = self.request.get('password')
        email = self.request.get('email')
        bitmoji = self.request.get('bitmoji')
        location = self.request.get('location')
        phone = self.request.get('phone')
        all = self.request.get('all')
        query = snap.Users.query().order().fetch()[0]
        # if (first == "on"):
        #     query.first.delete()
        # if last == "on":
        #     query.last.delete()
        # if username == "on":
        #     query.last.delete()
        # if password == "on":
        #     query.last.delete()
        if all == "on":
            query.delete()
        if email == "on":
            query.email = ""
        if bitmoji == "on":
            query.bitmoji = False
        if location == "on":
            query.location = ""
        if phone == "on":
            query.phone = ""


app = webapp2.WSGIApplication([
    ('/', FortuneHandler),
    ('/test_data', TestDataHandler),
    ('/main', Main),
    ('/confirm_delete', DeleteConfirmation),

], debug=True)
