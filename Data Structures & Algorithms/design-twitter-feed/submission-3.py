class Twitter:

    def __init__(self):
        self.time_stamp = 0 # tweet current time
        self.tweet_map = collections.defaultdict(list) # userId -> list of [time_stamp, tweetId]
        self.followee_map = collections.defaultdict(set) # userId -> hashset of user the userId follows

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time_stamp, tweetId])
        self.time_stamp += 1 # increment timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = [] # track the most recent tweets for the current user followers and the user
        res = [] # store the 10 most recent tweets
        self.followee_map[userId].add(userId) # user is a follower of himself
        
        for followeeId in self.followee_map[userId]: # loop all the current user followers
            if self.tweet_map[followeeId]: # check this user have tweets 
                idx = len(self.tweet_map[followeeId]) - 1 # last index
                time_stamp, tweetId = self.tweet_map[followeeId][idx] # unpack
                min_heap.append([-time_stamp, tweetId, followeeId, idx-1])
            heapq.heapify(min_heap)
        
        while min_heap and len(res) < 10:
            # pop
            time_stamp, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            # push
            if idx >= 0:
                # push the current user next most recent tweet 
                next_time_stamp, next_tweetId = self.tweet_map[followeeId][idx]
                heapq.heappush(min_heap, [-next_time_stamp, next_tweetId, followeeId, idx-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee_map[followerId]:
            self.followee_map[followerId].remove(followeeId)
        
