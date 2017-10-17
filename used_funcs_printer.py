
import sys
from cparser import *

if "__main__" == __name__:
  source_lines = []
  with open(sys.argv[1]) as lines_:
    for line in lines_:
      if not line.startswith("#"):
        source_lines.append(line)

  units = CParser().parse_units(CTokenizer(source_lines))
  print 'extern "C" {'
  for decls, unit_toks, is_typedef in units:
    print " ".join(t.str for t in unit_toks)

  print '}'
  print "[[gnu::used]] static void *__mcsema_extern_funcs[] = {"
  for decls, _, _ in units:
    for ctype, name in decls:
      ctype = ctype.unattributed_type()
      if isinstance(ctype, CTypeFunction):
        print "(void *) &{},".format(name)
  print "};"
