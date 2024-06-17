# Askme
Terminal-based flashcard application written in python.  
Flashcards are supposed to be written as .ask text files
which contain questions (each followed by line `--- question`)
and answers (each followed by line `--- answer`).  

To run `askme.py` you have to specify a file without the extension.  

Answers are counted as correct if similarity beween correct answer and given answer is at least 90%.
