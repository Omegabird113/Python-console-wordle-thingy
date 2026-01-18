WORD_LEVELS: dict[int,list[str]] = {
    3: ['bat', 'dog', 'toy', 'cat', 'rat', 'law', 'mud', 'boy', 'the', 'she', 'red', 'pop', 'lie', 'bay', 'hay', 'can', 'sad', 'mad', 'cap', 'rap', 'met', 'fad', 'hop', 'top', 'tap', 'lap', 'lie', 'bag', 'ham', 'ray', 'say', 'tie', 'bit', 'hit', 'hat', 'bet', 'bid', 'lid', 'pad', 'and', 'tan', 'tar', 'eat', 'ate', 'lag', 'rag', 'tag', 'kid', 'dip', 'rip', 'lip', 'pod', 'rod', 'nod', 'his', 'sis', 'gem', 'ant', 'wad', 'win', 'nap', 'way', 'pay', 'day', 'van', 'mom', 'dad', 'dot', 'rot', 'tip', 'hen', 'tin', 'fee', 'pee', 'tee', 'tea', 'pea', 'bee', 'sea', 'see', 'men', 'man', 'did', 'sim', 'pin', 'fib', 'yay', 'may', 'pot', 'pan', 'run', 'ran', 'ton', 'put', 'hut', 'but', 'cut', 'pit', 'vat'],
    5: ['lemon', 'happy', 'angry', 'carve', 'water', 'walks', 'visit', 'liver', 'house', 'train', 'spoon', 'tiger', 'zebra', 'teach', 'study', 'juice', 'never', 'peace', 'donor', 'uncle', 'table', 'river', 'cycle', 'queen', 'piano', 'sunny', 'sweet', 'dirty', 'clean', 'apple', 'refer', 'climb', 'light', 'shelf', 'tired', 'party', 'brain', 'vault', 'cover', 'paper', 'hello'],
    6: ['cheese', 'tomato', 'tattoo', 'flight', 'height', 'skirts', 'doctor', 'bottle', 'python', 'coding', 'sleeps', 'wonder', 'growth', 'forest', 'yellow', 'purple', 'pillow', 'school', 'yogurt', 'bouncy', 'flavor', 'guitar', 'breeze', 'window', 'marvel', 'gloves', 'framed', 'coffee', 'button', 'minute', 'wobble', 'tennis', 'winter', 'pencil', 'pizazz'],
    8: ['suburban', 'assuming', 'abundant', 'hygienic', 'medieval', 'tomorrow', 'zucchini'],
    9: ['xylophone', 'wednesday', 'versatile', 'unanimous', 'temporary', 'limousine', 'auxiliary', 'boulevard', 'labyrinth', 'lightning', 'medicinal', 'mezzanine', 'pneumonia', 'quadruple', 'sophomore'],
    10: ['absolutely', 'university', 'stewardess', 'withdrawal', 'vulnerable', 'veterinary', 'vegetarian', 'trajectory', 'tournament', 'psychology', 'plagiarism', 'pilgrimage', 'philosophy', 'nutritious', 'mayonnaise', 'leprechaun', 'cantaloupe', 'auditorium', 'apostrophe', 'adjustment', 'behavioral', 'camouflage', 'laboratory', 'lieutenant', 'legitimate', 'likelihood', 'masquerade', 'noticeable', 'pilgrimage', 'ridiculous', 'chandelier', 'suspicious', 'synonymous'],
    11: ['monstrosity', 'accommodate', 'overzealous', 'vaccination', 'temperature', 'necessarily', 'fluorescent', 'cauliflower', 'bureaucracy', 'description', 'exaggerated', 'fascinating', 'immediately', 'maintenance', 'mischievous', 'opportunity', 'picturesque', 'prohibitive', 'rudimentary', 'superfluous', 'susceptible'],
    12: ['cheeseburger', 'transmission', 'surveillance', 'practitioner', 'marshmallows', 'kindergarten', 'interference', 'inflammation', 'handkerchief', 'exhilaration', 'choreography', 'amphitheater', 'advantageous', 'abbreviation', 'ambidextrous', 'asymmetrical', 'bachelorette', 'enthusiastic', 'entrepreneur', 'governmental', 'overwhelming', 'sacrilegious'],
    13: ['visualization', 'pronunciation', 'participation', 'miscellaneous', 'knowledgeable', 'extraordinary', 'environmental', 'accommodation', 'determination', 'dysfunctional', 'eavesdropping', 'individuality', 'misunderstood'],
    14: ['photosynthesis', 'responsibility', 'recommendation', 'pharmaceutical', 'disappointment', 'circumstantial', 'impressionable', 'interpretation']
}

def get_words_list(min_length: int, max_length: int) -> list[str]:
    return_list: list[str] = []
    for key, val in WORD_LEVELS.items():
        if min_length <= key <= max_length:
            return_list.extend(val)
    return return_list
