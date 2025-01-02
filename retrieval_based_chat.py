#!./venv/bin/python3

# based off codecademy lessons

import os
import re
import random
from collections import Counter
from book_file import responses
from dictionary import dictionary
from retrieval_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity, StanfordPOSTagger
import spacy
word2vec = spacy.load('en_core_web_lg')
pwd = os.getcwd()
#stanfordModel = pwd + '/stanford-tagger-4.0.0/models/' + 'english-bidirectional-distsim.tagger'
stanfordModel = pwd + '/stanford-postagger-full-2020-11-17/models/' + 'english-bidirectional-distsim.tagger'
#stanfordJar = pwd + '/stanford-tagger-4.0.0/' + 'stanford-postagger.jar'
stanfordJar = pwd + '/stanford-postagger-full-2020-11-17/' + 'stanford-postagger.jar'
stanPOS = StanfordPOSTagger(stanfordModel, stanfordJar)

negative_response = ("nah", "nope", "none")
exit_commands = ("quit", "goodbye", "good bye", "exit", "nah", "nope", "none")
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
    #  print(greeting)
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
    print("bow_user_message")
    print(bow_user_message)
    # if no bow then use entity as the subject for bow
    if len(bow_user_message) < 1:
      bow_user_message = Counter(preprocess(subject))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(response, bow_user_message) for response in processed_responses]
    response_index = similarity_list.index(max(similarity_list))
    return(responses[response_index])


  def find_entities(self, user_message):
    print(user_message)
    print("preprocessed message")
    print(preprocess(user_message))
    tagged_user_message = pos_tag(preprocess(user_message))
    #tagged_user_message = stanPOS.tag(preprocess(user_message))
    print("tagged_user_message")
    print(tagged_user_message)
    if len(tagged_user_message) < 1:
      return(random.choice(dictionary))
    message_nouns = extract_nouns(tagged_user_message)
    if len(message_nouns) < 1:
      return("no_noun_found")
    tokens = word2vec(" ".join(message_nouns))
    print("tokens")
    print(tokens)
    cat_list = list()
    final_cat_list = list()
    for cat in categories:
      temp_cat = word2vec(cat)
      cat_list.append(compute_similarity(tokens, temp_cat))
    for first_level in cat_list:
      for sec_level in first_level:
        final_cat_list.append(sec_level)
    final_cat_list.sort(key=lambda x: x[2])
    print("final_cat_list")
    print(final_cat_list)
    if len(final_cat_list) < 1:
      pre_category = tokens[0]
    else:
      pre_category = final_cat_list[-1][0]
    category = word2vec(pre_category)
    word2vec_result = compute_similarity(tokens, category)
    word2vec_result.sort(key=lambda x: x[2])
    print("word2vec_result")
    print(word2vec_result)
    if len(word2vec_result) < 1:
      return category
    else:
      #return(word2vec_result[-1][0])
      return(tokens)


  def respond(self, user_message):
   entity = self.find_entities(user_message)
   print("entity - subject to intent")
   print(entity)
   if (entity == "no_noun_found"):
     return("that may have been an interesting statement but my POS tagger found no nouns to work with...gfy")
   best_response = self.find_intent_match(responses, user_message, entity)
   # don't use since constantly monitoring and output through discord; kept here for testing
   #print(best_response)
   return(best_response)

#initialize ChatBot instance below:

#call .chat() method below for testing:
#sandbot = SandBot()
#sandbot.chat("fake_user", "if the universe is so big are we alone ")

# interaction with discord program sandbot.py
def sendToRetrieval(name, message):
  sandy = SandBot()
  message = message.lower()
  message = message.replace("sandbot", "").replace("Sandbot", "")
  reply = sandy.chat(name, message)
  if len(reply) > 2000:
    reply = "sorry but i got a little long winded with that response and discord rejected it for being over 2000 chars... to have better luck please rephrase your question.. thanks.."
  return reply
