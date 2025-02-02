from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# In-memory data storage (replace with a database in a real-world application)
data_storage = []


class DataResource(Resource):
    """
    Resource to handle data operations.
    """

    def get(self):
        """
        Get all stored data.
        """
        return {"data": data_storage}

    def post(self):
        """
        Add data to the storage.
        """
        data = request.form.get('data')
        data_storage.append(data)
        return {"message": "Data added successfully", "data": data}


# API routes
api.add_resource(DataResource, '/data')


# Web route for form submission
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    HTML form to submit data.
    """
    if request.method == 'POST':
        data = request.form.get('data')
        data_storage.append(data)
        return f"Data submitted: {data}"
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)