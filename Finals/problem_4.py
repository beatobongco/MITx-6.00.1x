def longest_run(L):
  """
  Assumes L is a list of integers containing at least 2 elements.
  Finds the longest run of numbers in L, where the longest run can
  either be monotonically increasing or monotonically decreasing.
  In case of a tie for the longest run, choose the longest run
  that occurs first.
  Does not modify the list.
  Returns the sum of the longest run.
  """
  from operator import ge, le

  def get_longest_run_op(L, op):
    """Gets index and list of longest run that satisfies a comparison operator

    L - list
    op - operator e.g. >= (ge), <= (le)

    returns Tuple(int, list)
    """
    curr_index = None
    temp = []
    best = []
    best_index = None
    for index, value in enumerate(L):
      # Replace best
      if temp and len(temp) > len(best):
        best = temp
        best_index = curr_index

      if not temp:
        # new
        temp.append(value)
        curr_index = index
      elif op(value, temp[-1]):
        temp.append(value)
      else:
        # not continuous
        temp = [value]
        curr_index = index

    return best_index, best

  i_index, increasing = get_longest_run_op(L, ge)
  d_index, decreasing = get_longest_run_op(L, le)

  if len(increasing) == len(decreasing):
    if i_index > d_index:
      return sum(decreasing)
    return sum(increasing)
  elif len(increasing) > len(decreasing):
    return sum(increasing)
  return sum(decreasing)

assert longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]) == 26
assert longest_run([5, 4, 10]) == 9
assert longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 65

