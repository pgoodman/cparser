
import sys
import fileinput
from cparser import *

if "__main__" == __name__:
  source_lines = []
  for line in fileinput.input():
    if not line.startswith("#"):
      source_lines.append(line)

  units = CParser().parse_units(CTokenizer(source_lines))
  for decls, _, _ in units:
    for ctype, name in decls:
      ctype = ctype.unattributed_type()
      if isinstance(ctype, CTypeFunction):
        if ctype.is_variadic:
          print name, 16, "C", "N"
        else:
          print name, len(ctype.param_types), "C", "N"
