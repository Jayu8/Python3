"""
Like Java python has Immutable Strings unlike C and C++
Indexing :   J(0)K(1) , J(-2)K(-1)   
Encoding UTF32,16 and 8. Earlier ASCII was used
UTF-8 is variable length encoding english -1 byte,chinese-2 etc
Characters correspond to graphemes, the fundamental units of written or printed language.(Graphics)

Byte Strings
Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings. 
Every string or text in Python 3 is Unicode, but encoded Unicode is represented as binary data.
The type used to hold text is str, the type used to hold data is bytes. 
It's not possible to mix text and data in Python 3; it will raise TypeError. 
>>> x = b"Hallo"
>>> t = str(x)
>>> u = t.encode("UTF-8")

"""
