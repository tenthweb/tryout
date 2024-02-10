class Sentence:
    def __init__(self, contents, truth_value='unknown'):
        self.contents = contents
        self.truth_value = truth_value

men_are_mortal = Sentence('All men are mortal', 'true')

print(men_are_mortal.truth_value)

lst =[[['all','men','are','mortal'],['and']]]
