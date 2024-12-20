
with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day24_mailmerge\Mail Merge Project Start\Input\Names\invited_names.txt") as fp_name:
    name = fp_name.readlines()

with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day24_mailmerge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as fp_letter:
    letter = fp_letter.read()
    for item in name:
        stripped_name = item.strip()
        new_letter = letter.replace("[name]",stripped_name)
        with open(f"mnk-trainee/Python/Mnk-trainee-Vidhya_S_A/udemy_100_days/day24_mailmerge/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as file:
            file.write(new_letter)
