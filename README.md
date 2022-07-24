### chitero names generator
#### (free version)

I've been looking on github darkest layers and I've saw some weird "1M names txt" repositories, and it was obviously automatically generated. <br>
So I decided to make my own generator, that doesn't uses "random" strings, the premium version has tons of more features and it's way faster, but the free version still pretty good.

### how to use
you need to create a folder on your desktop/downloads/documents folder, or just drag n' drop it on those. <br.
1. make sure you have opened the terminal on the location of the file, as the free version doesn't finds itself.
2. once you opened the terminal on the right location, do `python generate.py`
3. to choose the amount of names that you want to create and the name of the file, change the variables `generate_amount` and `generate_name`.

**note: i don't recommend generating high amount of names, see why in the next topic**

### features
- [X] pre-setted cipher
- [X] randomic cipher
- [X] suffixes
- [X] double buffered anti-duplicated names
- [X] specific suffixes fixes
- [X] random capitalization
- [ ] self find
- [ ] general optimizations

### functions
`pre-setted cipher`: a cipher that it already made by default, you can change it but i don't recommend that much... <br>
`randomic cipher`: generates a cipher before the names gets converted. **not recommended to use, can make the generate task slower** <br>
`suffixes`: suffixes made by me, i dont know if there are more to add. <br>
`double buffered anti-dupes`: prevents the generator from creating duplicated names, making all of them uniques. <br>
`specific suffixes fixes`: fixes text when specific randomized suffixes are generated, for example: `'client'`. *(its so ugly when not capitalized)* <br>
`random capitalization`: adds a 50% chance of the current generated combination be capitalized. <br>
`self find`: finds itself so you dont need to open the terminal on the file location. *(premium feature)* <br>
`general optimizations`: overhaul rewritted functions to make name generation up to 60% faster. *(premium feature)* **0,64ms generating 700.000 names**

### important
a really important setting is the `randomization_threshold` setting, it basically holds how much strings are you going to create, how much possible combinations you want to create, and how much bigger the output can be. <br>
**Values higher than 3 (4 to 6):** generates higher output amounts, meaning that if you generate 50.000, it will generate around 42-44K. but generates bigger names, which for me looks ugly. <br>
**Values lower than 3 (2 to 1 (why)):** generates a very small output amount, meaning that if you generate 50.000, it will generate around 6-15k, but the generated names are very good, in my opinion. also the output time is really fast, like under 70ms

another setting: `obf_cipher`, its a cipher that generates itself, using the same 'template' as the main one, but... as it needs to generate 2 values and iterate on each value of our alphabet and digits, it increases the output time by more than 14 seconds. which is not good at all.

***made entirely from scratch by me***
