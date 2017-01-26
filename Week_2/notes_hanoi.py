def moveDiscs(numDiscs, source, destination, spare):
  """
    So this basic idea is that you want to move all of the discs
  """
  if numDiscs == 1:
    print("Move from", source, destination)
  else:
    moveDiscs(numDiscs - 1, source, spare, destination)
    moveDiscs(1, source, destination, spare)
    moveDiscs(numDiscs - 1, spare, destination, source)

moveDiscs(3, "P1", "P2", "P3")