"""
When it comes to data science project and we want to produce knowledge from tweets,
we have to remove first numbers, punctuactions and links that don't provide any useful meaning.
 Here comes the regular expressions.
 So, in this slide we will present the procedure which should be implemented.
"""



import  re

tweet = " Get ready for #PythonChallenge! Join us on 18/12 and 19/12 " \
    " for a weekend full of coding and debbuging, exploration and " \
    " inspiration and collaboration https://www.python.org/challenge"

print(f'Original tweet =  \"{tweet}\"')

# remove numbers
tweet1 = re.sub(r'\d+', "", tweet)

#remove links
tweet2 = re.sub(r'https\S', "", tweet1)
tweet3 = re.sub(r'www\S', "", tweet2)

#remove hashtags
tweet4 = re.sub(r'#[a-zA-Z0-9_]+', "", tweet3)

#remove panctuations
final_tweet = re.sub(r'[/!,.]', "", tweet4)

# Example's print
# print(final_tweet)

print(f'Cleaned tweet =  \"{final_tweet}\"')


"""
1. Removing numbers using the following pattern:  \d+

2. Now, we have to remove the link. As we can see the link contains the 
https and www characters. r"https\S+"  r"www\S+"

3. Next, we have to remove the hastag #PythonChallenge 
As we can see the pattern shoul match any character after #. 
So the pattern should be the following:

4. Finally, we should remove the punctuations, which are the following symbols: / , ! . 
So, the approptriate pattern is the following:  '[/!,]'
"""""