#! /usr/bin/env python3

import os
import sys
import subprocess
import difflib

from errors.check import test_errors_1, test_errors_2, test_errors_3, test_errors_4
from check_valid import check_valid_easy, check_valid_medium, check_valid_hard

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
  # project_path = input("Project path: ").strip()
  project_path = "correction"
  # project_path = "sudoku"

  #-- Check norminette
  # if os.system(f"norminette -R CheckForbiddenSourceHeader {project_path}/*.[ch]") != 0:
  #   return

  #-- Compile project
  if os.system(f"gcc  {project_path}/ex00/*.c -o rush") != 0:
    return
  # if os.system(f"gcc -Wall -Werror -Wextra {project_path}/ex00/*.c -o rush") != 0:
  #   return

  test_error_cases_ok = 0
  errors = []
  ko = 0

  #-- Test errors 1
  errors += test_errors_1() #-- Test wrong number of arguments and bad formatting
  if errors:
    ko = 1

  ret = check_valid_easy()
  points_lvl1 = 0 if ret else 1
  errors += ret

  ret = check_valid_medium()
  if ret and len(ret) >= 2:
    points_lvl1 += 0
  elif ret and len(ret) < 2:
    points_lvl1 += 1
  else:
    points_lvl1 += 2
  errors += ret

  ret = check_valid_hard()
  if ret and len(ret) >= 2:
    points_lvl1 += 0
  elif ret and len(ret) < 2:
    points_lvl1 += 1
  else:
    points_lvl1 += 2
  errors += ret

  points_lvl4 = 0

  ret =  test_errors_2() #-- Test only one solution
  points_lvl4 = 0 if ret else 2
  errors += ret

  ret = test_errors_3() #-- Test already filled_grid OK
  if points_lvl4 != 0:
    if ret:
      ko_lvl4 = 1
      if ret[0]['user_output'] == 'Error':
        points_lvl4 = 0
      else:
        points_lvl4 = 2
    else:
      ko_lvl4 = 0
      points_lvl4 += 2
  errors += ret

  ret = test_errors_4() #== Test already filled_grid KO
  if points_lvl4 != 0:
    points_lvl4 += 0 if ret or ko_lvl4 else 1
  errors += ret

  if ko:
    print(f"Preliminary tests : {bcolors.BOLD}{bcolors.FAIL}KO{bcolors.ENDC}")
  else:
    print(f"Preliminary tests : {bcolors.BOLD}{bcolors.OKGREEN}OK{bcolors.ENDC}")
  if points_lvl1 < 1:
    print(f"First part : {bcolors.BOLD}{bcolors.FAIL}KO{bcolors.ENDC}")
  else:
    print(f"First part : {bcolors.BOLD}{bcolors.OKGREEN}{points_lvl1} point(s){bcolors.ENDC} / 5")
  if points_lvl4 < 1:
    print(f"Second part: {bcolors.BOLD}{bcolors.FAIL}KO{bcolors.ENDC}")
  else:
    print(f"Second part : {bcolors.BOLD}{bcolors.OKGREEN}{points_lvl4} point(s){bcolors.ENDC} / 5")


  if errors:
    for e in errors:
      print(f"Test {e['test_id']} - {e['test_name']} : {bcolors.FAIL}KO{bcolors.ENDC}")
      print(f"{bcolors.BOLD}Test :{bcolors.ENDC} {e['test']}")
      # for line in difflib.context_diff([e['expected_result']], [e['user_output']]):
      #   print(line)
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?"
#       + bcolors.ENDC
#       print(e)


# GERE DIFF DU KO (Faire un truc bien visible et bien comprehensible)
# CHECK FONCTIONS INTERDITES (printf, for, define, ...)
# CHECK GITHUB API CODE


if __name__ == '__main__':
  main()
