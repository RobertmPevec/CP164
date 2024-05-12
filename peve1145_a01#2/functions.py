"""
------------------------------------------------------------------------
Assignment 1, Functions
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-07'
------------------------------------------------------------------------
"""


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    i = 0
    while i < len(minuend):
        if minuend[i] in subtrahend:
            minuend.pop(i)
        else:
            i += 1
    return minuend


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp = 0
    low = 0
    dig = 0
    whi = 0
    rem = 0
    for n in fv:
        for i in n:
            if i.isupper():
                upp += 1
            elif i.islower():
                low += 1
            elif i.isdigit():
                dig += 1
            elif i.isspace():
                whi += 1
            else:
                rem += 1
    return upp, low, dig, whi, rem


def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    reverse = string[::-1]
    if string.lower() == reverse.lower():
        palindrome = True
    else:
        palindrome = False
    return palindrome


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    length = len(a[0])
    b = []
    for n in range(length):
        row = []
        for i in a:
            row.append(i[n])
        b.append(row)
    return b


def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    for n in a:
        for i in n:
            b.append(i)
    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    for i in range(len(a)):
        sublist = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            sublist.append(total)
        c.append(sublist)
    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    for n in range(len(a[0])):
        turn_right = []
        for i in a:
            turn_right.append(i[n])
        turn_right.reverse()
        b.append(turn_right)
    return b


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    vowels = ["a", "e", "i", "o", "u"]
    if word[0].lower() in vowels:
        word += "way"
        pl = word
    else:
        letters = word[0:2]
        pl = word[2:]
        pl += letters.lower() + "ay"
        if word[0].isupper():
            pl = pl.capitalize()
    return pl


def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    string = string.upper()
    ciphertext = ciphertext.upper()
    check = {
        "A": ciphertext[0], "B": ciphertext[1], "C": ciphertext[2], "D": ciphertext[3],
        "E": ciphertext[4], "F": ciphertext[5], "G": ciphertext[6], "H": ciphertext[7],
        "I": ciphertext[8], "J": ciphertext[9], "K": ciphertext[10], "L": ciphertext[11],
        "M": ciphertext[12], "N": ciphertext[13], "O": ciphertext[14], "P": ciphertext[15],
        "Q": ciphertext[16], "R": ciphertext[17], "S": ciphertext[18], "T": ciphertext[19],
        "U": ciphertext[20], "V": ciphertext[21], "W": ciphertext[22], "X": ciphertext[23],
        "Y": ciphertext[24], "Z": ciphertext[25]
    }
    for letter in string:
        if letter.isnumeric():
            continue
        else:
            estring += check[letter]
    return estring
