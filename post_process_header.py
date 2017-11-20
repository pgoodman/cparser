"""Process a C-pre-processed file and remove extraneous pre-processor
directives, get rid of C++-isms, and do a bit of other "cleaning up".

Author:       Peter Goodman (peter.goodman@gmail.com)
Copyright:    Copyright 2012-2013 Peter Goodman, all rights reserved.
"""

import fileinput
import re
import sys

def O(*args):
  line = "".join(map(str, args))

  # watch out for C blocks
  if "(^" not in line:
    print line

def get_lines(lines):
  """Get the lines of a file as a list of strings such that no line has
  more than one brace, and that every line is C/C++ and not pre-processor
  line directives."""
  macro_defs = []
  all_lines = []

  # remove empty lines and new lines
  for line in lines:
    strip_line = line.strip(" \n\r\t")
    if not strip_line:
      continue
    
    # Turn things like `#  define` into `#define`.
    strip_line = strip_line.replace(r"#[ ]+", "#")
    if strip_line.startswith("#"):
      if strip_line.startswith("#define"):
        macro_defs.append(strip_line)
      continue

    # Ignore  pre-processor line numbers
    if not strip_line.startswith("//"):
      all_lines.append(strip_line)

  # # Inject new lines in a structured manner
  buff = " ".join(all_lines)
  buff = buff.replace(r"[ ]+", " ")  # Multiple spaces
  buff = buff.replace(" }", "\n}")
  buff = buff.replace("} ", "}\n")
  buff = buff.replace("{ ", "{\n")
  buff = buff.replace("; ", ";\n")
  buff = buff.replace("\t", " ")

  # Now there is only one brace ({ or }) per line.
  return macro_defs, buff.split("\n")


if "__main__" == __name__:
  macro_defs, lines = get_lines(fileinput.input())
  for line in lines:
    O(line)
