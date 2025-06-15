# Your code here
class Book :
    def __init__(self, set_title, set_author, set_pages):
        self.title = set_title
        self.author = set_author
        self.pages = set_pages
        
    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages}")
    

# Example:
# b = Book("The Hobbit", "J.R.R. Tolkien", 310)
# b.summary()

# Expected Output:
# The Hobbit by J.R.R. Tolkien, 310 pages

b = Book("The Hobbit", "J.R.R. Tolkien", 310)
b.summary()