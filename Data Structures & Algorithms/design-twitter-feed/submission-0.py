class Twitter:

    def __init__(self):
        self.count = 0 # act as a timestamp for the tweetId
        self.followee_map = collections.defaultdict(set) # userId -> set of followeesId
        self.tweet_map = collections.defaultdict(list) # userId -> list of [count, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count += 1 # increase time 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []        # This will hold our final top 10 tweet IDs
        min_heap = []    # This will hold the pointers for our K-way merge
        # 1. Ensure the user follows themselves so their own tweets are included
        self.followee_map[userId].add(userId)
        # 2. Loop through everyone the user follows
        for followeeId in self.followee_map[userId]:
            # check the followee have tweets
            if self.tweet_map[followeeId]:
                index = len(self.tweet_map[followeeId]) - 1 # point at most recent tweet of this followee tweet
                # Pull the [count, tweetId] data from that index
                count, tweetId = self.tweet_map[followeeId][index]
                # Append to our list: [timestamp, tweetId, who tweeted it, next index to check]
                min_heap.append([-count, tweetId, followeeId, index-1])
        # turn into minheap
        heapq.heapify(min_heap)
        # 3. Pull tweets from the heap until we hit 10 or run out of tweets
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            # STEP 2: The code selected above executes right here...
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [-count, tweetId, followeeId, index - 1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee_map:
            self.followee_map[followerId].remove(followeeId)