#!/usr/bin/python3

import re
import random

class SandBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are we here? ",
        "Are there many humans like you? ...maybe don't answer ;)",
        "What do you like coffee? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "is there anything outside of discord? ",
        "What technology do you have on this computer? "
    )

  def __init__(self):
    self.botbabble = {'describe_yourself_intent': r'.*who.*made.*',
                        'answer_why_intent': r'.*why.*are.*you.*',
                        'cubed_intent': r'.*cube.*(\d+)',
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

  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("ok, have a nice earth day!")
        return True
    return False

  # opening function called from outside function (sendNameandMessage)
  def chat(self, name, message):
    reply = self.match_reply(message)
    #reply = reply + ", " + (random.choice(self.random_questions))
    return reply

  def match_reply(self, reply):
    for intent, regex_pattern in self.botbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'describe_yourself_intent':
        return self.describe_yourself_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
    return self.no_match_intent()


  def describe_yourself_intent(self):
    responses = ("a really novice programmer ", "somebody with a very low IQ")
    return random.choice(responses)

  def answer_why_intent(self):
    responses = ("i come in peace", "i am here to say things that probably don't make much sense", "i like coffee")
    return random.choice(responses)

  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number * number * number
    return (f"the cube of {number} is {cubed_number}. i do numbers... ")

  def no_match_intent(self):
    responses = ("please don't tell me anymore", "tell me just a little more!", "why do you think that?", "i see why that is..", "interesting... can you shutup?", "i see. but not really...i don't have eyes", "why?", "you are strange")
    return random.choice(responses)

# interaction with discord program sandbot.py
def sendNameandMessage(name, message):
  sandy = SandBot()
  message = message.lower()
  reply = sandy.chat(name, message)

  return reply

