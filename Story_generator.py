
import random

when = ["During the boling hot summer",'She finally made it to her dream university','the moon was glistening  so bright','Thunder crackled the storm has begun', 'It was a cold night','The flowers blooming releasing a beautiful aroma','It was just like any other day']

who = ['Zoe','Brea','Isabella','Nadia','Emily ','Crystal','Celeste','Brianna ','Alice ','Ayla','Eliza ','Kate',]

setting = ['Country side','Busy City','New York',' Venice','Near the oceans','LA']

starter = [" finally decided to moved away from her hometown to achieve her ever long dream even if she was going get homesick", ' was surprised, weather like this never happened, there is something wrong she knew it', ' was frightned to near death']

middle  = ['She went into the forest to find the end to the eneasy feeling inside her head','she understood there was something very wrong with her new friend. They are not normal.','She stood there still, petrified, after seeing the shadow lurking behind her that has been following her.What should she do now? Is the end for her?']

ending = ['She decided to return to her home town and pretend whatever they were it was not going to harm her now',' She ran as fast a her tiny legs could take her but she kept on triping and then it got up to her. She at that momment knew she can not have a happy ending','She returned to her family and wailed on for hours on how she nearly escaped death','She somehow escaped for that wretchedness of a place. She is safe for now...']

print(random.choice(when) + ' , ' + random.choice(who)+' who lived in ', random.choice(setting)+' '+ random.choice(starter)+' ' + random.choice(middle)+' '+ random.choice(ending) )

