#計算amazon留言平均長度

data = []
with open('reviews.txt', 'r') as f:
	for sentence in f:
		data.append(sentence)
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

#----------------------
#要找留言小於100字的
small = 0
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100個字')
#	while len(d) < 100:
#		small += 1
#print(small)
#-----------------------
#找到留言中有"good"這個字的留言
count = 0
for d in data:
	if 'good' in d:
		count += 1
print('留言中有"good"這個字的數量有', count, '個')
#-----------------------
#快寫法
good = [d for d in data if 'good' in d]
print(len(good))
