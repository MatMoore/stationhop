import stations

shifted = [
    'abc',
    'bcd',
    'cde',
    'def',
    'efg',
    'fgh',
    'ghi',
    'hia',
    'iab'
]

redundancies = [
    'abc',
    'ab',
    'de',
    'def',
    'gh',
    'ghi',
]

def check_solution(words, expected):
  solver = stations.Solver(words)
  steps = solver.solve()
  assert steps == len(expected)
  result = solver.rebuild()
  assert result == expected

def test_convert_back():
  solver = stations.Solver(shifted)
  for i in range(255):
    s = solver.alphabets.decode(i)
    assert solver.alphabets.encode(s) == i

def test_convert_back_unordered():
  solver = stations.Solver(['a', 'c', 'e'])
  for i in range(2**3):
    s = solver.alphabets.decode(i)
    assert solver.alphabets.encode(s) == i

def test_cases():
  yield check_solution, shifted, set(('abc', 'def', 'ghi'))
  yield check_solution, redundancies, set(('abc', 'def', 'ghi'))

  yield check_solution, [
      'a b c',
      'd e f',
      'g h i',
      ' $:@~',
  ], set(('a b c', 'd e f', 'g h i'))

  yield check_solution, [
      'abcde',
      'abf',
      'cdg',
      'eh'
  ], set(('abf', 'cdg', 'eh'))

  yield check_solution, [
      'ab',
      'abf',
      'cdg',
      'edh'
  ], set(('abf', 'cdg', 'edh'))
