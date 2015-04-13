class SocialAddressBook:
    def __init__(self):
        self.people = set()
        self.names = {}
        self.friendWeb = {}
        self.nameOfFriends = []
        self.x = set()
       
    def addName(self, name, address):
        self.names[name] = address
       
    def addFriend(self, name, friend):
        if(name in self.friendWeb.keys()):
            self.friendWeb[name].append(friend)
        else:
            self.friendWeb[name] = []
            self.friendWeb[name].append(friend)
           
    #Is this function necessary?
    def address(self, name):
        return self.names[name]
 
    def friends(self,name,degree):
        l = []
        self.nameOfFriends.append(name)
        self.people = set()
       
        #loop through each person's friends by x degrees
        for i in range(degree):
            for j in self.friendWeb[name]:
                self.people.add(j)
            for x in list(self.people):
                if(x in self.friendWeb.keys()):
                    name = x
 
        return self.people


a = SocialAddressBook()
a.addName('Bill', 62)
a.addName('Emma', 56)
a.addName('Barb', 95)
a.addName('Fred', 46)
a.addName('Jane', 90)
a.addName('Joe', 33)
a.addName('Lisa', 21)
a.addName('Lucy', 18)
a.addName('Mary', 52)
a.addName('Sue', 12)
a.names
a.addFriend('Fred', 'Barb')
a.addFriend('Fred', 'Sue')
a.addFriend('Barb', 'Jane')
a.addFriend('Jane', 'Mary')
a.addFriend('Jane', 'Emma')
a.addFriend('Emma', 'Lisa')
