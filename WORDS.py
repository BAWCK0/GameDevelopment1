#Anagrams - same letters rearranged
'''Eg: listen, silent
Isogram: no reapeating letters
Eg: goblin

Pangram - have all the letters og English alphabets
Eg- The five boxing wizards jump quickly

Tautogram - string in which all the words begin with same letter
Eg- The tiger tried too tough.

Lion licks little locust

Abecedarian - strings in which letters appear in alphabetical order
Eg- almost'''

from tkinter import *

root = Tk()
root.title("Word Identifier for Goblins!")

Title = Label(root, font=("Arial", 30, "bold"), text="Word Identifier yay", bg="lightgrey")
Title.grid(row=1, column=1, columnspan=5, pady=5, padx=5)

Space_One = Label(root, text="")
Space_One.grid(row=2, column=1)

Anagram_Title = Label(root, text="Anagram C")
Anagram_Entry = Entry(root)
Anagram_CHECK = Button(root, text="CHECK", bg="lime")
Anagram_Results = Label(root, text="", bg="lightgrey", width=25)
Anagram_Title.grid(row=3, column=1)
Anagram_Entry.grid(row=4, column=1)
Anagram_CHECK.grid(row=4, column=2, padx=5)
Anagram_Results.grid(row=5, column=1, columnspan=2, pady=5)

Space_Two = Label(root, text="")
Space_Two.grid(row=6, column=1)

Isogram_Title = Label(root, text="Isogram C")
Isogram_Entry = Entry(root)
Isogram_CHECK = Button(root, text="CHECK", bg="lime")
Isogram_Results = Label(root, text="", bg="lightgrey", width=25)
Isogram_Title.grid(row=7, column=1)
Isogram_Entry.grid(row=8, column=1)
Isogram_CHECK.grid(row=8, column=2, padx=5)
Isogram_Results.grid(row=9, column=1, columnspan=2, pady=5)

Pangram_Title = Label(root, text="Pangram C")
Pangram_Entry = Entry(root)
Pangram_CHECK = Button(root, text="CHECK", bg="lime")
Pangram_Results = Label(root, text="", bg="lightgrey", width=25)
Pangram_Title.grid(row=5, column=4)
Pangram_Entry.grid(row=6, column=4)
Pangram_CHECK.grid(row=6, column=5, padx=5)
Pangram_Results.grid(row=7, column=4, columnspan=2, pady=5)



root.mainloop()