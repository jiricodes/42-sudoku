import subprocess
import sys

def sys_call(cmds):
  return subprocess.run(cmds, capture_output=True, shell=True)

def check_easy(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  expected_output = grid['sol']
  if res.returncode < 0:
    return {'test_name': 'Check valid grid easy', 'test': grid, 'expected_result': expected_output, 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output.decode() != grid['sol']:
    return {'test_name': 'Check valid grid easy', 'test': formatted_grid, 'expected_result': grid['sol'], 'user_output': user_output.decode(), 'test_id': grid['test_id']}
  return None

def check_medium(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  expected_output = grid['sol']
  if res.returncode < 0:
    return {'test_name': 'Check valid grid medium', 'test': grid, 'expected_result': expected_output, 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output.decode() != grid['sol']:
    return {'test_name': 'Check valid grid medium', 'test': formatted_grid, 'expected_result': grid['sol'], 'user_output': user_output, 'test_id': grid['test_id']}
  return None

def check_hard(grid):
  formatted_grid = " ".join(grid['grid'])
  res = sys_call([f'./rush {formatted_grid}'])
  if res.stdout and not res.stderr:
    user_output = res.stdout
  elif res.stderr and not res.stdout:
    user_output = res.stderr
  expected_output = grid['sol']
  if res.returncode < 0:
    return {'test_name': 'Check valid grid hard', 'test': forma, 'expected_result': expected_output, 'user_output': 'Error', 'test_id': grid['test_id']}
  if user_output.decode() != grid['sol']:
    return {'test_name': 'Check valid grid hard', 'test': formatted_grid, 'expected_result': grid['sol'], 'user_output': user_output, 'test_id': grid['test_id']}
  return None


def check_valid_easy():
  errors = []
  valid_grids = [
    {
      'grid': ['"..6..2..7"', '"5....7136"', '"478....2."', '"24.6.3.19"', '"..58.16.."', '"....2.753"', '"16..3.29."', '"..31....."', '"......3.1"'],
      'sol': '3 1 6 5 9 2 4 8 7\n5 9 2 4 8 7 1 3 6\n4 7 8 3 1 6 9 2 5\n2 4 7 6 5 3 8 1 9\n9 3 5 8 7 1 6 4 2\n6 8 1 9 2 4 7 5 3\n1 6 4 7 3 5 2 9 8\n8 2 3 1 6 9 5 7 4\n7 5 9 2 4 8 3 6 1\n',
      'test_id': 9
    },
    {
      'grid': ['"6.83.2.9."', '".91.48.6."', '"4.3619578"', '"81.97...."', '".5482...."', '"9......25"', '"1.95...47"', '"..6.8..53"', '".352..18."'],
      'sol': '6 7 8 3 5 2 4 9 1\n5 9 1 7 4 8 3 6 2\n4 2 3 6 1 9 5 7 8\n8 1 2 9 7 5 6 3 4\n3 5 4 8 2 6 7 1 9\n9 6 7 4 3 1 8 2 5\n1 8 9 5 6 3 2 4 7\n2 4 6 1 8 7 9 5 3\n7 3 5 2 9 4 1 8 6\n',
      'test_id': 10
    },
    {
      'grid': ['"62.....45"', '".5.32..1."', '"...4.8..."', '"78.5.2.63"', '"..4.8.5.."', '"56.9.3.82"', '"...2.9..."', '".1..65.7."', '"87.....29"'],
      'sol': '6 2 3 7 9 1 8 4 5\n4 5 8 3 2 6 9 1 7\n1 9 7 4 5 8 2 3 6\n7 8 9 5 1 2 4 6 3\n2 3 4 6 8 7 5 9 1\n5 6 1 9 4 3 7 8 2\n3 4 6 2 7 9 1 5 8\n9 1 2 8 6 5 3 7 4\n8 7 5 1 3 4 6 2 9\n',
      'test_id': 11
    },
    {
      'grid': ['".39725841"', '"24.98.763"', '"781436.2."', '"86325.417"', '".2.1.7938"', '"197843652"', '"458372196"', '"31659827."', '".....4.8."'],
      'sol': '6 3 9 7 2 5 8 4 1\n2 4 5 9 8 1 7 6 3\n7 8 1 4 3 6 5 2 9\n8 6 3 2 5 9 4 1 7\n5 2 4 1 6 7 9 3 8\n1 9 7 8 4 3 6 5 2\n4 5 8 3 7 2 1 9 6\n3 1 6 5 9 8 2 7 4\n9 7 2 6 1 4 3 8 5\n',
      'test_id': 12
    }
  ]
  for grid in valid_grids:
    ret = check_easy(grid)
    if ret:
      errors.append(ret)
  return errors

def check_valid_medium():
  errors = []
  valid_grids = [
    {
      'grid': ['"95..31.6."', '".1....5.9"', '".4.5....."', '"..1.683.."', '"........."', '"..314.8.."', '".....6.3."', '"7.4....1."', '".3.27..46"'],
      'sol': '9 5 2 8 3 1 4 6 7\n3 1 7 6 2 4 5 8 9\n8 4 6 5 9 7 1 2 3\n5 2 1 7 6 8 3 9 4\n4 8 9 3 5 2 6 7 1\n6 7 3 1 4 9 8 5 2\n2 9 5 4 1 6 7 3 8\n7 6 4 9 8 3 2 1 5\n1 3 8 2 7 5 9 4 6\n',
      'test_id': 13
    },
    {
      'grid': ['"3..49...."', '".82......"', '"7......15"', '"..417268."', '"........."', '".138465.."', '"83......9"', '"......73."', '"....61..8"'],
      'sol': '3 6 1 4 9 5 8 7 2\n5 8 2 7 1 3 9 6 4\n7 4 9 6 2 8 3 1 5\n9 5 4 1 7 2 6 8 3\n6 7 8 5 3 9 4 2 1\n2 1 3 8 4 6 5 9 7\n8 3 6 2 5 7 1 4 9\n1 2 5 9 8 4 7 3 6\n4 9 7 3 6 1 2 5 8\n',
      'test_id': 14
    },
    {
      'grid': ['".5....3.9"', '".8....7.."', '"....1...."', '".3.7....."', '"..2....14"', '"...5....."', '"..1.4..2."', '".....9..."', '"......5.."'],
      'sol': '1 5 6 4 7 2 3 8 9\n2 8 4 9 5 3 7 6 1\n3 9 7 6 1 8 4 5 2\n4 3 8 7 2 1 6 9 5\n5 7 2 3 9 6 8 1 4\n6 1 9 5 8 4 2 3 7\n7 6 1 8 4 5 9 2 3\n8 4 5 2 3 9 1 7 6\n9 2 3 1 6 7 5 4 8\n',
      'test_id': 15
    },
    {
      'grid': ['"9...4...."', '"....1.2.."', '"37......5"', '".......9."', '"..1...4.."', '"...7.5..."', '"....2.1.."', '"58.3....."', '"........."'],
      'sol': '9 1 2 5 4 7 3 6 8\n8 6 5 9 1 3 2 7 4\n3 7 4 6 8 2 9 1 5\n2 3 8 1 6 4 5 9 7\n7 5 1 2 9 8 4 3 6\n4 9 6 7 3 5 8 2 1\n6 4 7 8 2 9 1 5 3\n5 8 9 3 7 1 6 4 2\n1 2 3 4 5 6 7 8 9\n',
      'test_id': 16
    }
  ]
  for grid in valid_grids:
    ret = check_medium(grid)
    if ret:
      errors.append(ret)
  return errors

def check_valid_hard():
  errors = []
  valid_grids = [
    {
      'grid': ['".6.1..9.."', '"....5...2"', '"...2....4"', '"61.5..3.."', '".3..6..5."', '"..2..8.71"', '"3....2..."', '"9...3...."', '"..1..5.9."'],
      'sol': '2 6 4 1 8 7 9 3 5\n1 8 9 4 5 3 7 6 2\n7 5 3 2 9 6 8 1 4\n6 1 7 5 2 9 3 4 8\n4 3 8 7 6 1 2 5 9\n5 9 2 3 4 8 6 7 1\n3 4 6 9 1 2 5 8 7\n9 7 5 8 3 4 1 2 6\n8 2 1 6 7 5 4 9 3\n',
      'test_id': 17
    },
    {
      'grid': ['".1...4..."', '"...5..9.."', '"68..1..2."', '"......48."', '"578...263"', '".24......"', '".5..3..96"', '"..1..6..."', '"...2...1."'],
      'sol': '9 1 3 7 2 4 6 5 8\n2 4 7 5 6 8 9 3 1\n6 8 5 9 1 3 7 2 4\n1 6 9 3 7 2 4 8 5\n5 7 8 4 9 1 2 6 3\n3 2 4 6 8 5 1 7 9\n4 5 2 1 3 7 8 9 6\n7 9 1 8 5 6 3 4 2\n8 3 6 2 4 9 5 1 7\n',
      'test_id': 19
    },
    {
      'grid': ['"..32.7..."', '".9.....7."', '".4....8.."', '"..7349.8."', '"..1...5.."', '".3.1567.."', '"..6....3."', '".1.....9."', '"...7.42.."'],
      'sol': '1 8 3 2 6 7 9 5 4\n6 9 5 4 8 1 3 7 2\n7 4 2 5 9 3 8 1 6\n5 2 7 3 4 9 6 8 1\n9 6 1 8 7 2 5 4 3\n8 3 4 1 5 6 7 2 9\n4 7 6 9 2 8 1 3 5\n2 1 8 6 3 5 4 9 7\n3 5 9 7 1 4 2 6 8\n',
      'test_id': 19
    }
  ]
  for grid in valid_grids:
    ret = check_hard(grid)
    if ret:
      errors.append(ret)
  return errors
