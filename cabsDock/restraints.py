"""Module for handling distance restraints"""

from copy import copy


class Restraint:
    """Class represents single distance restraint"""
    def __init__(self, line, is_side_chain=False):
        i1, i2, d, w = line.split()
        self.id1 = i1
        self.id2 = i2
        self.distance = float(d)
        self.weight = float(w)
        self.sg = is_side_chain

    def __repr__(self):
        s = '%s %s %.4f %.2f' % (self.id1, self.id2, self.distance, self.weight)
        if self.sg:
            s += ' SG'
        return s

    def update_id(self, ids):
        self.id1 = ids[self.id1]
        self.id2 = ids[self.id2]
        return self


class Restraints:
    """Container for Restraint(s)"""
    def __init__(self, arg, sg=False):
        self.data = []
        if arg and type(arg) is list:
            self.data.extend([Restraint(str(line), sg) for line in arg])
        elif arg and type(arg) is str:
            with open(arg) as f:
                self.data.extend(Restraint(line, sg) for line in f)
        elif arg and arg.__class__.__name__ == 'Restraints':
            self.data = copy(arg.data)

    def __repr__(self):
        return '\n'.join(str(r) for r in self.data)

    def __iadd__(self, other):
        self.data.extend(other.data)
        return self

    def update_id(self, ids):
        for restr in self.data:
            restr.update_id(ids)
        return self

if __name__ == '__main__':
    pass