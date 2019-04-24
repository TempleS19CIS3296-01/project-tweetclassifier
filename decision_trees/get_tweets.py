import tweepy
import csv

#Twitter API credentials
consumer_key = "Cni7951JXNdCIoCxPYr9hYO3Z"
consumer_secret = "L5dKdHq3GQmtsSqJUW3r1OwVf9enpLVayR8WeiNqk6HtkDp4Ep"
access_token = "723661697551097856-AXqOAdGblcHL2GnseiCdzLNA2c2YDY0"
access_token_secret = "MvIC6QBEre2Fv19fMWG0l4JiUFPV4RUbZxYo17F34Swbi"

GET_ALL_TWEETS = True

def get_all_tweets():
    screen_name = input("insert the twitter user you want to analyze...  \n")
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []	
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    
    #keep grabbing tweets until there are no tweets left to grab
    if GET_ALL_TWEETS:
        while len(new_tweets) > 0:
            print ("getting tweets before %s" % (oldest))
            
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
            
            #save most recent tweets
            alltweets.extend(new_tweets)
            
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            
            print ("...%s tweets downloaded so far" % (len(alltweets)))
    print ("...%s tweets downloaded total" % (len(alltweets)))
    total_tweets_parsed = len(alltweets)
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [["0",tweet.id_str, tweet.created_at,"NO_QUERY",screen_name, str(tweet.text.encode("utf-8"))[2:-1]] for tweet in alltweets]
    
    #write the csv	
    with open('predict_data/tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)

    return total_tweets_parsed
if __name__=='__main__':
    get_all_tweets()
