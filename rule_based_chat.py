#!/usr/bin/python3

# based off codecademy lessons

import re
import random

class SandBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "good bye")
  
  def __init__(self):
    self.botbabble = {'describe_yourself_intent': r'.*who.*made.*',
                        'answer_why_intent': r'.*why.*are.*you.*',
                        'cubed_intent': r'.*cube.*(\d+)',
                        'greeting_intent': r'h.*\ssandbot.*',
                        'unsure_response_intent': r''
                            }

  # not used since bot is constantly monitoring
  '''
  def greet(self, name):
    self.name = name
    #self.name = input("what is your name? ")
    will_help = input("Hi " + self.name + ", i'm SandBot. Im an idiot bot that hasn't progressed far. will you help me learn about your planet? ")
    if will_help in self.negative_responses:
      print("ok, have a nice earth day!")
      return
    self.chat()
  '''
  # moved into match_reply function
  '''
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        return ("goodbye!")
    return False
  '''

  # opening function called from outside function (sendNameandMessage)
  def chat(self, name, message):
    reply = self.match_reply(name, message)
    return reply

  def match_reply(self, name, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        return("goodbye!")
    for intent, regex_pattern in self.botbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'greeting_intent':
        return self.greeting_intent(name)
      if found_match and intent == 'describe_yourself_intent':
        return self.describe_yourself_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
    return self.no_match_intent()


  def describe_yourself_intent(self):
    responses = ("a really novice programmer ", "somebody with a very low IQ", "just an all around nice guy")
    return random.choice(responses)

  def answer_why_intent(self):
    responses = ("i come in peace", "i am here to say things that probably don't make much sense", "i like coffee")
    return random.choice(responses)

  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number * number * number
    return (f"the cube of {number} is {cubed_number}. i do numbers... ")

  def greeting_intent(self, name):
    responses = ("hello", "hello!", "hi", "hi!", "hola", "hola!")
    reply = random.choice(responses)
    return (reply + " " + name)

  def no_match_intent(self):
    responses = ("please don't tell me anymore",
                "tell me just a little more!",
                "why do you think that?",
                "i see why that is..",
                "interesting... can you shutup?",
                "i see. but not really...i don't have eyes",
                "hmm.... nope",
                "you are strange",
                "why are we here? ",
                "are there many humans like you? ...maybe don't answer ;)",
                "What do you like coffee? ",
                "is there intelligent life in this server? ",
                "is there anything outside of discord? ")
    return random.choice(responses)

# interaction with discord program sandbot.py
def sendToRule(name, message):
  sandy = SandBot()
  message = message.lower()
  reply = sandy.chat(name, message)
  return reply

