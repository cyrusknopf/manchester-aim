"""
This is a stub for COMP16321 coursework 1.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.
"""

# ---Section 1 --- #

#(Question:a)
def read_file():#(s)
    """
        Read in the text file and save the paragraph to a single string

        :return: A text file paragraph as a string
    """

    #Your code here
    a = open("test.txt")
    file_string = a.read()
    return(file_string)#(s)

# ---Section 2 --- #

#(Question:a)
def length_of_file():#(s)
    """
        Reports the length of the paragraph including numbers and whitespace
    
        :input_text: The text file paragraph as a string
        :return: An integer length of the file
    """
    input_text = read_file()#(s)

    #Your code here
    int_length_of_file=len(input_text)
    return(int_length_of_file)#(s)

#(Question:b)
def if_apple():#(s)
    """
        Reports a boolean True/False if the paragraph contains the entire word "apple"

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    if "apple" in input_text:
        bool_if_apple = True
    elif "APPLE" in input_text:
        bool_if_apple = True
    else:
        bool_if_apple = False


    return (bool_if_apple)#(s)

#(Question:c)
def if_upper_case_exists():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of upper case letters

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    bool_if_upper_case_exist = False
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in input_text:
        if i in upperCase:
            bool_if_upper_case_exist = True
            break
    return (bool_if_upper_case_exist)#(s)

#(Question:d)
def if_numbers_exist():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of integers

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    bool_if_numbers_exist = False
    numbers = "12345679"
    for i in input_text:
        if i in numbers:
            bool_if_numbers_exist = True
            break
    return (bool_if_numbers_exist)#(s)

#(Question:e)
def if_spaces_exist():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of blank spaces

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    bool_if_spaces_exist = False
    whiteSpace = " "
    for i in input_text:
        if i in whiteSpace:
            bool_if_spaces_exist  = True
            break
    return (bool_if_spaces_exist)#(s)

#(Question:f)
def if_first_letter_t():#(s)
    """
        Reports a boolean True/False if the first letter of the paragraph is a t

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    start = input_text[0]
    start = start.lower()
    if start == "t":
        bool_if_first_letter_t = True
    else:
        bool_if_first_letter_t = False

    return (bool_if_first_letter_t)#(s)

#(Question:g)
def fourth_letter_seventh_word():#(s)
    """
        Reports the fourth letter in the seventh word of the paragraph as a string

        :input_text: The text file paragraph as a string
        :return: A string letter
    """
    input_text = read_file()#(s)

    #Your code here
    paraWords = input_text.split()
    if len(paraWords) > 6:
        seventhWord = paraWords[6]
        if len(seventhWord) > 3:
            string_fourth_letter_seventh_word = seventhWord[3]
        else:
            string_fourth_letter_seventh_word = "out of range"
    else:
        string_fourth_letter_seventh_word = "out of range"
    return (string_fourth_letter_seventh_word)#(s)

# ---Section 3 --- #

#(Question:a)
def convert_to_lower_case():#(s)
    """
        Converts the paragraph to entirely lowercase with no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_lower_case_paragraph = input_text.lower()
    return (string_lower_case_paragraph)#(s)

#(Question:b)
def reverse_paragraph():#(s)
    """
        Reverses the paragraph such that it can be read backwards with no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_reversed_paragraph = input_text[::-1]
    return (string_reversed_paragraph)#(s)

#(Question:c)
def duplicate_and_concatenate_paragraph():#(s)
    """
        Duplicate the paragraph and combine them such that they can be read twice in order with
        no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_duplicated_paragraph = input_text + input_text
    return (string_duplicated_paragraph)#(s)

#(Question:d)
def remove_whitespace_from_paragraph():#(s)
    """
        Remove any whitespace from the paragraph except spaces between words and numbers with no
        other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_clean_paragraph = input_text.strip()
    return (string_clean_paragraph)#(s)

if __name__ == '__main__':#(s)
    #You can place any ad-hoc testing here
    test = read_file()
    print(test)
