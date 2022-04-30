#計算amazon留言平均長度

data = []
with open('reviews.txt', 'r') as f:
	for sentence in f:
		data.append(sentence.strip())
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為:', sum_len/len(data), '個字')

#i = 0
#file = []
#num = []
#total = 0
#while i <= 999999:
#	file.append(data[i])
#	num.append(len(file[i])) 
#	total = total + int(num[i])
#	i += 1
#average = total/1000000
#print(average)
