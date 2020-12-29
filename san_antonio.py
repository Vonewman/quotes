import random
import json


def read_values_from_json(file, key):
    """Give a Json file and return a list"""
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values


def clean_strings(sentences):
    """Give a json and return a list"""
    cleaned = []
    # stores quotes on a list. Create an empty list and ea
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()
        # don't use extend as it adds each letter one by one!
        cleaned.append(clean_sentence)
    return cleaned


def random_item_in(object_list):
    """Return a random item in a list"""
    rand_numb = random.randint(0, len(object_list) - 1)
    return object_list[rand_numb]


def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item_in(clean_values)


#################
##### QUOTES ####
#################

# Gather quotes from San Antonio

def random_quote():
    return random_value('quotes.json', 'quote')

#################
### CHARACTERS ##
#################

# Gather characters from Wikipedia


def random_character():
    return random_value('characters.json', 'character')


#################
## INTERACTION ##
#################

# Print a random sentence.


def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))


def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
            # This will stop the loop!


if __name__ == '__main__':
    main_loop()
