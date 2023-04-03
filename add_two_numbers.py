'''
	You are given two linked-lists representing two non-negative integers.
	The digits are stored in reverse order and each of their nodes contain a single digit.
	Add the two numbers and return it as a linked list.

	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2, c = 0):
		# Fill this in.
		result = None
		ln = None
		while l1 is not None and l2 is not None:
			_sum = l1.val + l2.val + c
			tmp = _sum % 10
			if tmp != _sum:
				_sum = tmp
				c = 1
			else:
				c = 0
			# print(f"{l1.val} + {l2.val} = {_sum}, carry = {c}")

			if result is None:
				ln = ListNode(_sum)
				result = ln
			else:
				ln.next = ListNode(_sum)
				ln = ln.next

			l1 = l1.next
			l2 = l2.next
		
		remainder = l1
		if remainder is None:
			remainder = l2 

		while remainder is not None:
			_sum = remainder.val + c
			tmp = _sum % 10
			if tmp != _sum:
				_sum = tmp
			remainder = remainder.next
			ln.next = ListNode(_sum)
			ln = ln.next
			c = 0
		
		return result

def print_list(result):
	while result:
		print (result.val, end=" ")
		result = result.next
	print()

def create_Node(n):
	# last_n = n % 10
	# n = n//10
	head = ListNode(0)
	cur_node = head
	while n > 9:
		last_n = n % 10
		cur_node.val =  last_n
		cur_node.next = ListNode(0)
		cur_node = cur_node.next
		n = n//10
	cur_node.val =  n
	
	return head

n = create_Node(0)
print_list(n)
n = create_Node(1)
print_list(n)
n = create_Node(23)
print_list(n)
n = create_Node(234)
print_list(n)

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)


# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# print_list(l1)
# print("+")
# print_list(l2)
# result = Solution().addTwoNumbers(l1, l2)
# print_list(result)

# res = []
# while result is not None:
	# res.insert(0,result)
	# result = result.next

# for r in res:
	# print(r.val, end="")
# print()


