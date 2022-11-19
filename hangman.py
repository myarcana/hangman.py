import functools
import math
import random
import sys

from string import ascii_lowercase


title = r'''
DDDDDDDDDDDDD                                                    tttt         hhhhhhh             
D::::::::::::DDD                                              ttt:::t         h:::::h             
D:::::::::::::::DD                                            t:::::t         h:::::h             
DDD:::::DDDDD:::::D                                           t:::::t         h:::::h             
  D:::::D    D:::::D     eeeeeeeeeeee    aaaaaaaaaaaaa  ttttttt:::::ttttttt    h::::h hhhhh       
  D:::::D     D:::::D  ee::::::::::::ee  a::::::::::::a t:::::::::::::::::t    h::::hh:::::hhh    
  D:::::D     D:::::D e::::::eeeee:::::eeaaaaaaaaa:::::at:::::::::::::::::t    h::::::::::::::hh  
  D:::::D     D:::::De::::::e     e:::::e         a::::atttttt:::::::tttttt    h:::::::hhh::::::h 
  D:::::D     D:::::De:::::::eeeee::::::e  aaaaaaa:::::a      t:::::t          h::::::h   h::::::h
  D:::::D     D:::::De:::::::::::::::::e aa::::::::::::a      t:::::t          h:::::h     h:::::h
  D:::::D     D:::::De::::::eeeeeeeeeee a::::aaaa::::::a      t:::::t          h:::::h     h:::::h
  D:::::D    D:::::D e:::::::e         a::::a    a:::::a      t:::::t    tttttth:::::h     h:::::h
DDD:::::DDDDD:::::D  e::::::::e        a::::a    a:::::a      t::::::tttt:::::th:::::h     h:::::h
D:::::::::::::::DD    e::::::::eeeeeeeea:::::aaaa::::::a      tt::::::::::::::th:::::h     h:::::h
D::::::::::::DDD       ee:::::::::::::e a::::::::::aa:::a       tt:::::::::::tth:::::h     h:::::h
DDDDDDDDDDDDD            eeeeeeeeeeeeee  aaaaaaaaaa  aaaa         ttttttttttt  hhhhhhh     hhhhhhh
      :::::::: :::::::::::   :::   :::   :::    ::: :::            ::: ::::::::::: ::::::::  ::::::::: 
    :+:    :+:    :+:      :+:+: :+:+:  :+:    :+: :+:          :+: :+:   :+:    :+:    :+: :+:    :+: 
   +:+           +:+     +:+ +:+:+ +:+ +:+    +:+ +:+         +:+   +:+  +:+    +:+    +:+ +:+    +:+  
  +#++:++#++    +#+     +#+  +:+  +#+ +#+    +:+ +#+        +#++:++#++: +#+    +#+    +:+ +#++:++#:    
        +#+    +#+     +#+       +#+ +#+    +#+ +#+        +#+     +#+ +#+    +#+    +#+ +#+    +#+    
#+#    #+#    #+#     #+#       #+# #+#    #+# #+#        #+#     #+# #+#    #+#    #+# #+#    #+#     
######## ########### ###       ###  ########  ########## ###     ### ###     ########  ###    ###   
'''

game_over_screen = r'''
 ___________.._______                                                                                             
| .__________))______|                                                                                            
| | / /      ||                                                                                            ,---,  
| |/ /       ||                                                                                         ,`--.' |  
| | /        ||.-''.       .--.--.                                                                      |   :  :  
| |/         |/  _  \     /  /    '.                                                                    '   '  ;  
| |          ||  `/,|    |  :  /`. /          ,--,                                                      |   |  |  
| |          (\\`_.'     ;  |  |--`         ,'_ /|                                 .--.--.    .--.--.   '   :  ;  
| |         .-`--'.      |  :  ;_      .--. |  | :    ,---.     ,---.     ,---.   /  /    '  /  /    '  |   |  '  
| |        /Y . . Y\      \  \    `. ,'_ /| :  . |   /     \   /     \   /     \ |  :  /`./ |  :  /`./  '   :  |  
| |       // |   | \\      `----.   \|  ' | |  . .  /    / '  /    / '  /    /  ||  :  ;_   |  :  ;_    ;   |  ;  
| |      //  | . |  \\     __ \  \  ||  | ' |  | | .    ' /  .    ' /  .    ' / | \  \    `. \  \    `. `---'. |  
| |     ')   |   |   (`   /  /`--'  /:  | : ;  ; | '   ; :__ '   ; :__ '   ;   /|  `----.   \ `----.   \ `--..`;  
| |          ||'||       '--'.     / '  :  `--'   \'   | '.'|'   | '.'|'   |  / | /  /`--'  //  /`--'  /.--,_     
| |          || ||         `--'---'  :  ,      .-./|   :    :|   :    :|   :    |'--'.     /'--'.     / |    |`.  
| |          || ||                    `--`----'     \   \  /  \   \  /  \   \  /   `--'---'   `--'---'  `-- -`, ; 
| |          || ||                                   `----'    `----'    `----'                           '---`"  
| |         / | | \                           _                          _   _   _                                
""""""""""|_`-' `-' |"""|     _  _ ___ _  _  | |_  __ _ _ _  __ _ ___ __| | | |_| |_  ___   _ __  __ _ _ _        
|"|"""""""\ \       '"|"|    | || / _ \ || | | ' \/ _` | ' \/ _` / -_) _` | |  _| ' \/ -_) | '  \/ _` | ' \       
| |        \ \        | |     \_, \___/\_,_| |_||_\__,_|_||_\__, \___\__,_|  \__|_||_\___| |_|_|_\__,_|_||_|_)    
: :         \ \       : :     |__/                          |___/                                                 
. .          `'       . .
'''

win_screen = r'''
        .---.   ____     __   ,-----.      ___    _         .--.      .--..-./`) ,---.   .--. .---.         
(``--._ \   /   \   \   /  /.'  .-,  '.  .'   |  | |        |  |_     |  |\ .-.')|    \  |  | \   / _.--``) 
 `-._ _\|   |    \  _. /  '/ ,-.|  \ _ \ |   .'  | |        | _( )_   |  |/ `-' \|  ,  \ |  | |   |/_ _.-`  
   ( ` )\\ /      _( )_ .';  \  '_ /  | :.'  '_  | |        |(_ o _)  |  | `-'`"`|  |\_ \|  |  \ //( ' )    
  (_{;}_))v   ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|        | (_,_) \ |  | .---. |  _( )_\  |   v((_{;}_)   
   (_,_)/_ _ |   |(_,_)'  : (  '\_/ \   ;' (`. _` /|        |  |/    \|  | |   | | (_ o _)  |  _ _\(_,_)    
 .-'   /(_I_)|   `-'  /    \ `"/  \  ) / | (_ (_) _)        |  '  /\  `  | |   | |  (_,_)\  | (_I_)\   `-.  
(_.---'(_(=)_)\      /      '. \_/``".'   \ /  . \ /        |    /  \    | |   | |  |    |  |(_(=)_)`---._) 
        (_I_)  `-..-'         '-----'      ``-'`-''         `---'    `---` '---' '--'    '--' (_I_)
'''


hangman_pictures = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def mistakes_and_hangman(mistakes: set[str], hangman_pictures: list[str], seed: int) -> str:
    r'''Returns an ascii art string showing the cloud of mistake guesses and the hangman picture

    :param mistakes: the set of letters to draw in the cloud of wrong guesses next to the hangman
    :param hangman_pictures: an ordered list of ascii-art strings representing the stages from empty gallows to game end
    :param seed: the seed for the mistakes cloud randomisation, each instance of the game should probably draw the same
        mistakes cloud for each turn
    '''
    try:
        hangman = hangman_pictures[len(mistakes)]
    except IndexError:
        hangman = hangman_pictures[-1]
    mistakes_cloud_height = len(hangman.splitlines())
    mistakes_cloud = make_mistakes_cloud(mistakes, seed, mistakes_cloud_height)
    lines = []
    for pair in zip(mistakes_cloud.splitlines(), hangman.splitlines()):
        line = ''.join(pair)
        lines.append(line)
    return '\n'.join(lines)


def make_mistakes_cloud(mistakes: set[str], seed: int, height: int) -> str:
    shape = mistakes_cloud_shape(height, seed)
    characters = [[letter if letter in mistakes else ' ' for letter in row] for row in shape]
    return '\n'.join([''.join(line) for line in characters])


def bell(x, mean, stddev):
    r'''Gaussian bell curve shape with highest point at (mean, 1)'''
    #  height = 1 / (stddev * math.sqrt(2 * math.pi))
    return math.exp(-0.5 * (x - mean) ** 2 / stddev ** 2)


def calc_stddev(row_number, height, widest_value, narrowest_value, rate_of_narrowing):
    r'''Generate a stddev suitable for distributing the missed guesses of one row of the mistakes cloud.

    The topmost rows should have a much less concentrated spread of letters than the bottom rows, which
    should be tightly constrained around the means of those rows to look like the tail of a genie coming out
    of a lamp.

    :param rate_of_narrowing: between -1 and 1, a larger value means the stddev shrinks faster. 0 is linear
    '''
    right_bound = height - 1
    a_x, a_y = (0, widest_value)
    def straight_line_between(x0, y0, x1, y1):
        return lambda x: y0 + (x - x0) * (y1 - y0) / (x1 - x0)
    control_point_x = right_bound/2 - rate_of_narrowing * right_bound / 2
    control_point_y = straight_line_between(0, narrowest_value, right_bound, widest_value)(control_point_x)
    b_x, b_y = (control_point_x, control_point_y)
    c_x, c_y = (right_bound, narrowest_value)
    x = row_number
    t = (a_x-b_x + math.sqrt((a_x - b_x)**2-(a_x-x)*(a_x-2*b_x+c_x))) / (a_x - 2*b_x + c_x)
    y = a_y*(1-t)**2 + 2*b_y*t*(1-t)+c_y*t**2
    return y


def calc_mean(row_number, height, max_offset, funnel_factor, wavelength, seed):
    r'''Generate a mean according to a formula that will produce a sinuous smoke wisp shape.

    :param height: the total height in rows that the wisp will be
    :param max_offset: how horizontally far from 0 the widest point of inflection should be
    :param funnel_factor: a number 0 to 1, how much narrower the curves at the base of the wisp should be than the top
    :param wavelength: how much approximate distance (in terms of row_number) should there be between same-sided points of inflection
    :param seed: seed for the random number generator used to make the shape of the wisp different in different game instances
    :returns: the horizontal offset from the middle of the mistakes cloud that this row should be drawn at
    '''
    rand = random.Random()
    rand.seed(seed)
    funneling_factor = math.exp(math.log(funnel_factor)/height * row_number)
    translated_row_number = row_number + rand.randint(0, wavelength) # the offset should start according to RNG
    transformed_row_number = 2 * math.pi / wavelength * translated_row_number # scale to satisfy wavelength
    return max_offset * funneling_factor * math.sin(transformed_row_number)


@functools.cache
def mistakes_cloud_shape(height: int, seed: int) -> list[list[str]]:
    r'''Generate a 2D scattering of the alphabet in a grid according to a seeded random shape.

    At the moment, I'm going for a wisp-of-smoke/genie shape:
        #  # # #  #
      #   #
            # #  
         # #
      #
       #
    The method implemented is to align normal distributions horizontally with the middle of the smoke on each row
    according to some random sinusoid, and then placing the letters by weighted chance according to that distribution.
    '''
    rand = random.Random()
    rand.seed(seed)
    distribution = []
    width = height * 3
    noise = 8e-3 # each cell in the distribution gets noise% uniform randomisation
    funnel_factor = 0.2 # ratio of the amplitudes of the curves of the bottom of the wisp and the top
    wavelength = height # in number of rows
    amplitude = width / 2 # the greatest distance of the curve from 0
    widest_stddev = height
    narrowest_stddev = height / 10
    tightening_factor = 1 # how quickly the width of the wisp should narrow
    for row_number in range(height):
        row = []
        distribution.append(row)
        mean = calc_mean(row_number, height, amplitude, funnel_factor, wavelength, seed)
        stddev = calc_stddev(row_number, height, widest_stddev, narrowest_stddev, tightening_factor)
        for x in range(-width // 2 + 1, width // 2 + 1):
            row.append(bell(x, mean, stddev) * rand.uniform(1-noise, 1+noise))
    grid = [[None for _ in range(width)] for _ in range(height)] # the output grid of letter positions
    for letter in rand.sample(ascii_lowercase, len(ascii_lowercase)):
        # get the largest value from the distribution, place the letter there, then set adjacent probabilities in the distribution to zero
        flat_distribution = [p for row in distribution for p in row]
        flat_index = flat_distribution.index(max(flat_distribution))
        expected_row, expected_col = divmod(flat_index, width)
        grid[expected_row][expected_col] = letter
        distribution[expected_row][expected_col] = 0 # stop future letters being placed here
        if expected_row > 0: # no vertical adjacency
            distribution[expected_row - 1][expected_col] = 0
        if expected_row < height - 1:
            distribution[expected_row + 1][expected_col] = 0
        if expected_col > 0: # no horizonal adjacency
            distribution[expected_row][expected_col - 1] = 0
        if expected_col < width - 1:
            distribution[expected_row][expected_col + 1] = 0
    return grid


def masked_word(word: str, letters_guessed: set[str]) -> str:
    r'''Create the hangman hint based on the word and (correct) letters guessed so far.
    >>> masked_word('hello', {'e'})
    '_ e _ _ _'
    >>> masked_word('indubitable', {'i', 'l'})
    'i _ _ _ _ i _ _ _ l _'
    '''
    return ' '.join([letter if letter in letters_guessed else '_' for letter in word])


if __name__ == '__main__':
    with open('common_words.txt', 'r') as f:
        common_words = f.read().splitlines()
    word = random.choice(common_words)

    art_seed = random.randint(0, sys.maxsize)
    hint_indent = len(hangman_pictures[0].splitlines())
    alphabet = set(ascii_lowercase)
    mistakes = set()
    correct = set()
    print(title)
    while len(mistakes) < len(hangman_pictures):
        print(mistakes_and_hangman(mistakes, hangman_pictures, art_seed))
        print(' ' * hint_indent, masked_word(word, correct))
        guess = input('Please guess a letter: ')
        while guess not in alphabet:
            guess = input("Please enter a single lowercase letter, like 'a', 'b', ... 'z': ")
        if guess in word:
            correct.add(guess)
            if len(set(word) - correct) == 0:
                break
        else:
            mistakes.add(guess)
        print() # blank line, separate the turns
    if len(mistakes) < len(hangman_pictures):
        print(mistakes_and_hangman(mistakes, hangman_pictures, art_seed))
        print(' ' * hint_indent, masked_word(word, correct))
        print(win_screen)
        print(f'You got it! The word was {word}.')
    else:
        print(mistakes_and_hangman(mistakes, hangman_pictures, art_seed))
        print(game_over_screen)
        print('You got as far as:', masked_word(word, correct))
        print('The word was:', word)

