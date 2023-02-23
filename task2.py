#!python3
'''
##### Task 2
Take a string and make sure that it is a proper sentence, with only the first letter capitalized and the rest of the sentence in lower case. We will assume that the sentence never includes names that require capitalization.
(2 points)
'''

def properCaps(input):
    '''
    parameters:
    str input - string to fix capitalization for
    
    return
    str - proper capitalized string
    '''
    return
def format_sentence(sentence):
    
    sentence = sentence.lower()
    
    sentence = sentence.capitalize()
    
    if sentence[-1] not in ['.', '!', '?']:
        # If not, add a period at the end
        sentence += '.'
    return sentence

sentence = "this Is a sample Sentence that Needs formatting"
formatted_sentence = format_sentence(sentence)
print(formatted_sentence)

if __name__ == "__main__":
    sentence = "Carry On My Wayward Son!"
    assert format_sentence(sentence) == "Carry on my wayward son!"

    sentence = "I'm JuSt A LiTtle Black RainCLOUD!"
    assert format_sentence(sentence) == "I'm just a little black raincloud!"