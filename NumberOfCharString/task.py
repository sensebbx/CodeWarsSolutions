def alphabet_position(text: str):
    text = text.lower()
    start_index = ord('a')
    end_index = ord('z')
    res_array = [str(ord(i) - start_index + 1) for i in text if start_index <= ord(i) <= end_index]
    return ' '.join(res_array)


def IDEAL_alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


test_string = "The sunset sets at twelve o' clock."
print(alphabet_position(test_string).replace(' ', '\t'))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11".replace(' ', '\t'))
