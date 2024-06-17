# Please read this page carefully. https://pypi.org/project/jiwer/
# Please follow the instructions on this page to make independent conda environment only for calculating WER

import jiwer

# Input the reference text prompt and recognized text prompt
reference  = input("reference text prompt: ")
recognized = input("recognized text prompt: ")

# Create transformation function for the input text
transformation = jiwer.Compose([
    jiwer.ToLowerCase(),
    jiwer.RemoveMultipleSpaces(),
    jiwer.ExpandCommonEnglishContractions(),
    jiwer.RemovePunctuation(),
    jiwer.Strip(),
])

wer_value = jiwer.wer(transformation(reference), transformation(recognized))
print(wer_value)