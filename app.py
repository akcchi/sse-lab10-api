from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Southern Gothic",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Dystopian Fiction",
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "genre": "Romantic Novel",
    },
    {
        "id": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "American Literature",
    },
    {
        "id": 5,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "publication_year": 2008,
        "genre": "Young Adult Dystopian",
    },
]


# Return books matching URL parameters in json format
def process_query(query):
    if query:
        ret_list = []  # store matching books
        query_keys = list(query.keys())

        for dict in books:
            for key in query_keys:
                if key in dict:
                    if key == "id" or key == "publication_year":
                        if int(query[key]) == dict[key]:
                            ret_list.append(dict)
                            break  # next book
                    else:
                        if query[key].lower() in dict[key].lower():
                            ret_list.append(dict)
                            break  # next book

        if not ret_list:
            return ("no matching books", 404)
        else:
            return jsonify(ret_list)

    else:
        return jsonify(books)


@app.route("/books", methods=["GET"])
def get_books():
    query = request.args.to_dict()
    return process_query(query)


if __name__ == "__main__":
    app.run(debug == True)
