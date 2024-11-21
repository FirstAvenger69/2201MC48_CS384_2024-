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
        frequency_dict[key] = dict(frequency