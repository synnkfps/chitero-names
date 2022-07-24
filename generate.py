import random, time

suffixes = [".net", ".com", ".xyz", " client", ".cry", ".ware", "ware", ".aim", ".cheat", ".today", ".get", "hack", ".cc", ".lol", ".wtf", "mod", ".1337", "+", "++"]
letters = "abcdefghijklmnopqrstuvwxyz0123456789" 
no_numbers = "abcdefghijklmnopqrstuvwxyz" 


cipher = {"0":["he","zi"],"1":["ce","un"], "2":["li","du"],  "3":["asu","ti"],   "4":["toshi","qu"],    "5":["ve","ci"],     "6": ["zu","se"],      "7": ["ni","fu"],       "8":["ete","min"],        "9": ["imu","lo"],         "a":["ji","ka"],          "b":["ku","lu"],           "c":["de","nano"],            "d":["fo","su"],             "e":["le","ne"],              "f":["no","si"],               "g":["ke","es"],                "h":["fe","she"],                 "i":["cu","ir"],                  "j":["sha","are"],                   "k":["me","muni"],                    "l":["te","ca"],                     "m":["kun","ce"],                      "n":["to","ze"],                       "o":["shi","jo"],                        "p":["pu","ky"],                         "q":["mu","bo"],                          "r":["ful","shai"],                           "s":["ari","zai"],                            "t":["mun","on"],                             "u":["do","ice"],                              "v":["ru","han"],                               "w":["mei","xo"],                                "x":["ge","go"],                                 "y":["xi","wo"],                                  "z":["au","we"]}
obf_cipher = {}

# Not recommended, increases the execution time
high_randomization = False

randomization_threshold = 3

debugging = True

# Replace the strings
def to_ninja(string):
    out = []
    if high_randomization == False:
        [out.append(cipher[i][random.randint(0, 1)]) for i in string]
    else:
        for i in letters:
            obf_cipher[i] = [''.join(random.choice(no_numbers) for _ in range(2)), ''.join(random.choice(no_numbers) for _ in range(2))]
        [out.append(obf_cipher[i][random.randint(0, 1)]) for i in string]
    return ''.join(out)

# Main function
def generate_random(length, name):
    file = open(f'{name}.txt', 'w')
    start_file = time.time()
    names = []
    output = []

    # Generating the primary strings
    # Generator
    
    [names.append(''.join(random.sample(letters, randomization_threshold))) for i in range(length)]
    
    # Converting
    # Generator
    [file.write(to_ninja(j)+"\n") for j in list(set(names))]

    # Add each line of the created txt to output
    with open(f'{name}.txt', 'r') as file_output:
        while (line := file_output.readline().rstrip()):
            output.append(line)

    output = list(set(output))

    # Write all the lines with the content of output
    with open(f'{name}.txt', 'w') as final_write:
        for i in output:
            r_suffix = random.choice(suffixes)
            final = i + r_suffix
            
            if r_suffix == ' client':
                r_suffix = ' Client'
                final = i.capitalize() + r_suffix

            if random.randint(0, 1) == 1 and r_suffix == 'ware':
                r_suffix = 'Ware'
                final = i.capitalize() + r_suffix

            if random.randint(0, 1) == 1 and r_suffix == 'mod':
                r_suffix = 'Mod'
                final = i.capitalize() + r_suffix

            if random.randint(0, 1) == 1 and r_suffix == 'hack':
                aliases = random.randint(0, 2)
                aliases_2 = random.randint(0, 1)
                if aliases == 0: r_suffix = ' Hack'
                elif aliases == 1: r_suffix = 'Hack'
                elif aliases == 2: r_suffix = 'hack'
                
                if aliases_2 == 0: final = i.lower() + r_suffix
                elif aliases_2 == 1: final = i.capitalize() + r_suffix

            if random.randint(0, 1) == 1: final = i.capitalize() + r_suffix

            final_write.write(final + '\n')
        else:
            end = round(time.time() - start_file, 2)
            s = 'ms' if (end < 1.00) else 's'
            
            final_write.write(f"\n\n-> Generated with: SynnK's Generator™\n   Total names: {len(output)}\n  Time taken: {end-start_file}") # write watermark
            final_write.close()
            print(f'Finished writing {len(output)} lines of names. Took: {end}{s}')

generate_random(30000, "50K")