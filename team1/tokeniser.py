# coding=utf8

import re

word_re = r"(?:\w+(?:[':-]\w+)? ?)|(?:\r|\n)+|. +|."
s=u"12:34\tThe quick-brown\r\nfox. jumps,\no'er the \r\n £2 l*zy dog! 12:35 END"
words = re.findall(word_re, s)
s2 = ''.join(words)

print s
print
print words
print
print s2
print 'Same' if s==s2 else 'Different'