# Textwrap
#
# The textwrap module provides two convenient functions: wrap() and fill().
#
# textwrap.wrap()
# The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
# It returns a list of output lines.

def wrap(string, max_width):
    return textwrap.fill(string,max_width)