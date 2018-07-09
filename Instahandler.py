import os,random
memes = os.listdir('/Users/Kunbargi/Desktop/Memes')
random.shuffle(memes)
print(len(memes))
pic = memes[0]
os.rename('/Users/Kunbargi/Desktop/Memes/'+pic,
          '/Users/Kunbargi/Desktop/Used/{}.jpg'.format(str(len(memes))))
print(len(memes))
