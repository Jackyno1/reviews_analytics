data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀完了, 總共有', len(data), '筆資料')

wc = {} #wc 為 word_count
for d in data:
    words = d.split()
    for w in words:
        if w in wc:
            wc[w] += 1
        elif w not in wc:
            wc[w] = 1 #新增新的字進wc字典
for w in wc:
    if wc[w] > 1000:
        print(w, wc[w])

while True:
    w = input('請輸入要查詢字數的字:')
    if w == 'q':
        print('感謝您使用本查詢功能')
        break
    elif w not in wc:
        print('留言沒有這個字唷')
    else:
        print('你要查詢的字出現過', wc[w], '次')



