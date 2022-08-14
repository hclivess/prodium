import json

root_name = "prod"
max_name_length = 8

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
            output.append(candidate)
    return output


print(root_name[-1])
root_end_vowel = not is_vowel(root_name[-1])
print(root_end_vowel)

processed = process_endings(vowel_start=root_end_vowel)
joined = join(root=root_name, endings=processed)

with open(f"{root_name}.txt", "w") as output:
    json.dump(joined, output)
