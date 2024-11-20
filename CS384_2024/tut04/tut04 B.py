from collections import defaultdict

def group_anagrams(words):

    anagram_dict = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)

    frequency_dict = {}
    for key, anagram_group in anagram_dict.items():
        frequency_count = defaultdict(int)
        for word in anagram_group:
            for char in word:
                frequency_count[char] += 1
        frequency_dict[key] = dict(frequency_count)

    max_freq_group = max(frequency_dict.items(), key=lambda x: sum(x[1].values()))

    return anagram_dict, max_freq_group

input_words = input("Enter words separated by commas: ").split(',')

input_words = [word.strip() for word in input_words]

anagram_dict, max_freq_group = group_anagrams(input_words)

print("\nAnagram Dictionary:")
for key, group in anagram_dict.items():
    print(f"'{key}': {group}")

print("\nGroup with the highest total character frequency:")
print(f"'{max_freq_group[0]}': {max_freq_group[1]}")