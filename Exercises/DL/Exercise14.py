def __str__(self):
    '''
    Display a string representation of the hand.
    '''
    output = ''
    hand_keys = self.hand.keys()
    hand_keys.sort()
    for letter in hand_keys:
        for j in range(self.hand[letter]):
            output += letter
    return output


# A more concise version of this code might be

def __str__(self):
    '''
    Display a string representation of the hand.
    '''
    output = ''
    for letter in sorted(self.hand.keys()):
        output += letter * self.hand[letter]
    return output


# Use whichever __str__ method you like. This will make sure the grading of the hand's display is consistent.


# Paste the entire Hand class in this box
class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0, len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def setDummyHand(self, handString):

        assert len(
            handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(
            len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1

    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):

        # Your code here
        word_letter_list = list(word)
        hand_letter_list = []
        for i in self.hand.keys():
            for j in range(self.hand[i]):
                hand_letter_list.append(i)

        def isValidWord(word):

            # TO DO ... <-- Remove this comment when you code this function
            output = self.hand.copy()
            letter_check = set(list(word)) <= set(output.keys())
            for letter in word:
                if letter in output.keys():
                    output[letter] -= 1

            value_check = all(i >= 0 for i in output.values())
            if letter_check == True and value_check == True:
                return True
            else:
                return False

        if isValidWord(word) == True:
            output = self.hand.copy()
            for letter in word_letter_list:
                if letter in output.keys():
                    output[letter] -= 1
            self.hand = {k: output[k] for k in output if output[k] != 0}
            return True
        else:
            return False