PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strippted_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strippted_name)
        with open(f"./Output/ReadyToSend/letter_for_{strippted_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
