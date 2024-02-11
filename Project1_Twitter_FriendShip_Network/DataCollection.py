import tweepy
from tweepy import OAuthHandler
import pandas as pd

consumer_key = '0C96p0R1rfGjTuJ5OVRAKSlZc'
consumer_secret = 'MzXX8xbLAqjOeHoI3FFxcRoh8yL829wyahB5STzywtLpJoUTCe'
access_token = '898297547659165696-6eeaRMcGIrgPMt9dgQcFwWUcTCyeGmI'
access_token_secret = 'tUQI0WNMcqtww831L0xT2IOgKjjjMsSwEMzMcpGeGaD0F'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
me = api.get_follower_ids(screen_name="Swathi_Rao99")

# Create a list to store the data
data = []
limit = 5
limit2 = 5
index = 0
findex = 0
frindex = 0

# Crawl the followers and friends of each node
for n in range(len(me)):
 index += 1
 try:
    # Get the node's screen name
    screen_names1 = api.get_user(user_id=me[n])
    screen_names = screen_names1.screen_name

    # Get the node's followers
    followers1 = api.get_follower_ids(user_id=me[n])
    followers = []
    for x in range(len(followers1)):
        findex += 1
        screen_nam1 = api.get_user(user_id=followers1[x])
        screen_nam = screen_nam1.screen_name
        followers.append(screen_nam)
        if findex == limit2:
            break

    # Get the node's friends
    friends1 = api.get_friend_ids(user_id=me[n])
    friends = []
    for y in range(len(friends1)):
        frindex += 1
        scr_nam1 = api.get_user(user_id=friends1[y])
        scr_nam = scr_nam1.screen_name
        friends.append(scr_nam)
        if frindex == limit2:
            break

    # Store the data in the list
    data.append([screen_names, followers, friends])
    if index == limit:
     break
 except:
    continue

# Convert the list to a Pandas dataframe
data = pd.DataFrame(data, columns=['screen_names', 'followers', 'friends'])

# Save the dataframe to a CSV file
data.to_csv('friendship_network.csv', index=True)