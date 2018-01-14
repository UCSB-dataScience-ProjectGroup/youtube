import pandas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

hit = 0
miss = 0
sizeList = 1100

def nullGen(n):
    return ([0] * n)

sentimentValue = nullGen(sizeList)
vs = nullGen(sizeList)
prediction = nullGen(sizeList)
analyzer = SentimentIntensityAnalyzer()
classified = pandas.read_csv('classifyCSV.csv')
comments = pandas.read_csv('comments.csv')
comments = comments.rename(columns={'' : '0','Video is crazy - but song sucks.': '1'})



def morph(value):
	if value > 0.5:
		return 1
	if value < 0.5:
		return -1
	else:
		return 0

for x in range(0,1095):
    vs[x] = analyzer.polarity_scores(comments['1'][x])
    sentimentValue[x] = vs[x]['compound']
    prediction[x] = morph(sentimentValue[x])
    if classified['1'][x] == prediction[x]:
        hit = hit + 1
    if classified['1'][x] != prediction[x]:
        miss = miss + 1
print (hit / (hit+miss))
    

