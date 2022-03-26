class MorseData:
    def __init__(self):
        """contains all the attributes for the morse data. The morse dictionary is created from the morse list"""
        morse_list = ['A', '._', 'N', '_.',
                           'B', '_...', 'O', '___', 'C', '_._.',
                           'P', '.__.',' D', '_..',
                           'Q', '__._', 'E', '.',  'R', '._.',
                           'F', '.._.', 'S', '...', 'G', '__.', 'T',
                           '_', 'H', '....', 'U', '.._', 'I', '..',
                           'V', '..._', 'J', '.___',
                           'W', '.__', 'K', '_._', 'X', '_.._', 'L', '._..',
                           'Y', '_.__', 'M', '__', 'Z', '__..',
                           '1', '.____', '6', '_....', '2', '..___',
                           '7', '__...', '3', '...__', '8', '___..',
                           '4', '...._', '9', '____.', '5', '.....',
                           '0', '_____',
                           ',', '__..__', '.', '._._._', '?',
                           '..__..', ';', '_._._.', ':', '___...',
                           '/', '_.._.', '-', '_...._', "'",
                           '.____.', '"', '._.._.',
                           '(', '_.__.', ')', '_.__._',
                           '=', '_..._', '+', '._._.',
                           '@', '.__._.', 'Á', '.__._', 'Ä', '._._', 'É', '.._..',
                           'Ñ', '__.__', 'Ö', '___.', 'Ü', '..__']
        self.morse_dictionary = {}
        a = 0
        b = 1
        for i in range(len(morse_list)):
            try:
                self.morse_dictionary[morse_list[a]] = morse_list[b]
                a += 2
                b += 2
            except IndexError:
                break