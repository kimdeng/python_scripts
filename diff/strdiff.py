#!/usr/bin/python

import difflib

text1="""text1:
this modeule provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
text1_lines=text1.splitlines()
text2="""text2:
this module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines=text2.splitlines()
#d=difflib.Differ()
#diff=d.compare(text1_lines,text2_lines)
#print type(diff)
#print '\n'.join(list(diff))
#print type(text1_lines)

d=difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)
