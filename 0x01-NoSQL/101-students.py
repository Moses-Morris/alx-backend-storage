from pymongo import MongoClient

def list_all(mongo_collection):
    """ Lists all documents in a collection """
    documents = mongo_collection.find()
    return documents

def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": { "$first": "$name" },
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        }
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students

# Example usage:
if __name__ == "__main__":
    # Assuming you have a MongoDB client and a 'students' collection
    client = MongoClient("mongodb://localhost:27017")
    db = client["your_database_name"]  # Replace 'your_database_name' with your actual database name
    collection = db["students"]        # Replace 'students' with your actual collection name

    top_students_list = top_students(collection)
    for idx, student in enumerate(top_students_list, 1):
        print(f"{idx}. {student['name']}: {student['averageScore']}")
