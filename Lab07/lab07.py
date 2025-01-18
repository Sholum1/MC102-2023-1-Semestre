def main() -> None:
    """The main function of the code
    """
    # Define some important variables
    operator, operand1, operand2 = input(), input(), input()
    n_lines = int(input())
    message, concatenated_lines = [], ""
    translated_lines, translated_message = [], ""

    # Every line is a input
    for i in range(0, n_lines):
        line = input()
        concatenated_lines += line
        message.append(line)

    # Apply the find function to the operand1 and find his positions
    operand1_pos = find(concatenated_lines, operand1)
    # As specified in the problem, operand2 can only be sought from operand1
    reduced_lines = concatenated_lines[operand1_pos::]
    operand2_pos = find(reduced_lines, operand2)

    # Calculate the key value
    if operator == "+":
        key = operand1_pos + (operand1_pos+operand2_pos)
    elif operator == "-":
        key = operand1_pos - (operand1_pos+operand2_pos)
    elif operator == "*":
        key = operand1_pos * (operand1_pos+operand2_pos)

    # Use the key value to translate every character
    for i in range(len(message)):
        conc_translated_lines = ""
        for j in range(len(message[i])):
            translated_char = ord(message[i][j]) + key
            # We need to make sure that the ASCII code of the
            # translated_char is between 32 and 127
            translated_char = (translated_char - 32) % 95 + 32
            conc_translated_lines += (chr(translated_char))
        translated_lines.append(conc_translated_lines)

    # Translate the message
    for i in range(len(translated_lines)):
        if i == 0:
            translated_message += translated_lines[i]
        else:
            translated_message += "\n" + translated_lines[i]

    # Show the key and the translated message
    print(key)
    print(translated_message)


def find(concatenated_lines: str, operand: str) -> int:
    """Find the position of a determined char in a string

    Parameters:
    concatenated_lines -- string that the function will search in
    operand            -- string that will be searched for

    Returns:
    int                -- the position of the first character equal to the
                          operand
    """

    # Define the vowels
    vowels = "aeiouAEIOU"

    # If the operand is "vogal"
    if operand == "vogal":
        for i, s in enumerate(concatenated_lines):
            if s in vowels:
                return i
    # If the operand is "consoante"
    elif operand == "consoante":
        for i, s in enumerate(concatenated_lines):
            if s.isalpha() and s not in vowels:
                return i
    # If the operand is "numero"
    elif operand == "numero":
        for i, s in enumerate(concatenated_lines):
            if s.isdigit():
                return i
    # If the operand any character
    else:
        for i, s in enumerate(concatenated_lines):
            if s == operand:
                return i


if __name__ == '__main__':
    main()
