class Solution:    
	# @param A, a list of integer    
	# @return an integer    
	def singleNumber(self, A):
		single = 0
		for a in A:
			single ^= a
		return single 

if __name__ == "__main__":
	sol = Solution()
	print sol.singleNumber([1,2,9,3,2,1,9])
