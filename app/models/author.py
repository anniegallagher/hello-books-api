from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def to_dict(self):
        author_as_dict = {}
        author_as_dict["id"] = self.id
        author_as_dict["name"] = self.name


        return author_as_dict

    @classmethod
    def from_dict(cls, author_data):
        new_author = cls(title=author_data["name"])
        return new_author