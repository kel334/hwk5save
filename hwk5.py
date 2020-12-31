# Kendra Ludwig (kel334)


# Function 1: Select a field
def select_field(x, y):
    x = x.split(', ')
    y = int(y)
    try:
        y <= len(x)
        answer = x[y]
        return answer
    except IndexError:
        return None


# Function 2: Find all vowel indices
def find_vowel_indexes(x):
    vowels = []
    for i in range(len(x)):
        if x[i] in 'AaEeIiOoUuYy':
            vowels.append(i)
    if x[0] == 'Y' or x[0] == 'y':
        del vowels[0]
    return vowels


# Function 3: Finding the First Factor
def first_factor(x):
    for i in range(2, x+1):
        if (x % i) == 0:
            return i


# Function 4: Detecting Primes
def is_prime(x):
    if first_factor(x) == x:
        return True
    else:
        return False


# Function 5: Roman Numerals
def romanize(x):
    roman = {1: 'I',
             2: 'II',
             3: 'III',
             4: 'IV',
             5: 'V',
             6: 'VI',
             7: 'VII',
             8: 'VIII',
             9: 'IX',
             10: 'X',
             11: 'XI',
             12: 'XII',
             13: 'XIII',
             14: 'XIV',
             15: 'XV',
             16: 'XVI',
             17: 'XVII',
             18: 'XVIII',
             19: 'XIX',
             20: 'XX',
             21: 'XXI',
             22: 'XXII',
             23: 'XXIII',
             24: 'XXIV',
             25: 'XXV',
             26: 'XXVI',
             27: 'XXVII',
             28: 'XXVIII',
             29: 'XXIVX',
             30: 'XXX',
             31: 'XXXI',
             32: 'XXXII',
             33: 'XXXIII',
             34: 'XXXIV',
             35: 'XXXV',
             36: 'XXXVI',
             37: 'XXXVII',
             38: 'XXXVIII',
             39: 'XXXIX',
             40: 'XL',
             41: 'XLI',
             42: 'XLII',
             43: 'XLIII',
             44: 'XLIV',
             45: 'XLV',
             46: 'XLVI',
             47: 'XLVII',
             48: 'XLVIII',
             49: 'XLIX',
             50: 'L',
             51: 'LI',
             52: 'LII',
             53: 'LIII',
             54: 'LIV',
             55: 'LV',
             56: 'LVI',
             57: 'LVII',
             58: 'LVIII',
             59: 'LIX',
             60: 'LX',
             61: 'LXI',
             62: 'LXII',
             63: 'LXIII',
             64: 'LXIV',
             65: 'LXV',
             66: 'LXVI',
             67: 'LXVII',
             68: 'LXVIII',
             69: 'LXIX',
             70: 'LXX',
             71: 'LXXI',
             72: 'LXXII',
             73: 'LXXIII',
             74: 'LXXIV',
             75: 'LXXV',
             76: 'LXXVI',
             77: 'LXXVII',
             78: 'LXXVIII',
             79: 'LXXIX',
             80: 'LXXX',
             81: 'LXXXI',
             82: 'LXXXII',
             83: 'LXXXIII',
             84: 'LXXXIV',
             85: 'LXXXV',
             86: 'LXXXVI',
             87: 'LXXXVII',
             88: 'LXXXVIII',
             89: 'LXXXIX',
             90: 'XC',
             91: 'XCI',
             92: 'XCII',
             93: 'XCIII',
             94: 'XCIV',
             95: 'XCV',
             96: 'XCVI',
             97: 'XCVII',
             98: 'XCVIII',
             99: 'XCIX',
             100: 'C'
             }
    rom_num = roman[x]
    return rom_num
