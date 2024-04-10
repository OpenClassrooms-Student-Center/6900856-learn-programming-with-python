class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        # Method for displaying the file
        pass

class Image(File):
    def __init__(self, image_size):
        self.image_size = image_size

    def display(self):
        # Method specific for displaying an image
        pass

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        # Method for user login
        pass
    
    def post(self, thread, content):
        # Method for posting in a thread
        pass
    
    def make_thread(self, title, content):
        # Method for creating a new thread
        pass

class Moderator(User):
    def edit(self, post, content):
        # Method for editing a post
        pass

class Post:
    def __init__(self, user, time_of_posting, content):
        self.user = user
        self.time_of_posting = time_of_posting
        self.content = content
    
    def display(self):
        # Method for displaying the post
        pass

class FilePost(Post):
    def __init__(self, file):
        self.file = file

class Thread:
    def __init__(self, title, time_of_creation):
        self.title = title
        self.time_of_creation = time_of_creation
        self.posts = []  # Collection of posts
    
    def display(self):
        # Method for displaying the thread
        pass
    
    def add_post(self, post):
        # Method for adding a post to the thread
        self.posts.append(post)
