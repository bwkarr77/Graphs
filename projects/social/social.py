import random

from util import Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(1, num_users+1):
            self.add_user(i)

        # Create friendships
        n = len(self.users)
        for user_id in self.users:
            for num_friends in range(random.randrange(1, avg_friendships)):
                # friend_id = number between 1 and n (number of users)
                friend_id = random.randrange(1, n)

                # friend_id cannot be assigned to user_id
                if friend_id == user_id:
                    # if friend_id is last person in self.users:
                    if friend_id == n:
                        friend_id -= 1
                    else:
                        friend_id += 1

                # friendships are bi-directional
                if friend_id not in self.friendships[user_id]:
                    self.add_friendship(user_id, friend_id)
                    # assigns current user to the friend's-friendslist
                    if user_id not in self.friendships[friend_id]:
                        self.add_friendship(friend_id, user_id)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        stack = Stack()
        stack.push([user_id])
        # dictionary for checking if users aren't connected to the user_id
        not_visited = self.users

        while stack.size() > 0:
            path = stack.pop()
            user = path[-1]

            if user in not_visited:
                # if users are connected to user_id, remove from dict
                not_visited.pop(user)
                # will return a dictionary of users NOT connected to user_id

            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    if friend not in visited:
                        new = list(path)
                        new.append(friend)
                        stack.push(new)

        visited['users not connected'] = list(not_visited.keys())
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
