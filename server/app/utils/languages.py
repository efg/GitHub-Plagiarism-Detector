import json
import os

# Return a list of file extensions corresponding to the given language
def get_file_extensions(language):
    # Path to languages.json file
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    languages_file = 'app/resources/languages.json'
    
    # Load the json file as dictionary
    with open(os.path.join(file_dir, languages_file)) as file:
        languages = json.load(file)
    
    # If language is present return extensions corresponding to it else return extensions corresponding to 'C'
    if language in languages:
        return languages[language]
    
    return languages['c']



