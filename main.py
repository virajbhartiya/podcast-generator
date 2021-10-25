from urllib import request
from bs4 import BeautifulSoup
import os
from gtts import gTTS

def makeSoup(url):
    try:
      page = request.urlopen(url)
      soup = BeautifulSoup(page)
      return soup
    except:
      pass

def getSubReddit(body):
  return body.find_all("div", {"class":"_11R7M_VOgKO1RJyRSRErT3"})

def getTitles(data):
  titles = []
  for subreddits in data:
    result =  subreddits.find_all("h3", {"class":"_eYtD2XCVieq6emjKBH3m"})[0].get_text()
    titles.append(result)
  return titles

def getParas(data):
  paras = []
  for subreddit in data:
    paras.append(subreddit.find_all("div", {"class":"_292iotee39Lmt0MkQZ2hPV"})[0].get_text())
  
  return paras

def generateAudio(title, para):
  text = para
  language = 'en'
  gttObj = gTTS(text=text, lang=language, slow=False)
  gttObj.save(title+'.mp3')


body = makeSoup('https://www.reddit.com/r/confessions/top/')
subReddit = getSubReddit(body)
titles = getTitles(subReddit)
paras = getParas(subReddit)
print(paras)
for i in range(0, len(titles)):
  generateAudio(titles[i], paras[i])
