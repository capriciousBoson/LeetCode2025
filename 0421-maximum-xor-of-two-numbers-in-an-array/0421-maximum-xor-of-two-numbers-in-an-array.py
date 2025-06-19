class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_a_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        current = self.root

        for char in s:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
        current.is_end_of_a_word = True
    
    def findMaxXor(self, s):
        current = self.root
        max_xor = ""
        for char in s:
            max_bit = '0' if char=='1' else '1'
            if max_bit in current.children:
                max_xor += max_bit
                current= current.children[max_bit]
            else:
                max_xor += char
                current = current.children[char]
        return max_xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        t = Trie()

        binary_nums = [bin(n)[2:].zfill(32) for n in nums]
        for s in binary_nums:
            t.insert(s)
        
        max_xor_val = -float('inf')
        for i in range(len(nums)):
            max_xor_str = t.findMaxXor(binary_nums[i])
            current_max_xor = int(max_xor_str, 2)^nums[i]
            max_xor_val = max(max_xor_val, current_max_xor)

            # print(f"for string {s} max xor string : {max_xor_str,': ',int(max_xor_str, 2) } current xor  : {current_max_xor max : {max_xor_val}")

        return max_xor_val

        