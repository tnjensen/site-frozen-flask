from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("Static files have been generated successfully.")