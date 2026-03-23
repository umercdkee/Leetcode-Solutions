from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        l = len(words[0])
        max_count = len(words)

        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        words_set = set(words)

        for offset in range(l):
            left = offset
            count = 0
            word_lst_count = {}

            for j in range(offset, len(s) - l + 1, l):
                word = s[j:j+l]

                if word in words_set:
                    word_lst_count[word] = word_lst_count.get(word, 0) + 1
                    count += 1

                    while word_lst_count[word] > word_count[word]:
                        left_word = s[left:left+l]
                        word_lst_count[left_word] -= 1
                        left += l
                        count -= 1

                    if count == max_count:
                        indices.append(left)

                else:
                    word_lst_count.clear()
                    count = 0
                    left = j + l

        return indices