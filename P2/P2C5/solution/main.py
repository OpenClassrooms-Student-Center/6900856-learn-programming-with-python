from abc import ABC

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        # Method for displaying the file
        pass

class Image(File):
    def __init__(self, name, size, alt_text):
        super().__init__(name, size)
        self.alt_text = alt_text

    def display(self):
        # Overridden method to display the image with its name and alt text
        print(f"Image Name: {self.name}, Alt Text: {self.alt_text}")

class GIFImage(Image):
    def __init__(self, name, size, alt_text):
        super().__init__(name, size, alt_text)

    def display(self):
        # Overridden method to display the GIF image with its type
        print(f"Image Type: GIF, Name: {self.name}, Alt Text: {self.alt_text}")

class JPGImage(Image):
    def __init__(self, name, size, alt_text):
        super().__init__(name, size, alt_text)

    def display(self):
        # Overridden method to display the JPG image with its type
        print(f"Image Type: JPG, Name: {self.name}, Alt Text: {self.alt_text}")

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

class Post(ABC):
    def __init__(self, user, time_of_posting, content):
        self.user = user
        self.time_of_posting = time_of_posting
        self.content = content
    
    def display(self):
        # Method for displaying the post
        pass

class FilePost(Post):
    def __init__(self, user, time_of_posting, content, file):
        super().__init__(user, time_of_posting, content)
        self.file = file

    def display(self):
        print(f"{self.user} : <{self.time_of_posting}> {self.content}")
        self.file.display()

class Thread:
    def __init__(self, title, time_of_creation):
        self.title = title
        self.time_of_creation = time_of_creation
        self.posts = []  # Collection of posts
    
    def display(self):
        print("Thread Title:", self.title)
        print("Created At:", self.time_of_creation)
        print("\nPosts:")
        for post in self.posts:
            post.display()
            print("\n------------------------\n")
    
    def add_post(self, post):
        # Method for adding a post to the thread
        self.posts.append(post)

if __name__ == "__main__":
    # Creating File
    gif_image = GIFImage("animation.gif", "2MB", "Funny cat animation")
    jpg_image = JPGImage("landscape.jpg", "5MB", "Beautiful scenery")

    # Creating FilePost
    post1 = FilePost("Alice", "2023-03-20 10:00", "This is the first post.", gif_image)
    post2 = FilePost("Bob", "2023-03-20 10:15", "This is the second post.", jpg_image)


    thread = Thread("Python Programming", "2023-03-20")
    thread.add_post(post1)
    thread.add_post(post2)
    thread.display()
