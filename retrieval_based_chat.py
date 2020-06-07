#!/usr/bin/python3

# based off codecademy lessons

import re
import random
from collections import Counter
from book_file import responses
from dictionary import dictionary
from retrieval_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load('en_core_web_md')

negative_response = ("no", "nah", "nope", "none")
exit_commands = ("quit", "goodbye", "good bye", "exit", "no", "nah", "nope", "none")
categories = ["science", "philosophy", "life", "reality", "history", "reason", "technology", "intelligence"]

class SandBot:
  def __init__(self):
    self.greetings = ("hello", "hello!", "hi", "hi!", "hola", "hola!", "Hello", "Hello!", "Hi", "Hi!", "Hola", "Hola!")

  def greeting_intent(self, name):
    responses = ("hello", "hello!", "hi", "hi!", "hola", "hola!")
    reply = random.choice(responses)
    return (reply + " " + name)
  
  def make_exit(self, message):
    for obj in exit_commands:
      if obj in message:
        if obj in negative_response:
          return("ok")
        else:
          return("good bye")
        #return True
      else:
        pass


  def chat(self, name, message):
    # don't use since constantly monitoring
    #user_message = input("what is your question? ")
    #for greeting in self.greetings:
    #  if greeting in message:
    #    return(self.greeting_intent(name))
    response = ''
    response = self.make_exit(message)
    if (response == 'ok') or (response == 'good bye'):
      return(response + ' ' + name)
    else:
      response = self.respond(message)
      return(response)


  def find_intent_match(self, responses, user_message, subject):
    bow_user_message = Counter(preprocess(user_message))
    # if no bow then use entity as the subject for bow
    if len(bow_user_message) < 1:
      bow_user_message = Counter(preprocess(subject))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(response, bow_user_message) for response in processed_responses]
    response_index = similarity_list.index(max(similarity_list))
    return(responses[response_index])


  def find_entities(self, user_message):
    tagged_user_message = pos_tag(preprocess(user_message))
    if len(tagged_user_message) < 1:
      return(random.choice(dictionary))
    message_nouns = extract_nouns(tagged_user_message)
    tokens = word2vec(" ".join(message_nouns))
    cat_list = list()
    final_cat_list = list()
    for cat in categories:
      temp_cat = word2vec(cat)
      cat_list.append(compute_similarity(tokens, temp_cat))
    for first_level in cat_list:
      for sec_level in first_level:
        final_cat_list.append(sec_level)
    final_cat_list.sort(key=lambda x: x[2])
    if len(final_cat_list) < 1:
      pre_category = tokens[0]
    else:
      pre_category = final_cat_list[-1][0]
    category = word2vec(pre_category)
    word2vec_result = compute_similarity(tokens, category)
    word2vec_result.sort(key=lambda x: x[2])
    if len(word2vec_result) < 1:
      return category
    else:
      return(word2vec_result[-1][0])


  def respond(self, user_message):
   entity = self.find_entities(user_message)
   print(entity)
   best_response = self.find_intent_match(responses, user_message, entity)
   # don't use since constantly monitoring and output through discord; kept here for testing
   #print(best_response)
   return(best_response)

#initialize ChatBot instance below:

#call .chat() method below for testing:
#sandbot = SandBot()
#sandbot.chat("fake_user", "how are we here ")

# interaction with discord program sandbot.py
def sendToRetrieval(name, message):
  sandy = SandBot()
  message = message.lower()
  message = message.replace("sandbot", "").replace("Sandbot", "")
  reply = sandy.chat(name, message)
  return reply
