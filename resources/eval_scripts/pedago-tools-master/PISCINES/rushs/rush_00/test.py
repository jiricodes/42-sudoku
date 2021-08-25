#!/usr/bin/env python3
import os
import sys
import subprocess
from termcolor import colored

PROJECT_PATH="/Users/ablette/Projects/42_PROJECTS/piscine_c/rush_00"

class Rush(object):
  def do_tests(self):
    errors = 0
    print(colored(f"Rush {self.number} :\n", "yellow"))
    os.system(f"gcc {PROJECT_PATH}/{self.rush_dir}/ft_putchar.c {PROJECT_PATH}/{self.rush_dir}/rush{self.number}.c main.c -o rush")
    for test in self.tests:
      user_output = subprocess.run(['./rush', test['x'], test['y']], stdout=subprocess.PIPE).stdout.decode('utf-8')
      if user_output != test['output']:
        print(colored(f"KO for rush({test['x']}, {test['y']})", "red"))
        print("<<< User result")
        print(user_output)
        print(">>> Expected result")
        print(test['output'])
        errors += 1
    if not errors:
      print(colored("OK", 'green'))
    os.system("rm rush")
    return errors

class Rush00(Rush):
  def __init__(self):
    self.tests = [
      {'x': '0', 'y': '3', 'output': ''},
      {'x': '1', 'y': '4', 'output': "o\n|\n|\no\n"},
      {'x': '2', 'y': '1', 'output': "oo\n"},
      {'x': '1', 'y': '1', 'output': "o\n"},
      {'x': '2', 'y': '2', 'output': "oo\noo\n"},
      {'x': '25', 'y': '17', 'output': "o-----------------------o\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\n|                       |\no-----------------------o\n"},
    ]
    self.rush_dir = "ex00"
    self.number = "00"

class Rush01(Rush):
  def __init__(self):
    self.tests = [
      {'x': '0', 'y': '3', 'output': ''},
      {'x': '1', 'y': '4', 'output': "/\n*\n*\n\\\n"},
      {'x': '2', 'y': '1', 'output': "/\\\n"},
      {'x': '1', 'y': '1', 'output': "/\n"},
      {'x': '2', 'y': '2', 'output': "/\\\n\\/\n"},
      {'x': '25', 'y': '17', 'output': "/***********************\\\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n*                       *\n\\***********************/\n"},
    ]
    self.rush_dir = "ex00"
    self.number = "01"

class Rush02(Rush):
  def __init__(self):
    self.tests = [
      {'x': '0', 'y': '3', 'output': ''},
      {'x': '1', 'y': '4', 'output': "A\nB\nB\nC\n"},
      {'x': '2', 'y': '1', 'output': "AA\n"},
      {'x': '1', 'y': '1', 'output': "A\n"},
      {'x': '2', 'y': '2', 'output': "AA\nCC\n"},
      {'x': '25', 'y': '17', 'output': "ABBBBBBBBBBBBBBBBBBBBBBBA\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nCBBBBBBBBBBBBBBBBBBBBBBBC\n"}
    ]
    self.rush_dir = "ex00"
    self.number = "02"

class Rush03(Rush):
  def __init__(self):
    self.tests = [
      {'x': '0', 'y': '3', 'output': ''},
      {'x': '1', 'y': '4', 'output': "A\nB\nB\nA\n"},
      {'x': '2', 'y': '1', 'output': "AC\n"},
      {'x': '1', 'y': '1', 'output': "A\n"},
      {'x': '2', 'y': '2', 'output': "AC\nAC\n"},
      {'x': '25', 'y': '17', 'output': "ABBBBBBBBBBBBBBBBBBBBBBBC\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nABBBBBBBBBBBBBBBBBBBBBBBC\n"}
    ]
    self.rush_dir = "ex00"
    self.number = "03"

class Rush04(Rush):
  def __init__(self):
    self.tests = [
      {'x': '0', 'y': '3', 'output': ''},
      {'x': '1', 'y': '4', 'output': "A\nB\nB\nC\n"},
      {'x': '2', 'y': '1', 'output': "AC\n"},
      {'x': '1', 'y': '1', 'output': "A\n"},
      {'x': '2', 'y': '2', 'output': "AC\nCA\n"},
      {'x': '25', 'y': '17', 'output': "ABBBBBBBBBBBBBBBBBBBBBBBC\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nB                       B\nCBBBBBBBBBBBBBBBBBBBBBBBA\n"}
    ]
    self.rush_dir = "ex00"
    self.number = "04"


if __name__ == '__main__':
  PROJECT_PATH = input("Project path : " ).strip()
  # PROJECT_PATH = f"{project_path}/ex00"
  if len(sys.argv) == 1:
    print("You must specify the rush or `all`.")
  else:
    test_ret = ""
    if sys.argv[1] == '0':
      rush_00_errors = Rush00().do_tests()
    if sys.argv[1] == '1':
      rush_01_errors = Rush01().do_tests()
    if sys.argv[1] == '2':
      rush_02_errors = Rush02().do_tests()
    if sys.argv[1] == '3':
      rush_03_errors = Rush03().do_tests()
    if sys.argv[1] == '4':
      rush_04_errors = Rush04().do_tests()
    if sys.argv[1] == 'all':
      rush_00_errors = Rush00().do_tests()
      rush_01_errors = Rush01().do_tests()
      rush_02_errors = Rush02().do_tests()
      rush_03_errors = Rush03().do_tests()
      rush_04_errors = Rush04().do_tests()
  # TODO : Faire test no printf, no forbidden functions
  # grep -Hn "printf" *.[ch]
  # grep -Hn "stdio" *.[ch]
  # grep -Hn "?" *.[ch]
  # grep -Hn "for" *.[ch]
  # TODO : Faire anti cheat ? (vérifier header, vérifier github ?)
