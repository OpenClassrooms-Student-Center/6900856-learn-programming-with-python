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

if __name__ == "__main__":
    # Creating instances of GIF and JPG images
    gif_image = GIFImage("animation.gif", "2MB", "Funny cat animation")
    jpg_image = JPGImage("landscape.jpg", "5MB", "Beautiful scenery")

    # Calling display method for each image
    print("Displaying GIF image:")
    gif_image.display()
    print("\nDisplaying JPG image:")
    jpg_image.display()
