# please read this page carefully. https://pypi.org/project/jiwer/
# please follow the instructions on this page to make independent conda environment only for calculating WER

import jiwer

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