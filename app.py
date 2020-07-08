from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

# la ruta de donde este la base de datos
db_connect = create_engine('sqlite:///simpson.db')
app = Flask(__name__)
api = Api(app)


class Characters(Resource):
    def get(self):
        conn = db_connect.connect() #hace la conexion
        query = conn.execute("select * from characters") #ejecuta el query y retorna un json
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        name = request.args['name']
        gender = request.args['gender']
        status = request.args['status']
        occupation = request.args['occupation']
        image = request.args['image']
        query = conn.execute("insert into characters values('{}','{}','{}','{}','{}')".format(
            name, gender, status, occupation, image
        ))
        return {'status': 'nuevo personaje añadido'}


class Locations(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from locations")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Episodes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from episodes")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class Cities(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from cities")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class CharactersData(Resource):
    def get(self, character_id):
        conn = db_connect.connect()
        query = conn.execute("select * from characters where rowid =%d " % int(character_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self,character_id):
        type = request.args['type']
        change = request.args['value']
        conn = db_connect.connect()
        query = conn.execute("update characters set '%s' ='%s' where rowid = %s " % (type, change, int(character_id)))
        return {'status': 'Cambio de %s realizado' % type}

    def delete(self, character_id):
        conn = db_connect.connect()
        query = conn.execute("delete from characters where rowid= %d" % int(character_id))
        return {'status': 'Character number %d deleted' % int(character_id)}


class LocationsData(Resource):
    def get(self, location_id):
        conn = db_connect.connect()
        query = conn.execute("select * from locations where rowid =%d " % int(location_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self,location_id):
        type = request.args['type']
        change = request.args['value']
        conn = db_connect.connect()
        query = conn.execute("update locations set '%s' ='%s' where rowid = %s " % (type, change, int(location_id)))
        return {'status': 'Cambio de %s realizado' % type}

    def delete(self, location_id):
        conn = db_connect.connect()
        query = conn.execute("delete from locations where rowid= %d" % int(location_id))
        return {'status': 'Character number %d deleted' % int(location_id)}

class EpisodesData(Resource):
    def get(self, episode_id):
        conn = db_connect.connect()
        query = conn.execute("select * from episodes where rowid=%d " % int(episode_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self,episode_id):
        type = request.args['type']
        change = request.args['value']
        conn = db_connect.connect()
        query = conn.execute("update episodes set '%s' ='%s' where rowid = %s " % (type, change, int(episode_id)))
        return {'status': 'Cambio de %s realizado' % type}

    def delete(self, episode_id):
        conn = db_connect.connect()
        query = conn.execute("delete from episodes where rowid= %d" % int(episode_id))
        return {'status': 'Character number %d deleted' % int(episode_id)}

class CitiesData(Resource):
    def get(self, city_id):
        conn = db_connect.connect()
        query = conn.execute("select * from cities where rowid=%d " % int(city_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self,city_id):
        type = request.args['type']
        change = request.args['value']
        conn = db_connect.connect()
        query = conn.execute("update cities set '%s' ='%s' where rowid = %s " % (type, change, int(city_id)))
        return {'status': 'Cambio de %s realizado' % type}

    def delete(self, city_id):
        conn = db_connect.connect()
        query = conn.execute("delete from cities where rowid= %d" % int(city_id))
        return {'status': 'Character number %d deleted' % int(city_id)}

api.add_resource(Characters, '/characters') #
api.add_resource(Locations, '/locations')
api.add_resource(Cities, '/cities')
api.add_resource(Episodes, '/episodes')
api.add_resource(CharactersData, '/characters/<character_id>') #route with parameter for changes
api.add_resource(LocationsData, '/locations/<location_id>')
api.add_resource(EpisodesData, '/episodes/<episode_id>')
api.add_resource(CitiesData, '/cities/<city_id>')

if __name__ == '__main__':
    app.run(port='5000')


