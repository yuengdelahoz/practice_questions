'''
Given a string, find the length of the longest substring without repeating characters.

'''
class Solution:
	def lengthOfLongestSubstring(self, s):
		print(s)
		# Fill this in.
		substring = {}
		max_length = 0
		cur_length = 0
		for i in range(len(s)):
			c = s[i]
			if c not in substring:
				substring[c] = 0
				cur_length += 1
			else:
				if cur_length > max_length:
					max_length = cur_length 
				cur_length = 0
				print("".join(list(substring.keys())))
				substring = {}
		return max_length

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
