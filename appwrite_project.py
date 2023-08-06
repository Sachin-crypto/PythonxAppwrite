import os
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID

""" Configuring Appwrite Client For API Access """
# Instantiating Appwrite Client
client = Client()

# To load environment variables
load_dotenv()

(client
 # Setting API Endpoint
 .set_endpoint('https://cloud.appwrite.io/v1')
 # Setting Project ID
 .set_project(os.getenv("PROJECT_ID"))
 # Setting API Key
 .set_key(os.getenv("API_KEY"))
 )

databases = Databases(client)
""" Configuration Code Ends Here """

"""Creating Database"""
# To generate unique database ID
db_id = ID.unique()

create_db = databases.create(db_id, 'BooksDB')
print("Database Successfully Created.")
""" Database Creation Code Ends Here """

"""Creating Collections"""
# Database ID
database_id = create_db['$id']
# For Generating Unique Collection ID
collection_id = ID.unique()

# Creating a New Collection
new_collection = databases.create_collection(database_id=database_id,
                                             collection_id=collection_id,
                                             name='Books')

print('Collection Successfully Created.')
""" Collection Creation Code Ends Here """

"""Creating Attributes"""
# Collection ID of Book
c_id = new_collection['$id']

""" Creating integer attribute """
# ID Attribute
book_id = databases.create_integer_attribute(database_id=database_id,
                                             collection_id=c_id,
                                             key="id",
                                             required=True)

""" Creating url attribute """
# URL Attribute
book_url = databases.create_url_attribute(database_id=database_id,
                                          collection_id=c_id,
                                          key="image",
                                          required=True)

""" Creating string attribute """
# Title Attribute
book_title = databases.create_string_attribute(database_id=database_id,
                                               collection_id=c_id,
                                               key="title",
                                               required=True,
                                               size=100)

# Author Attribute
book_author = databases.create_string_attribute(database_id=database_id,
                                                collection_id=c_id,
                                                key="author",
                                                required=True,
                                                size=50)

# Genre Attribute
book_genre = databases.create_string_attribute(database_id=database_id,
                                               collection_id=c_id,
                                               key="genre",
                                               required=True,
                                               size=50)

print("Attributes Successfully Created.")
""" Attribute Creation Code Ends Here """

""" Adding Documents """
# Unique Identifier for Document ID
document_id = ID.unique()

""" Function for Adding Documents(data) in the Database """


def add_doc(document):
    try:
        doc = databases.create_document(
            database_id=database_id,
            collection_id=c_id,
            document_id=document_id,
            data=document
        )

        print("Id:", doc['id'])
        print("Image:", doc['image'])
        print("Title:", doc['title'])
        print("Author:", doc['author'])
        print("Genre:", doc['genre'])
        print("-" * 20)

    except Exception as e:
        print(e)
        print("Something went wrong, exiting the program.")


# Data To Be Added
book_1 = {
    "id": 1,
    "image": "https://i.pinimg.com/474x/dc/17/2d/dc172d6fa3f5461d94e6d384aded2cb4.jpg",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction"
}

book_2 = {
    "id": 2,
    "image": "https://i.pinimg.com/originals/0b/bf/b5/0bbfb59b4d5592e2e7fac9930012ce6d.jpg",
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction"
}

book_3 = {
    "id": 3,
    "image": "https://i.pinimg.com/736x/66/1d/17/661d179ab722e67eed274d24b8965b0d.jpg",
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance"
}

book_4 = {
    "id": 4,
    "image": "https://i.pinimg.com/originals/68/c5/4c/68c54c9599ba37d9ab98c0c51afe2298.png",
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "genre": "Psychological Fiction"
}

# Calling function with the data to be added
add_doc(book_1)
add_doc(book_2)
add_doc(book_3)
add_doc(book_4)
print("Documents Successfully Added.")
