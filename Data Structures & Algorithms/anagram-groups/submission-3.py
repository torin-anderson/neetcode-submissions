class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for character in word:
                count[ord(character) - ord('a')] += 1
            output[tuple(count)].append(word)
        return [x for x in output.values()]