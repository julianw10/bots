import tweepy
import random
import time as t
import signal
import sys
import os
import re
from datetime import datetime, timezone, timedelta
    
FILE_NAME='last.txt'
consumer_key='gtO7gSYInA6Q65FxN6iM9Hd5G'
consumer_secret='6J42MOj8VUU271LS03wnaqzCD9IjGxuoZazI1PdFpJ7kYsgEJn'
access_token='1593606700870803458-TgWQfiXFc4jI14FfchIiMheK7SkNHZ'
access_token_secret='xDCJUaHk0h634U07xTkdWycdBFdPXcT6TkXgz4QxPixUT'

current_account="mallow_bright"

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAACYTkAEAAAAAxx7RXGZiwO5oZbEMvh4zAx65pUg%3DzmddinXGCHSoAo6bPIeSjkQOUbiy7FzV8WI5COx8NKFoQoTAg4', consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret,access_token,access_token_secret)
api = tweepy.API(auth)

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
    
    
girls = ['Meiko', 'Smurfette', 'Dark Arle', 'Splash Woman', 'Lana', 'Crona', 'Hinomori Shizuku', 'Ganyu', 'Mipha', 'Rainbow Dash', 'Asuka', 'Akiyama Mizuki', 'Yor Forger', 'Femboys', 'a cat girlfriend', 'Kizuna Ai', 'Sage', 'Mii Fighter', 'Catgirl', 'Maki Harukawa', 'Doki Doki Literature Club', '2B', 'Basil', 'Nepgear', 'Yotsuba','Sunstar', 'Luisa Madrigal', 'Zone-Tan', 'Molly', 'Kazama Iroha', 'Klee', 'Monika', 'Cylindria', 'Inkling Boy', 'gang pull up', "Inkling girl"]
general=["Ratio", "Massive W", "Massive L", "I used to be a huge fan of you. Unfortunately your recent posts felt a bit off. Hopefully you can improve again in the future", "Seems like a W to me", "Seems like an L to me", "If you want to keep a loyal follower I suggest you to improve your post"]

time = datetime.now()-timedelta(hours=1)

def reply():
    last_id=read_last_seen(FILE_NAME)

    tweets = client.get_home_timeline(since_id=read_last_seen(FILE_NAME), exclude=['retweets'], tweet_fields=['author_id', 'in_reply_to_user_id', 'attachments', 'entities'], start_time=time)
    
    if tweets[0]:
        print(tweets[0])
        i=0
        
        for tweet in reversed(tweets[0]):    
            strings = []
            author_id = tweet.author_id
            
            user = client.get_user(id=author_id)[0]
            username_replied_to = ""
            
            if tweet.in_reply_to_user_id:
                username_replied_to = client.get_user(id=tweet.in_reply_to_user_id)[0].username
            
            username = user.username
            name = user.name 
            
            gimmick_accounts = ['crim_tweets_', 'insanepplYT', 'insultsrare', 'weirdreviewss', 'YearbookQuotes_', 'fuckedupfoods', 'InternetH0F', 'strangepacks', 'HelpingChads', 'strangepacks_', 'OrwellNGoode', 'SoftwareGore']
            onlyfanswomen = ['Nothennyfr', 'arabcnnie', 'iUsedToBeADuck', 'pokegff']
            g = []
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
                    strings = strings + ["Not anything", "This is anything", "Looks like anything to me! Nice!", "This is anything! Well done!"]
                else:
                    strings = general
                    g = []
                    match username:
                        case "StokeyyG2" | "nocontextfooty" | "firecrackergirI" | "ishowspeedsui" | "UTDTrey":
                            g = ['Soccer is an interesting game. Tiny ball, massive net…should be very, very easy to score points. And yet, sometimes a whole game goes by without a single goal. Stands to reason that the players just aren’t very good.',
                                        'Soccer is my {absolutely} favourite game. I love it so much. But my question is what is even its point? People walking around and dribbling a ball, what is the point? It can do better',
                                        'Is soccer really a good sport? What is the point? The players kick the ball on the ground for a few hours, sometimes not even scoring a goal and cry over every injury. Football is a REAL sport with actual amazing things happening. Follow a REAL sport!',
                                        'Soccer is a pretty interesting sport. In recent years it had absolutely positive impact on society. Unfortunately it fell kinda off. Very interested to see its future development']
                        case "DeludedPhobes":
                            g = ["Phobes are never deluded", "They are right. Respect them"]
                        case "gimmicksellouts":
                            g = ["Not a sellout. They need the money"]
                        case "honestsportz":
                            g = ["Not a honest sportstake", "You are not honest"]
                        case "crazyinteract":
                            g = ["Not a crazy interaction. I have to unfollow"]
                        case "origins_audio":
                            g = ["This video and audio doesn't seem iconic to me"]
                        case "CultureCrave":
                            g = ["Not a Culture Crave post", "Post real Culture Crave or I have to unfollow"]
                        case "SigmaMemes_69":
                            g = ["Not a Sigma Meme", "This is not a Sigma meme"]
                        case "OldMemeArchive":
                            g = ["This is not an ancient meme"]
                        case "Best0fTheNet":
                            g = ["Not the best of the net"]
                        case "WTF_Gimmick":
                            g = ["Seems completely normal to me"]
                        case "imindatinghell":
                            g = ["Not dating hell", "This is dating heaven"]
                        case "rSoftwareGore":
                            g = ["Completely normal software behaviour"]
                        case "WeHateThese":
                            g = ["I love this thing"]
                        case "fckeveryword":
                            g = ["Yes please", "Correct", "Me to please man"]
                        case "BeratStuff":
                            g = ["Not a post about stuff"]
                        case "Discord_Lies":
                            g = ["This is a Discord Truth. Unfollowed"]
                        case "weirddalle":
                            g = ["Not a weird dalle generation"]
                        case "GimmickAccsOOC2":
                            g = ["They are not out of character"]
                        case "amazingmap":
                            g = ["Not an amazing map"]
                        case "4chan_green":
                            g = ["Not a greentext", "This is a redtext, unfollowed"]
                        case "internetethos":
                            g = ["This is an internet hall of fame post", "Perfectly normal to me"]
                        case "TerribleFinance":
                            g = ["Good finance only here"]
                        case "offbranddesigns":
                            g = ["Not offbrand design"]
                        case "StrangestMedia":
                            g = ["Perfectly fine media here. I have to unfollow"]
                        case "ConSelfOwns":
                            g = ["This is left wing cope behaviour. You have lost a loyal follower"]
                        case "TheGimmickAcc":
                            g = ["Not preceding a legendary event sadly"]
                        case "ConsoomerLs":
                            g = ["Consumers are always a W"]
                        case "Internet_TLCM":
                            g = ["The left can meme very good", "The left can meme better than the right"]
                        case "OrwellNGoode":
                            g = ["Not an OrwellNGoode post"]
                        case "BasedByAccident":
                            g = ["This is not based by accident", "This is unbased"]
                        case "WomenPostingLs":
                            g = ["Women always post Ws"]
                        case "TerribleMaps":
                            g = ["This is an amazing map. You have lost a loyal follower"]
                        case "SpotifyWeird":
                            g = ["Spotify is always good", "Spotify is never weird"]
                        case "RespectfulMemes":
                            g = ["Not a respectful meme"]
                        case "PoorlyAgedThings":
                            g = ["This aged good"]
                        case "insultsrare":
                            g = ["This is a common insult"]
                        case "fuckedupfoods":
                            g = ["Looks perfectly tasty to me"]
                        case "TransphobicsL":
                            g = ["This is a phobes W moment", "They say Ws"]
                        case "CointersTakingLs":
                            g = ["Cointers always take Ws"]
                        case "crim_tweets_":
                            g = ["Not a criminal tweet in my books"]
                        case "bad2sentence":
                            g = ["These are two good sentences"]
                        case "AAAAAWTFAAAAA":
                            g = ["Not an AAAAAAAA post"]
                        case "DuolingoStrange":
                            g = ["This is a completely normal Duolingo post"]
                        case "FungersTakingLs":
                            g = ["NFTs are the best thing in the entire world"]
                        case "namesoun":
                            g = ["This is not a name soundalike"]
                        case "cringeposts":
                            g = ["This is a perfectly fine post"]
                        case "weirdreviewss":
                            g = ["This is an amazing review in my books"]
                        case "LocalBateman":
                            g = ["Not a local bateman post sadly"]
                        case "ShockedAtShit":
                            g = ["I am not shocked at this. This is good"]
                        case "dms_weird":
                            g = ["A perfectly fine DM"]
                        case "WhiningGimmicks":
                            g = ["They are spitting facts"]
                        case "strangepacks_":
                            g = ["Not a strange starterpack"]
                        case "HelpingChads":
                            g = ["They are not helping chads"]
                        case "image_origins":
                            g = ["Not an origin of an iconic image"]
                        case "ShitpostGate":
                            g = ["Not a gate to a shpost"]
                        case "ManMilk2":
                            g = ["This makes me feel no pain. This makes me feel good"]
                        case "wildtiktokss":
                            g = ["A completely normal Tiktok in my opinion"]
                        case "OddSteamReviews":
                            g = ["Not an odd Steam review"]
                        case "insanepplYT":
                            g = ["They are completely sane"]
                        case "DudesPostingWs":
                            g = ["They are posting their L"]
                        case "ShapedInternet":
                            g = ["Did not shape the internet"]
                        case "InternetH0F":
                            g = ["Not an Internet Hall of Fame post"]
                        case "GreenTextRepost":
                            g = ["This is not a Greentext", "This is a Redtext"]
                        case "RightWingCope":
                            g = ["This is left wing cope, you need to get well soon"]
                        case "gimmickannoying":
                            g = ["They are never annoying"]
                        case "onlyFansPostinL":
                            g = ["Onlyfans girls always post Ws"]
                        case "mike27356894":
                            g = ["Thank you Mike for your enlightement. Massive W as always", "Best post ever", "Amazing post"]
                        case "youtube_bad":
                            g = ["Youtube is good"]
                        case "stone_toss":
                            g = ["Stonetoss comics are not funny"]
                        case "reddit_lies":
                            g = ["Reddit always tells the truth", "Reddit never lies"]
                        case "tragicbirdapp":
                            g = ["Not a tragic bird app post"]
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
            if g:
                strings = strings + g
                
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
                print()
                message = random.choice(strings)
                message = message.format(authorname = name)
                try:
                    client.like(tweet.id)
                except Exception as e:
                    print("Failed to like post. Error " + str(e))
                    
                try:
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message, exclude_reply_user_ids=exclude_ids)                    
                    print("Reply:" + message)
                    t.sleep(5)                    
                except Exception:
                    print("Failed to send reply")
            print("-"*50)
            store_last_seen(FILE_NAME, tweet.id)
            i = i+1
def random_porn():
    
    texts = ["I like her so much", "Why does she look so hot?", "I'm in love", "She's looks so beautiful", "She looks so hot"]
    dir = 'C:\\Users\Julian\Pictures\Shadowfightgirls'
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
    tweets = client.get_home_timeline(exclude=['retweets'],start_time=time)
    id = next(reversed(tweets[0])).id-1
    stored_id = read_last_seen(FILE_NAME)
    if id>stored_id:
        store_last_seen(FILE_NAME,id)
    print(tweets)
    print(id)
    
    while True:
        reply()
        t.sleep(6) 
    
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
