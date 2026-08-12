#So ,we use the method count; when we want to check how many times a particular character or text 
#has been repeated.

#For example: You might be reading a article... any random article.

#You might want to check how many times a particular word or character arises in it.

#For example: Lets do this -> I'll copy a random article from BBC. Copy it ..--> then 
#we will find out how many times a particular word has been repeated.

text = """I got him before he got me. They tried twice. Well, I got him first 
That was President Donald Trump's observation, made to ABC correspondent Jonathan Karl,
in a phone conversation the day after he launched the US military campaign against Iran in February.
An Israeli airstrike, conducted with US approval and co-ordination, had just killed the Ayatollah Ali
 Khamenei and other top Iranian leaders  and Trump drew a direct line from that attack to threats and 
alleged plots the Iranians had made against him in previous years.
Trump has refrained from similar remarks in the ensuing six months of warfare,
but Defence Secretary Pete Hegseth has echoed the view.
Iran tried to kill President Trump, and President Trump got the last laugh,he said in 
March, noting that an unnamed Iranian who he said led an assassination unit had been killed in 
US strikes.These comments hint at the personal nature of this war  and the concerns by the president 
and his security team of the threat Iran still poses to his safety.
Those concerns were dramatically illustrated by this week's revelation that Trump secretly'
' switched to an alternate aircraft on his flight back from the Nato summit in Turkey '
'last month. He left the media and most of the White House staff to depart on the '
'presidential Air Force One 747 jet, which became, essentially, a decoy """

#Source :https://www.bbc.com/news/articles/cly8jexn1z9o

#ok now lets count how many times the word "Trump" has been used.

print(text.count("Trump"))

#And we get the output 6

#We can similarly also find how many times a alphabet , phrase has been used as well.