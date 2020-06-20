from collections import namedtuple

def partitionsin(limit, size):
  rsums = []
  for e in limit:
    rsums.append(e + (rsums[-1] if rsums else 0))
  rsums.reverse()

  def _p(parts, level, rem):
    if rem == 0 and len(parts) <= len(limit):
      yield parts
      return

    if rem < 0 or level >= len(limit) or rsums[level] < rem:
      yield from ()
      return

    max_part = min(rem, limit[level], parts[-1] if parts else size)
    for m in range(max_part+1):
      yield from _p(parts + (m,), level+1, rem-m)

    yield from ()
    return

  return _p((), 0, size)


Vars = namedtuple('Vars', ['parts', 'level', 'rem'])

class PartitionsIn:
  def __init__(self, limit, size):
    self.limit = limit
    self.size = size

    rsums = []
    for e in limit:
      rsums.append(e + (rsums[-1] if rsums else 0))
    rsums.reverse()
    self.rsums = rsums

    self.callStack = [Vars((), 0, size)]

  def Next(self):
    while self.callStack:
      print(self.callStack)
      v = self.callStack.pop()

      if v.rem == 0 and len(v.parts) <= len(self.limit):
        return v.parts

      if v.rem < 0 or v.level >= len(self.limit) or self.rsums[v.level] < v.rem:
        continue

      min_part = 1
      max_part = min(v.rem, self.limit[v.level], v.parts[-1] if v.parts else self.size)
      print(min_part, max_part)

      self.callStack.extend([
        Vars(v.parts+(m,), v.level+1, v.rem-m)
        for m in range(max_part, min_part-1, -1)
      ])

    return None


VarsT = namedtuple('VarsT', ['parts', 'level', 'rem', 'mn', 'mx', 'cameFrom'])
class PartitionsInT:
  def __init__(self, limit, size):
    self.limit = limit
    self.size = size

    rsums = []
    for e in limit:
      rsums.append(e + (rsums[-1] if rsums else 0))
    rsums.reverse()
    self.rsums = rsums

    self.callStack = [VarsT((), 0, size, 1, None, None)]

  def GoBack_(self, v):
    if v.cameFrom is None: return False
    last = v.cameFrom._replace(mn=v.cameFrom.mn+1)
    self.callStack.append(last)
    return True

  def Next(self):
    while self.callStack:
      v = self.callStack.pop()

      if v.rem == 0 and len(v.parts) <= len(self.limit):
        if not self.GoBack_(v): break
        return v.parts

      if v.rem < 0 or v.level >= len(self.limit) or self.rsums[v.level] < v.rem:
        if not self.GoBack_(v): break
        continue

      if v.mx is None:
        max_part = min(v.rem, self.limit[v.level], v.parts[-1] if v.parts else self.size)
        v = v._replace(mx=max_part)
        if v.mn > v.mx:
          if not self.GoBack_(v): break
          continue
        self.callStack.append(VarsT(v.parts+(1,), v.level+1, v.rem-1, 1, None, v))
      else:
        if v.mn > v.mx:
          if not self.GoBack_(v): break
          continue
        self.callStack.append(VarsT(v.parts+(v.mn,), v.level+1, v.rem-v.mn, 1, None, v))
    return None


class PartitionsInTT:
  def __init__(self, limit, size):
    self.limit = limit
    self.size = size

    rsums = []
    for e in limit:
      rsums.append(e + (rsums[-1] if rsums else 0))
    rsums.reverse()
    self.rsums = rsums

    self.callStack = [VarsT((), 0, size, 1, None, None)]

  def GoBack_(self, v):
    if v.cameFrom is None: return False
    last = v.cameFrom._replace(mn=v.cameFrom.mn+1)
    self.callStack.append(last)
    return True

  def Next(self):
    while self.callStack:
      v = self.callStack.pop()

      if v.rem == 0 and len(v.parts) <= len(self.limit):
        if not self.GoBack_(v): break
        return v.parts
      elif v.rem < 0 or v.level >= len(self.limit) or self.rsums[v.level] < v.rem or \
          (len(v.parts) > 0 and v.parts[-1]*(len(self.limit)-len(v.parts)) < v.rem):
        if not self.GoBack_(v): break
      elif v.mx is None:
        max_part = min(v.rem, self.limit[v.level], v.parts[-1] if v.parts else self.size)
        v = v._replace(mx=max_part)
        if v.mn <= v.mx:
          self.callStack.append(VarsT(v.parts+(1,), v.level+1, v.rem-1, 1, None, v))
        elif not self.GoBack_(v): break
      elif v.mn <= v.mx:
        self.callStack.append(VarsT(v.parts+(v.mn,), v.level+1, v.rem-v.mn, 1, None, v))
      elif not self.GoBack_(v): break

    return None

p = PartitionsInTT((24, 12, 12), 24)
p.Next()
