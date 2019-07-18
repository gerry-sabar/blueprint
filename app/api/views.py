from . import api
from flask_restplus import Api, Resource
from ..models import Log,LogSchema  # import class & schema to serialize JSON

api = Api(api, doc='/docs')
name_space = api.namespace('my_api', description='API Project')

@name_space.route("/")
class LogList(Resource):
    def get(self):  # fetch all logs from database
        logs = Log.query.all()
        result = []
        schema = LogSchema()
        for log in logs:
            result.append(schema.dump(log))
        return {
            "data": result
        }

    def post(self):  # will be used to create a new log record
        return {
            "status": "Create new log"
        }


@name_space.route("/<int:id>")
class LogDetail(Resource):
    def get(self, id):  # will be used to see one particular log detail
        return {
            "status": "See detail for log with id " + str(id)
        }

    def put(self, id):  # will be used to update particular log
        return {
            "status": "Updated log with id " + str(id)
        }

    def delete(self, id):  # will be used to delete particular log
        return {
            "status": "Deleted log with id " + str(id)
        }