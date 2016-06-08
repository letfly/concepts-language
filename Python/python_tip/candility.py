def solution(A):
	n = len(A)
	L = [-1] + A
	L.sort()
	count = 0
	pos = (n+1) // 2
	candidate = L[pos]
	for i in xrange(1, n+1):
		print i
		if (L[i]==candidate):
			count = count+1
	if (2*count > n):
		return candidate
	return -1
print solution([1,1,1,50,1])
