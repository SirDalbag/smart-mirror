class News:
    def __init__(self, author, title, description):
        self.author = author
        self.title = title
        self.description = description

    def __repr__(self):
        return f"News: {self.title} - {self.description}. Author: {self.author}"
