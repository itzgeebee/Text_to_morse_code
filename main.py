from morse import MorseData #import the morse code data class
import winsound #import winsound to add beep effects

morse_data = MorseData()

user_prompt = input("what would you like to convert to morse code today?\n ").upper()

answer = ""

# get all characters in user input
for i in user_prompt:
    # accounts for the space
    if i not in morse_data.morse_dictionary:
        answer += " "
        winsound.Beep(1000, 500)

    else:
        # adds the morse code character to the answer variabe
        answer += morse_data.morse_dictionary[i]
        winsound.Beep(1000, 500)
# prints the answer variable
print(answer)