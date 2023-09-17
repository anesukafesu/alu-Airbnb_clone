from models.engine import file_storage

# classes = ["BaseModel", "User", "Amenity",
#            "City", "Place", "Review", "State"]

storage = file_storage.FileStorage()
storage.reload()
