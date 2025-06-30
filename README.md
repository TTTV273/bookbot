# BookBot

BookBot is a Python CLI tool that analyzes text files and generates detailed character frequency reports. This is my first [Boot.dev](https://www.boot.dev) project!

## Features

- **Word counting** - Total words in the document
- **Character frequency analysis** - Counts all alphabetical characters
- **Sorted output** - Characters ordered by frequency (most common first)
- **Beautiful formatting** - Professional-looking console reports
- **Flexible input** - Works with any text file

## Usage

```bash
python3 main.py <path_to_book>
```

**Examples:**
```bash
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

## Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============
```
