Python GNU C99 Declaration Parser
=================================

This is a sort-of GNU C99 declaration parser. This parser exists because:
  * I needed to parse glibc headers, Linux kernel headers, and libc as on
    Max OS X (Darwin / BSD libc?).
  * I did not want to be bound to either of gcc or clang. In retrospect, something
    like the ROSE compiler might have been best; however, at the time, I did 
    not know about it, and it would make a very large dependency as well.
  * I have a strong preference toward Python, as opposed to another scripting
    language.
  * Previous Python C parsers that I have tried [1] did not meet my needs when
    parsing glibc/Linux kernel headers.

This code includes a C tokenizer, parser, and almost certainly buggy declaration
printer. The parser assumes that code being parsed is valid--or almost valid--pre-processed GNU
C99.

This code exists as part of a much larger project. In that project, this code is used
as part of several code generators. The current focus of this other project is type and
function declarations, hence the emphasis on those aspects of the language and a
complete lack of code to parse normal expressions / statements.

[1] Note: I tried two Python C parsers some time ago, and so recent versions of 
those parsers might meet my current needs. However, that is now beside the point
because this parser meets my current needs rather well.

Maintenance
-----------
I will update this library as I discover bugs in it. I also welcome updates from
interested third parties.
