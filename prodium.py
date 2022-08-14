import json
import whois

root_name = "nad"
max_name_length = 8
check_domain = True

vowels = ["a", "e", "i", "o", "u"]
spice = []

with open("spice.txt") as spicefile:
    for line in spicefile:
        spice.append(line.rstrip())

def is_vowel(letter):
    if letter in vowels:
        return True
    else:
        return False

def is_registered(name):
    try:
        registered = whois.whois(f"{name}.com")
    except:
        print(f"Domain registration check failed for {name}, assuming unregistered")
        registered = False

    if registered:
        return True
    else:
        return False

def process_endings(vowel_start=True):
    endings = []

    for word in spice:
        length = len(word)

        for cut in range(0, length):
            reduced = word[length - cut:]

            if vowel_start and reduced not in endings and reduced:
                if is_vowel(reduced[0]):
                    endings.append(reduced)

            elif reduced not in endings and reduced:
                endings.append(reduced)

    endings = sorted(endings, key=len)
    return endings


def join(root, endings):
    output = []
    for entry in endings:
        candidate = root + entry


        if len(candidate) < max_name_length:
            if check_domain:
                if not is_registered(candidate):
                    output.append(candidate)
            else:
                output.append(candidate)

    return output


root_end_vowel = not is_vowel(root_name[-1])
processed = process_endings(vowel_start=root_end_vowel)
joined = join(root=root_name, endings=processed)

with open(f"{root_name}.txt", "w") as output:
    json.dump(joined, output)
