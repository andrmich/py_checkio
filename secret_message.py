def find_message(text: str) -> str:
    """Find a secret message"""
    text = text.replace(' ', '')
    n_text = ''
    for c in text:
        if c.isupper():
            n_text += c
    return n_text

#''.join(x for x in n if x.isupper())

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
