if __name__=="__main__":
	n = int(input())
	words = []
	for _ in range(n):
		words.append(str(input()))
	words = sorted(list(set(words)))
	words.sort(key=lambda x:len(x))
	for _ in words:
		print(_)