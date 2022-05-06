numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

powers = {
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
}

def parse_number(text: str) -> int:
    text = text.lower().split('!')[0]
    split_text = text.split()

    number = 0

    number_built_up = 0

    for word in split_text:
        if word in powers:
            # Get the previous number, multiply it by this power, and add it
            # to the total
            number += number_built_up * powers[word]
            number_built_up = 0
        elif word in numbers:
            # Add the number to the current buildup
            number_built_up += numbers[word]
        else:
            raise ValueError(f'Unknown word: {word}')

    number += number_built_up
    return number