#!/usr/bin/env python3

from termcolor import colored

class Rush(object):

  def __init__(self, number):
    self.subject = f"THE SUBJECT IS RUSH_0{number}"
    if number == 0:
      self.schema = "\no---o\n|   |\no---o\n"
    elif number == 1:
      self.schema = "\n/***\\\n*   *\n\\***/\n"
    elif number == 2:
      self.schema = "\nABBBA\nB   B\nCBBBC\n"
    elif number == 3:
      self.schema = "\nABBBC\nB   B\nABBBC\n"
    elif number == 4:
      self.schema = "\nABBBC\nB   B\nCBBBA\n"

  def print_rush(self):
    print(self.subject)
    print("\nThe rush should display :")
    print(colored(self.schema, 'cyan'))


if __name__ == '__main__':
  letter = input("Team leader login : ").strip().lower()[0]
  letter = ord(letter) - 96
  if letter % 5 == 1:
    r = Rush(1)
  elif letter % 5 == 2:
    r = Rush(2)
  elif letter % 5 == 3:
    r = Rush(3)
  elif letter % 5 == 4:
    r = Rush(4)
  elif letter % 5 == 0:
    r = Rush(0)
  r.print_rush()
