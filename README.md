# AHS64: Anti‑Hash Standard 64

> You’ve heard of SHA256. You've heard of num2words. Now get ready for SHA“whatinthehellisthismethod.”
> (Also called AHS64 or words2num)

## Overview
AHS64 is a revolutionary anti‑hash algorithm that converts words into absurdly huge numbers.  
Instead of compressing data, it inflates it into integers so massive they make cosmologists uncomfortable.

## Features
- Deterministic: same input → same absurdly huge number  
- Reversible: you can get your text back  
- Astronomical scale: even a short sentence becomes enormous  
- Looks like magic, but it’s just base conversion  

## Usage
Note: do not do this at home as "words2num" or "AHS64" doesn't exist (or at least not in my understanding) on PyPI
Instead, just run the included Python script directly:
```bash
python words2num.py "Hello, world!"
```
Which outputs 91773068209181679254210355806736.
Or, if you're inside Python:
```python
>>> from words2num import words2num #remember the note?
>>> words2num("Hello, world!")
91773068209181679254210355806736
>>> words2num("Please don't turn me into a number D:")
639942983767050993241300677095348160276790952976154343966310455055426182129226934053520288
```

## Warning
- not suitable for small integers
- May cause existensial dread
- Collisions irrelevant—no one can store the output anyway
- If you use this in an ARG, add five empty lines and then a "p" in the desc, just to confuse people even more
- The previous one was completely just a troll, but if you somehow commit to the bit, I guess... Thanks?
- 9 out of 10 doctors DON'T recommend this. Turns out one of them is psychotic.
- Do NOT import the actual `num2words` package from PyPI alongside this one. Unless you enjoy watching namespaces fight to the death.
- The name "AHS64" actually is used by some other people with other meanings, but this one, just... Scroll up to the top. Basic coincidences really.

Fun fact: The real `num2words` package converts numbers into words.
This fake `num2words` converts absurdly huge numbers back into words.
Together, they form a cursed yin-yang of Python APIs.

## License
This project is licensed under the Unlicense.  
Translation: anyone can use it, for anything, without restrictions.
