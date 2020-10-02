from collections import Counter
a = 947
b = 891

print(f'{a}^2 + {b}^2 = {a**2 + b**2}')

#strings and lists
w1StartPos = 12
w1EndPos = 19

w2StartPos = 119
w2EndPos = 126

txtStr = "8BFYfhWhx54lButhacusxpBsmRaNX4CXLisM2EfGvXpdaqhaljRx5YjtQiuBwGutERkfeBOaPH2SOpIVwnSrrWrc4hvmx34VMleyNXLwyJogGgXjBjO7VGgnelsoniiwNZtzUCF7uFrCVGbjBxV99FUtXCWGFEf2YQGE3KoA."
print(f'{txtStr[w1StartPos:w1EndPos +1 ]} {txtStr[w2StartPos:w2EndPos +1 ]}')

#loops and conditions
#You can use a % 2 == 1 to test if a is odd.

startPos = 4912
endPos = 9195
result = 0
for i in range(startPos, endPos + 1):
     if i % 2 !=0:
         result += i
print(result)
#alt-one-liner
result = sum([i for i in range(startPos, endPos +1) if i % 2 !=0])
print(result)

#working with files:

ouputFile = []
with open('/home/kamonde/Desktop/python4bioinformatics/rosalind_problems/village/input.txt', 'r') as f:
    ouputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 !=0]
with open('/home/kamonde/Desktop/python4bioinformatics/rosalind_problems/village/out.txt', 'w') as f:
    f.write(''.join([line for line in ouputFile]))


#working with dictionaries:
txtStr2 = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
#approach1:
wordCountDict = {}
for word in txtStr2.split(' '):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

#approach2:
wordCountDict = Counter(txtStr2.split(' '))

for key, value in wordCountDict.items():
    print(key, value)

