import subprocess

# def sys_call(cmds):
#   return subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

def sys_call(cmds):
  return subprocess.run(cmds, capture_output=True, shell=True)

def check_bad_format(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  if res.returncode < 0:
    return {'test_name': 'Wrong format of arguments', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output != "Error\n".encode():
    return {'test_name': 'Wrong format of arguments', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': user_output.decode(), 'test_id': grid['test_id']}
  return None

def check_nb_arguments(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  if res.returncode < 0:
    return {'test_name': 'Wrong number of arguments', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output != "Error\n".encode():
    return {'test_name': 'Wrong number of arguments', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': user_output.decode(), 'test_id': grid['test_id']}
  return None

def check_only_one_sol(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  if res.returncode < 0:
    return {'test_name': 'Wrong number of solutions', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output != "Error\n".encode():
    return {'test_name': 'Wrong number of solutions', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': user_output.decode(), 'test_id': grid['test_id']}
  return None

def check_already_filled(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  expected_output = "9 1 4 3 7 5 2 6 8\n2 8 7 4 9 6 1 5 3\n3 6 5 8 1 2 4 7 9\n8 4 6 5 2 1 3 9 7\n5 2 9 6 3 7 8 1 4\n7 3 1 9 8 4 5 2 6\n1 5 3 7 4 9 6 8 2\n6 9 8 2 5 3 7 4 1\n4 7 2 1 6 8 9 3 5\n"
  if res.returncode < 0:
    return {'test_name': 'Correct grid already filled', 'test': formatted_grid, 'expected_result': expected_output, 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output.decode() != expected_output:
    return {'test_name': 'Correct grid already filled', 'test': formatted_grid, 'expected_result': expected_output, 'user_output': user_output.decode(), 'test_id': grid['test_id']}
  return None

def check_already_filled_bad(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  if res.returncode < 0:
    return {'test_name': 'Wrong grid already filled', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output.decode() != "Error\n":
    return {'test_name': 'Wrong grid already filled', 'test': formatted_grid, 'expected_result': "Error\n", 'user_output': user_output.decode.decode(), 'test_id': grid['test_id']}
  return None

def test_errors_1():
  '''
    Test error cases
  '''
  errors = []
  #-- Invalid number of arguments
  valid_grid = {'grid': ['"9...7...."', '"2...9..53"', '".6..124.."', '"84...1.9."', '"5.....8.."', '".31..4..."', '"..37..68."', '".9..5.741"', '"47......."'], 'test_id': 0 }
  for i in range(9):
    ret = check_nb_arguments({'grid': valid_grid['grid'][:i], 'test_id': f"0 - {i}"})
    if ret:
      errors.append(ret)
  #-- Invalid formatting of arguments
  invalid_grids = [
    {
      'grid': ['"9,,,7,,,,"', '"2,,,9,,53"', '",6,,124,,"', '"84,,,1,9,"', '"5,,,,,8,,"', '",31,,4,,,"', '",,37,,68,"', '",9,,5,741"', '"47,,,,,,,"'],
      'test_id': 1
    },
    {
      'grid': ['"9...7..."', '"2...9..53"', '".6..124.."', '"84...1.9."', '"5.....8.."', '".31..4..."', '"..37..68."', '".9..5.741"', '"47......."'],
      'test_id': 2
    },
    {
      'grid': ['"9...7...."', '"2...9..53"', '".6..124.."', '"84...1.9."', '"5.....8.."', '".31..4..."', '"..37..68."', '".9..5.741"', '"48......."'],
      'test_id': 3
    },
    {
      'grid': ['"........."', '"........."', '"........."', '"........."', '"........."', '"........."', '"........."', '"........."', '"........."'],
      'test_id': 4
    },
    {
      'grid': ['"99.31.62."', '"...6..358"', '"3678..4.1"', '"2.......6"', '"67..329.."', '"...4....."', '".5.7.18.."', '"..2563..."', '"..328976."'],
      'test_id': 5
    },
    {
      'grid': ['".9.31.62."', '"9..6..358"', '"3678..4.1"', '"2.......6"', '"67..329.."', '"...4....."', '".5.7.18.."', '"..2563..."', '"..328976."'],
      'test_id': 6
    },
    {
      'grid': ['"12345678."', '"........2"', '"........3"', '"........4"', '"........5"', '"........6"', '"........7"', '"........"', '"........9"'],
      'test_id': 7
    },
    {
      'grid': ['"9...7...."', '"2...9..53"', '".6..124.."', '"84...1.9."', '"5.....8.."', '".31..4..."', '"........."', '".9..5.741"'],
      'test_id': 8
    }
  ]
  for grid in invalid_grids:
    ret = check_bad_format(grid)
    if ret:
      errors.append(ret)
  return errors


def test_errors_2():
  errors = []
  invalid_grids = [
    {
      'grid': ['"9...7...."', '"2...9..53"', '".6..124.."', '"84...1.9."', '"5.....8.."', '".31..4..."', '"........."', '".9..5.741"', '"47......."'],
      'test_id': 20
    }
  ]
  for grid in invalid_grids:
    ret = check_only_one_sol(grid)
    if ret:
      errors.append(ret)
  return errors

def test_errors_3():
  errors = []
  invalid_grids = [
    {
      'grid': ['"914375268"', '"287496153"', '"365812479"', '"846521397"', '"529637814"', '"731984526"', '"153749682"', '"698253741"', '"472168935"'],
      'test_id': 21
    }
  ]
  for grid in invalid_grids:
    ret = check_already_filled(grid)
    if ret:
      errors.append(ret)
  return errors

def test_errors_4():
  errors = []
  invalid_grids = [
    {
      'grid': ['"914375268"', '"287496153"', '"365812479"', '"846521397"', '"529637814"', '"731984526"', '"153749682"', '"698253742"', '"472168935"'],
      'test_id': 22
    }
  ]
  for grid in invalid_grids:
    ret = check_already_filled_bad(grid)
    if ret:
      errors.append(ret)
  return errors
