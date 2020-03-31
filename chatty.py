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
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.botbabble = {'describe_planet_intent': r'.*\s*your.*planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.*(\d+)',
                        'unsure_response_intent': r''
                            }

  # not used since bot is constantly monitoring
  def greet(self, name):
    self.name = name
    #self.name = input("what is your name? ")
    will_help = input("Hi " + self.name + ", i'm SandBot. Im not from this planet. will you help me learn about your planet? ")
    if will_help in self.negative_responses:
      print("ok, have a nice earth day!")
      return
    self.chat()

  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("ok, have a nice earth day!")
        return True
    return False

  # opening function called from outside function (sendNameandMessage)
  def chat(self, name, message):
    reply = self.match_reply(message)
    reply = reply + " " + (random.choice(self.random_questions))
    return reply

  def match_reply(self, reply):
    for intent, regex_pattern in self.botbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
      else:
        return self.no_match_intent()


  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(responses)

  def answer_why_intent(self):
    responses = ("i come in peace", "i am here to collect data on your planet and its inhabitants", "i heard the coffee is good")
    return random.choice(responses)

  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number^3
    return (f"the cube of {number} is {cubed_number}. isn't that cool? ")

  def no_match_intent(self):
    responses = ("please tell me more", "tell me more!", "why do you say that?", "i see. can you elaborate?", "interesting... can you tell me more?", "i see. how do you think?", "why?", "how do you think i feel when you say that?")
    return random.choice(responses)

# interaction with discord program sandbot.py
def sendNameandMessage(name, message):
  sandy = SandBot()
  message = message.lower()
  reply = sandy.chat(name, message)

  return reply

