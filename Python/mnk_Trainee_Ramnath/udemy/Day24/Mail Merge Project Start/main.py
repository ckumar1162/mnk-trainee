#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
PLACEHOLDER='[name]'
with open('./Input/Names/invited_names.txt') as data:
    nam_list=data.readlines()

with open('./Input/Letters/starting_letter.txt') as letters:
    letter_content=letters.read()
    for name in nam_list:
        stripped_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as complete_letter:
            complete_letter.write(new_letter)


