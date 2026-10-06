#group all anagrams together into sublists
#order doesn't matter
#An easy way to find an anagram is to run collections.Count(word) and compare this hashmap to another word's.
#How we can solve this is by going through each word in strs. In each word we can then create a list of 26 0's where we 0 represent a different character. We cna then iterate through each char of the word and we can utilize ord(char) to find the spot in the array the current character represents. Once we finish going through the character we can add the 26 integer representation's tuple as the key for a hashmap and the value is the current word. This way wheenever two words have the same 26 integer representation we can just add onto the value fo rtha tkey in the hashmap.
#The time for this is O(n*m) where n is the lenth of stings, and m is the length of the longest string. This is because we have to go through each and every string and each character.
#The space for this is O(n) because we will be adding every value to the hashmap.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for string in strs:
            rep = [0] * 26
            for c in string:
                rep[ord(c) - ord('a')] += 1
            
            output[tuple(rep)].append(string)
        return list(output.values())
