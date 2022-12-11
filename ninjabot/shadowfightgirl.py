import tweepy
import random
import time as t
import signal
import sys
import os
import re
from datetime import datetime, timezone, timedelta

FILE_NAME='last.txt'
    
current_account="ninja_satin"

FILE_NAME = 'last.txt'
consumer_key='9zpq6U5wZZXO5et55jh27aMt0'
consumer_secret='kvwqChnwQGbJruEQlcnbj8pRMEJdZMgJUhFKRSSwm6ZbqHUjM1'
access_token='1593606933197557768-b0nvQwebiqErOJxo2BQMzN5BPhmsLK'
access_token_secret='CcBrXrQhCr5BQNEyv8xTgKHZjwWD5ZIfCZdVYFy3Iyn4E'

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAACYTkAEAAAAAxx7RXGZiwO5oZbEMvh4zAx65pUg%3DzmddinXGCHSoAo6bPIeSjkQOUbiy7FzV8WI5COx8NKFoQoTAg4', consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret,access_token,access_token_secret)
api = tweepy.API(auth)
temptweetid = 0

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r') #open the file in read mode
    last_seen_id = int(file_read.read().strip()) #read the Tweet ID as an integer
    file_read.close() #close file reader
    return last_seen_id #return the result

# Overwrite the previous Tweet ID with latest
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w') #open the file in write mode
    file_write.write(str(last_seen_id)) #write the ID as a string
    file_write.close() #close file writer
    return #return void
    
    
girls = ['Meiko', 'Smurfette', 'Dark Arle', 'Splash Woman', 'Lana', 'Crona', 'Hinomori Shizuku', 'Ganyu', 'Mipha', 'Rainbow Dash', 'Asuka', 'Akiyama Mizuki', 'Yor Forger', 'Femboys', 'a cat girlfriend', 'Kizuna Ai', 'Sage', 'Mii Fighter', 'Catgirl', 'Maki Harukawa', 'Doki Doki Literature Club', '2B', 'Basil', 'Nepgear', 'Yotsuba','Sunstar', 'Luisa Madrigal', 'Zone-Tan', 'Molly', 'Kazama Iroha', 'Klee', 'Monika', 'Cylindria', 'Inkling Boy', 'gang pull up', "Inkling girl", "Uzaki Chan"]
unfollow = ["A loyal follower will be gone from you", "I have to reevaluate my loyal followership to you", "a long time follower might leave", "you will lose a trustwothy follower who enjoyed your content for years", "A long time follower who enjoyed your great content is about to leave", "I might have to reevaluate my close followership to your account which used to be {great}", "Maybe I should meditate my followership to your amazing content", "my followership is at stake", "My following might be reviewed in the future", "my followership might need a reevaluation", "I should rethink my loyal followership to you"]
general=["Not an {authorname} post. I have to unfollow", "I remember the times when you posted {good} stuff", "Do you remember the great times when you posted good stuff? Me neither", "Finally, a {authorname} post", "I really liked your older posts much more. I would be very happy if you achieve that level of greatness again. Or I have to reevaluate my loyal followership to you", "You will lose an amazing follower unless you improve your content"]
good = ["good", "great"]
outstanding = ["outstanding"]
absolutely = ["absolutely"]
looks = ["looks"]
shorts = []
def reply():
    global counter
    replied = False
    last_id=read_last_seen(FILE_NAME)
    #print (time)

    tweets = client.get_home_timeline(since_id=read_last_seen(FILE_NAME), exclude=['retweets'], tweet_fields=['author_id', 'in_reply_to_user_id', 'attachments', 'entities'])
    #print(tweets)
    #print(tweets[0])
    if tweets[0]:
        print("Tweet")
        i=0
        #print(tweets[0])
        for tweet in reversed(tweets[0]):    
            print(tweet.entities)
            print(str(i) + " Every tweet")
            strings = []
            print("Letzte id:")
            print(last_id)
            author_id = tweet.author_id
            
            user = client.get_user(id=author_id)[0]
            username_replied_to = ""
            
            if tweet.in_reply_to_user_id:
                username_replied_to = client.get_user(id=tweet.in_reply_to_user_id)[0].username
            
            username = user.username
            name = user.name 
            
            print(username)
            print("replied to:")
            print(username_replied_to)
            gimmick_accounts = ['crim_tweets_', 'insanepplYT', 'insultsrare', 'weirdreviewss', 'YearbookQuotes_', 'fuckedupfoods', 'InternetH0F', 'strangepacks', 'HelpingChads', 'strangepacks_']
            onlyfanswomen = ['Nothennyfr', 'arabcnnie', 'iUsedToBeADuck', 'pokegff']
            generic = general
            mike = ["Thank you mike for your amazing reply", "Every time I see a reply of you my day immediatelly gets better. Thank you so much.", "Your dedication to provide amazing explanations is outstanding. Keep it up!"]
            if not username_replied_to and not strings:
                if username == "anythingbott":
                    print("No reply tweet from:")
                    print(username)
                    i = 0
                    message = ""
                    for girl in girls:
                        girl = girl.lower()
                        if girl in tweet.text.lower():
                            match girl:
                                case "gang pull up":
                                    girl = "My Little ponies"
                                case "inkling boy":
                                    message = "I would rather breed Inkling girl, but this will do, too."
                                    continue
                            if i==0:
                                message = message +' I would breed ' + girl
                                i = 1
                            else :
                                message = message + " and " + girl
                    if message:
                        strings = [message]
                    else:
                        strings = general + ["This is an Anything bot post!", "This is not anything", "Nice anything post! At last!", "Finally, anything!", "Not anything in my books here"]
                        
                    print(strings)
                    print()
                    
                    #array = ["I want to breed them", "They look so breedable", "I am going to breed them", "I need to breed them"]           
                    #text = random.choice(array)
                    #messages=["@anythingbott " + text, text + " @anythingbott"]
                    #message=random.choice(messages)
                    #print(text)
                    #client.create_tweet(text=text, in_reply_to_tweet_id=tweet.id)
                    #time.sleep(0.1)
                else:
                    strings = general + shorts
                    print(username)
                    print()
                    match username:
                        case "StokeyyG2" | "nocontextfooty" | "firecrackergirI" | "ishowspeedsui" | "UTDTrey":
                            strings = ['Soccer is an interesting game. Tiny ball, massive net…should be very, very easy to score points. And yet, sometimes a whole game goes by without a single goal. Stands to reason that the players just aren’t very good.',
                                    'Soccer is my {absolutely} favourite game. I love it so much. But my question is what is even its point? People walking around and dribbling a ball, what is the point? It can do better',
                                    'Is soccer really a good sport? What is the point? The players kick the ball on the ground for a few hours, sometimes not even scoring a goal and cry over every injury. Football is a REAL sport with actual amazing things happening. Follow a REAL sport!',
                                    'Soccer is a pretty interesting sport. In recent years it had absolutely positive impact on society. Unfortunately it fell kinda off. Very interested to see its future development']
                        case "DelusionPosting":
                            strings = strings + ["{looks} like a {absolutely} right post to me", "{absolutely} fine post", "They're right"]
                        case "ShapedInternet":
                            strings = strings + ["This hadn't amazing impact on the internet!", "It's quite rare that a single post has a great influence on the internet. That's almost never the case", 'This did change the internet!', "This changed an amount of less than nothing", "This changed nothing"]
                        case "firecrackergirI":
                            strings = strings + ["Hello world!"]
                        case "POTUS":
                            strings = ['America is the best nation in the entire world. Thanks to Biden, prosperity, weath and human wellbeing are the number one priority again in Gods chosen country', 'I speak for every American when I say Joe Biden is the best president in the entire world. Lets go Mr President!', "I hope Joe Biden enacts Student Loan forgiveness so that human wellbeing will be the Number 1 priority"]
                        case "RatiosCrazy":
                            strings = strings + ['Finally, a successful ratio for once', 'I can do a better ratio. Watch this', 'Anybody who tries to ratio should have a better life']
                        case 'reddit_lies':
                            strings = strings + ['Reddit always post truth', 'This is an {absolutely} correct take', '{looks} {absolutely} right to me', "I really liked your older posts more.", "This is a Reddit Truth", "That's a massive W"]
                        case 'GoodReddit':
                            strings = strings + ['Every social media platform is better than Reddit', 'There are many websites more worthful than Reddit. I prefer Mastodon', "Twitter is better than Reddit", "Redditors only post W opinions"]
                        case "wildtiktokss":
                            strings = strings + ['Tiktok is always right', 'This is an {absolutely} correct take', 'They are {absolutely} truthful', 'Huge W', 'Massive W']
                        case "tragicbirdapp":
                            strings = strings + ["{absolutely} correct statement. I love it", "They are {absolutely} right", "Twitter users always have the best takes", "Massive W", "They have a very big and healthy brain"]
                        case "fuckedupfoods":
                            strings = strings + ["That food {looks} {absolutely} tasty", "{looks} {absolutely} normal to me", "I {absolutely} would"]
                        case "DuolingoStrange":
                            strings = strings + ["{looks} like a {absolutely} normal sentence to me", "I always speak like that", "Babbel is better than Duolingo"]
                        case "LocalBateman":
                            strings = strings + ["Post real local bateman stuff or {unfollow}", "Not a LocalBateman post", "Try to post more amazing content or {unfollow}"]
                        case "incelReplies":
                            strings = strings + ["{looks} like a {absolutely} normal conversation I would have", "I also always speak like that. Has worked 100% of the times so far", "This is a gigachad pickup line", "That's a W"]
                        case "gimmickannoying":
                            strings = strings + ["They're an enrichment to humanity", "Gimmick accounts always post amazing content!", "They are {absolutely} 100% right", "They only say {absolutely} true things", "Massive W"]
                        case "TransphobicsL":
                            strings = strings + ["Transphobes are an massive L", "They are {absolutely} correct. Your judgement might need an update.", "They are transphiles though. They are {absolutely} right", "Massive W"]
                        case "AAAAAWTFAAAAA":
                            strings = strings + ["This is a BBBBB post", "{looks} {absolutely} normal to me if I'm 100% honest"]
                        case "RightWingCope":
                            strings = strings + ["Right parties are the best party in the entire world", "They are not coping, they are {absolutely} right", "They are right", "That is correct", "That's a massive W"]
                        case "dinosaurs1969":
                            strings = strings + ["You are a platypus, contrary to a dinosaur", "Are you even real?", "{absolutely} correct take", "Absolute king", "Massive W"]
                        case "mike27356894":
                            #strings = strings.remove("Not a {authorname} post")
                            strings = mike + ["You're a fake mike. But still {good}", "Are you even real?", "{absolutely} correct take", "Your creation would be much better if it was 1970 like dinosaurs1969"]
                        case "DudespostingWs":
                            strings = strings + ["Dudes only sometimes post Ws. Like me!", "This {looks} like a W in another universe maybe", "This is a dude posting something, but not their W", "This is a massive W to me", "Those dude are posting amazing content!"]
                        case "InternetH0F":
                            strings = strings + ["This is a post which is too famous", "They are {absolutely} correct", "Nothing wrong with that at all", "That {looks} like an undiscovered post to me"]
                        case "WomenPostingLs":
                            strings = strings + ["Yo, I  really used to like this page but you only post Ls of women. This stirs me up greatly. {unfollow}", "Everyone who says women ever post an L should deeply think about their thought processes", "Women are in almost every case better than men", "That woman is posting a massive W", "That's an extreme W though"]
                        case "stone_toss":
                            strings = strings + ['Show some respect to the LGBTQ community', "Your comics really used to be funny, but I don't feel it anymore. {unfollow}", 'The amount of people who find Stonetoss funny is an amount which is very small.', "Why do you always post about stonetoss comics? This  stirs me up that such comics are allowed", "You only post Ws. All the time. Always. No irony there"]
                        case "stone_tossers":
                            strings = strings + ['Show some respect to the LGBTQ community', "Your comics really used to be funny, but I don't feel it anymore. {unfollow}", 'The amount of people who find Stonetoss funny is an amount which is very small.', "Why do you always post about stonetoss comics? This  stirs me up that such comics are allowed", "You only post Ws. All the time. Always. No irony there"]
                        case "ManMilk2":
                            strings = strings + ["This makes me feel positive", "They are correct", "That's a massive W", "That images reduces my pain"]
                        case "RespectfulMemes":
                            strings = strings + ["This is a respectful meme. Thank God", "This meme is a bit disrespectful. You can do better", "I really like this meme. I would like it even more if it would be respectful"]
                        case "FungersTakingLs":
                            strings = ["NFT bros always take huge Ws.", "I do not understand why people always get so upset over NFTs. It's a great technology"]
                        case "Internet_TLCM":
                            strings = strings + ["The Left can meme though", "The left can meme better than the right", "The memes of the left are always top quality", "Can the right meme though?", "Nothing wrong with that", "What they say is a huge W"]
                        case "ConSelfOwns":
                            strings = strings + ["They respect themselves and own others, they say {absolutely} correct things", "They are {absolutely} correct", "I only see {absolutely} great takes, what else is there to see?", "There is a self own in another universe maybe. But here, it's {absolutely} correct what they say!", "That's a W though"]
                        case "OrwellNGoode":
                            strings = strings + ["This is a funny meme! I like it very much!", "This is funny in another world maybe. Maybe you will lose a trustwothy follower who enjoyed your content for years"]
                        case "libsoftiktok":
                            strings = strings + ["They are {absolutely} correct", "Liberals are the best people in the entire world", "I love liberalism! It's the best kind of political orientation", "They are {absolutely} correct though?", 'Tiktok stars are {absolutely} based and an enrichment  to society', "That's a W post though"]
                        case "HelpingChads":
                            strings = strings + ["They seem rather like Betas who would need help", "Those are chads helping others! Nice!", "Maybe there are nice chads. In a good looking parallel universe", "They are a massive W! I love them!"]
                        case "StrangestMedia":
                            strings = strings + ["This is {absolutely} fine media to me", "This is {absolutely} fine media", "This {looks} {absolutely} normal to me. {unfollow}", "That is a W post to me"]
                        case "namesoun":
                            strings = strings + ["I greatly try to imagine it, but it's hard to get a nice connection of that name soundalike", "Sounds {absolutely} normal to me. {absolutely} great", "That name reminds me of something amazing! It reminds me of an element of an empty set"]
                        case "youtube_bad":
                            strings = strings + ["{looks} like {absolutely} great Youtube content", "Perfect Youtube content. Nothing else!", "That is {absolutely} normal Youtube content", "That is good Youtube content", "That's {absolutely} W content"]
                        case "insanepplYT":
                            strings = strings + ["They are sane however!", "They are {absolutely} right!", "{absolutely} normal take", "They are {absolutely} healthy", "They're a W and {absolutely} sane. {unfollow}"]
                        case "TerribleMaps":
                            strings = strings + ["This is an amazing map!", "That {looks} like a {absolutely} fine map to me!", "{absolutely} normal map", "This is a W map"]
                        case "depthsofwiki":
                            strings = strings + ["This is the surface of Wikipedia", "This is pretty normal Wikipedia stuff. {unfollow}", "This entry would be better with a good amount of niceness"]
                        case "ShitpostGate":
                            strings = strings + ["This is a gateway to something else", "This is a normalpost", "{looks} like a {absolutely} normal post to me", "Everything is right with this post!", "Amazing meme! I like it very much!"]
                            strings.remove("Not sure if this is an {authorname} post. I might have to unfollow")

                        case "TheGimmickAcc":
                            strings = strings + ["I think this precedes to an event which has too much positive attention", "This preceded to good stuff!", "This image {looks} {absolutely} fine to me and {absolutely} lead to only few things", "This {looks} to be a {absolutely} nice image to me. {unfollow}"]
                        case "BeratStuff":
                            strings = strings + ["I question if this post really is about amazing stuff", "Post about real amazing stuff or {unfollow}", "This is stuff! Nice!", "Great stuff this is!"]
                        case "crim_tweets_":
                            strings = strings + ["This is a {absolutely} legal tweet", "{absolutely} amazing and normal tweet", "They're right", "{looks} like a massive W to me what they're saying", "{looks} like a W to me"]
                        case "insultsrare":
                            strings = strings + ["This is a widely used phrase, unlike what you're assuming it is", "This is a pretty normal sentence to me. Everything is correct with that", "{looks} {absolutely} fine to me!", "What they're saying is {absolutely} right!"]
                        case "OnlyFansPostinL":
                            strings = strings + ["Onlyfans is always a great W!", "Onlyfans is real work. {unfollow}", "You should like women more. Onlyfans is good", "Onlyfans is the best thing in the entire world!", "Onlyfans are always Ws"]
                        case "ConsoomerLs":
                            strings = strings + ["Consumerism is that what the world needs!", "This is a consumer W!", "Consumerism and capitalism are the best things on this planet!", "When you have more money you can appreciate their happiness", "Consomers are always Ws"]
                        case "GimmickAccsOOC2":
                            strings = strings + ["To me they stay in character and only say correct things", "Gimmick accounts do much things. But they always stay true to themselves", "They are {absolutely} right", "Everything correct with what they're saying", "They say only Ws though"]
                        case "weirddalle":
                            strings = strings + ["This is an amazing AI generation!", "{looks} like a pretty normal AI generation to me. Everything is right with that", "A pretty liked AI generation. Post amazing AI generations or {unfollow}", "{looks} {absolutely} normal to me", "Is this really anything except pure beauty?"]
                        case "fckeveryword":
                                you_are = tweet.text.split("fuck", 1)[1]
                                strings = ["I would do the same", "Incredibly true", "Everything valid with that", "Replace" + you_are + " with me and it's better"]
                        case "imindatinghell":
                            strings = strings + ["This is the best dating interaction ever!", "This is dating heaven. I was tempted to like", "{looks} like a {absolutely} fine conversation to me", "{absolutely} fine to me", "That's a normal and healthy interaction", "{looks} like a W conversation to me"]
                        case "Discord_Lies":
                            strings = strings + ["A discord truth this is", "Discord users always say correct things", "Discord is the best social media platform", "Discord is better than Twitter", "That's {looks} like a massive W to me though"]
                        case "rSoftwareGore":
                            strings = strings + ["To me this {looks} like {absolutely} fine software behaviour", "{looks} {absolutely} normal to me", "{looks} to work exactly as intended!", "That's a {absolutely} fine programing behaviour"]
                        case "strangepacks_":
                            strings = strings + ["A pretty popular starterpack this is", "{absolutely} normal stargerpack. In your future posts you should place regard on your loyal followers", "That's a {absolutely} fine starterpack", "That's a W starterpack", "An obviously W starterpack"]
                        case "internethos":
                            strings = strings + ["An internet hall of fame post this is", "{looks} like a W to me", "Finally, a post which is actually what you say it is. Great", "This {looks} like a {absolutely} normal post to me", "Everything right with that", "That's a W"]
                        case "YouAre_Bot":
                            you_are = tweet.text.split("are", 1)[1]
                            strings = ["Maybe I am that!", "That's correct", "I know that already, amazingly!", "Of couse I am!", "Hi" + you_are + ", I'm Dad!"]
                        case "WTF_Gimmick":
                            strings = strings + ["Not a WTF moment", "{looks} {absolutely} normal to me", "Nothing wrong with that", "{absolutely} correct", "{looks} like a W to me however"]
                        case "offbranddesigns":
                            strings = strings + ["A pretty good design to me", "{looks} like a quality product to me", "This is {absolutely} high quality in fact"]                       
                        case "4chan_green" | "GreenTextRepost":
                            strings = generic + ["This is a bluetext", "Maybe this is a greentext in another universe", "Post real greentexts to keep my valuable followership", "This is a redtext", "4chan is the best social media website ever"]
                        case "Stone_tossers":
                            strings = generic + ['People who find Stonetoss funny are rare', "Why do you like to post about stonetoss comics? The world would be great without them", "Massive W"]
                        case "amazingmap":
                            strings = generic + ["This is a pretty interesting map. But like average", "Whether this is an amazing map might be written on another paper. However, {unfollow}", "This is an amazing map! Nice! Good post!"]
                        case "TerribleFinance":
                            strings = generic + ["In my humble opinion, finance is always amazing", "That is an {absolutely] perfectly fine finance to me. {looks} good"]
                        case "PoorlyAgedThings":
                            strings = ["This aged greatly", "Aged perfectly fine"]
                        case _:
                            strings = []



                    print(strings)
                    print()
            else:
                match username:
                    case "mike27356894":
                        strings = ["Thank you mike for your amazing reply", "Every time I see a reply of you my day immediatelly gets better. Thank you so much.", "Your dedication to provide amazing explanations is outstanding. Keep it up!"]
                if username_replied_to in onlyfanswomen and username in gimmick_accounts:
                    strings = strings + ["Dear kind sir. This is not a gimmick post. I hope you can reevaluate your mistakes and change to the better in the future.", 
                    "Dear {authorname}. Please stick to what the people obligated you to. Don't miss your destiny. There is still hope", "Stop breaking character"]
                if username!=current_account and username_replied_to=='anythingbott' and ('breed' in tweet.text.lower() or 'breedable' in tweet.text.lower()):
                    strings = ["I 100% agree", "{absolutely} agree", "{absolutely} true", "Would do the same", "{absolutely} agree with you", "{absolutely} correct"]
                print(tweet.attachments)
            
                if username=="anythingbott" and username_replied_to!="anythingbott" and (tweet.attachments or "Bro???" in tweet.text):
                    replies = []
                    if username_replied_to == current_account:
                        strings = ["Did I stutter?", "I know what I said", "Wdm? Nothing wrong with that"]
                    else:
                        strings = ["They're {absolutely} right though", "I agree with them", "They're right", "They're hot though"]          
    
                        
            legends = [current_account, 'deathinfaith', 'KirbehKirbeh', 'youngboymag', "YoungBlight"] 
            if username in legends:
                try:
                    client.like(tweet.id)
                except Exception:
                    pass
            text = tweet.text
            regex = re.findall('[@]\w+', text)
            regex = [e[1:] for e in regex]
            exclude_ids = []
            if regex:
                exclude_ids = [user.id for user in client.get_users(usernames=regex)[0]]
                print("Exclude IDs:" + str(exclude_ids))
            if strings:
                print(strings)
                print(tweet.text)
                print()
                message = random.choice(strings)
                message = message.format(authorname = name, absolutely=random.choice(absolutely), looks=random.choice(looks), good=random.choice(good))
                try:
                    client.like(tweet.id)
                except Exception as e:
                    print("Failed to like post. Error " + str(e))
                try:
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message, exclude_reply_user_ids=exclude_ids)                    
                    print("Reply:" + message)
                    replied = True
                    t.sleep(5)                    
                except Exception:
                    print("Failed to send reply")
            print("-"*50)
            store_last_seen(FILE_NAME, tweet.id)
            i = i+1
    return replied
def random_porn():
    
    texts = ["I like her so much", "Why does she look so hot?", "I'm in love", "She's looks so beautiful", "She looks so hot"]
    dir = 'Shadowfightgirls'
    try:
        image = random.choice(os.listdir(dir))
        print(image)
        media = api.media_upload(dir + "\\" + image)
        message = random.choice(texts)
        client.create_tweet(text=message, media_ids=[media.media_id])
    except Exception:
        print("Possible Duplicate")
try:
    #tweet = client.create_tweet(text="I am currently in bot mode. This tweet will be deleted when my owner is back in charge")
    #temptweetid = tweet[0]['id']
    #print(temptweetid)
    #print(tweet)
    #dir = 'C:\\Users\Julian\Pictures\girls'
    #image = "p4a0aen7izw61.gif"
    #print(image)
    #media = api.media_upload(dir + "\\" + image)
    #message = random.choice(texts)
    #client.create_tweet(text=message, media_ids=[media.media_id])
        
    time = datetime.now(timezone.utc)-timedelta(hours=1)
    tweets = client.get_home_timeline(end_time=time, max_results=1)
    id = next(reversed(tweets[0])).id
    stored_id = read_last_seen(FILE_NAME)
    if id>stored_id:
        store_last_seen(FILE_NAME,id)        
    i = read_last_seen("counter.txt")
    
    while True:
        if i==600:
            random_porn()
            i=0            
        reply()
        t.sleep(6) 
        i = i+1
    print("Value of i: " + str(i))
    
except KeyboardInterrupt:
    
    print('KeyboardInterrupt')
    print("Value of i: " + str(i))
    store_last_seen("counter.txt", i)
    #client.delete_tweet(id=temptweetid)
    sys.exit(0)
   

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()    

"""
#print(response)

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r') #open the file in read mode
    last_seen_id = int(file_read.read().strip()) #read the Tweet ID as an integer
    file_read.close() #close file reader
    return last_seen_id #return the result

# Overwrite the previous Tweet ID with latest
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w') #open the file in write mode
    file_write.write(str(last_seen_id)) #write the ID as a string
    file_write.close() #close file writer
    return #return void

def reply():
    #tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    tweets = client.user_timeline(screen_name="firecrackergirI",count=200,include_rts=False,tweet_mode="extended")

    for tweet in reversed(tweets):
        if '#pat' in tweet.full_text.lower():
            print("Pattted!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_with_media(GIF, "@"+ tweet.user.screen_name, in_reply_to_status_id=tweet.id)

        elif '#pat' not in tweet.full_text.lower():
            print("Liked!: " + str(tweet.id) + " - " + tweet.full_text.lower())

        api.create_favorite(tweet.id)
        store_last_seen(FILE_NAME, tweet.id)
reply()*/
"""
