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

def read_process_data():
    with open('third_party/jane-eyre.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content


# You do not need to call this function unless you are doing level 3
def get_stop_words():
    with open('stop-words.txt') as f:
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content.split(' ')

def get_highest_words(counts_dictionary, count):
    highest = sorted(counts_dictionary.items(), key=lambda x:x[1])[::-1][:count]
    for word in highest:
        print("%s: %s" % (word[0], word[1]))

if __name__ == '__main__':
    content = read_process_data()
    word_count = {}
    stops = get_stop_words()
    words = content.split(" ")
    for word in words:
        if word == "" or word in stops:
            continue
        if word.endswith(".") or word.endswith(",") or word.endswith('"'):
            word = word[:-1]
        if word.startswith('"'):
            word = word[1:]
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    get_highest_words(word_count, 50)
#for thing in word_count:
#    print thing+": "+str(word_count[thing])
# Write your solution below!
