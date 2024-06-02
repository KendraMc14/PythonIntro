def print_upper_words(words):
    """Print each word on a separate line, uppercased.

        >>> print_upper_words(["This", "is", "really", "cool"])
        THIS
        IS
        REALLY
        COOL
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word on a separate line, uppercased, if it starts with e or E.

        >>> print_upper_words2(["elbow", "East", "Paper"])
        ELBOW
        EAST
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on a separate line, uppercased, if it starts with one of the given letters.

        >>> print_upper_words3(["elbow", "East", "Paper", "Cherry", "violin"],
        ...                   must_start_with=["C", "E"])
        CHERRY
        ELBOW
        EAST
        
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break