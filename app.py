from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

# la ruta de donde este la base de datos
db_connect = create_engine('sqlite:///simpson.db')
app = Flask(__name__)
api = Api(app)


class Content(Resource):
    def get(self):
        ip = 'http://127.0.0.1:5000/api/'
        content = {}
        content['data'] = []
        content['data'].append({
            'character': ip.__add__('characters'),
            'locations': ip.__add__('locations'),
            'cities': ip.__add__('cities'),
            'episodes': ip.__add__('episodes')
        })
        return jsonify(content)


class Characters(Resource):
    def get(self):
        nameQuery = request.args.get('name', None)
        genderQuery = request.args.get('gender', None)
        statusQuery = request.args.get('status', None)
        conn = db_connect.connect()  # hace la conexion
        if nameQuery:
            query = conn.execute("select * from characters where name like '%{}%' ".format(str(nameQuery)))
        elif genderQuery:
            query = conn.execute("select * from characters where gender like '%{}%' ".format(str(genderQuery)))
        elif statusQuery:
            query = conn.execute("select * from characters where status like '%{}%' ".format(str(statusQuery)))
        else:
            cantidad = conn.execute("select count(*) from characters")
            query = conn.execute("select * from characters")
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
        nameQuery = request.args.get('name', None)
        typeQuery = request.args.get('type', None)
        useQuery = request.args.get('use', None)
        if nameQuery:
            query = conn.execute("select * from locations where name like '%{}%' ".format(str(nameQuery)))
        elif typeQuery:
            query = conn.execute("select * from locations where type like '%{}%' ".format(str(typeQuery)))
        elif useQuery:
            query = conn.execute("select * from locations where use like '%{}%' ".format(str(useQuery)))
        else:
            query = conn.execute("select * from locations")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Episodes(Resource):
    def get(self):
        conn = db_connect.connect()
        nameQuery = request.args.get('name', None)
        episodeQuery = request.args.get('episode', None)
        dateQuery = request.args.get('date', None)
        seasonQuery = request.args.get('season', None)
        if nameQuery:
            query = conn.execute("select * from episodes where name like '%{}%' ".format(str(nameQuery)))
        elif episodeQuery:
            query = conn.execute("select * from episodes where episode like '%{}%' ".format(int(episodeQuery)))
        elif dateQuery:
            query = conn.execute("select * from episodes where air_date like '%{}%' ".format(str(dateQuery)))
        elif seasonQuery:
            query = conn.execute("select * from episodes where season like '%{}%' ".format(int(seasonQuery)))
        else:
            query = conn.execute("select * from episodes")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Cities(Resource):
    def get(self):
        conn = db_connect.connect()
        nameQuery = request.args.get('name', None)
        populationQuery = request.args.get('type', None)
        if nameQuery:
            query = conn.execute("select * from cities where name like '%{}%' ".format(str(nameQuery)))
        elif populationQuery:
            query = conn.execute("select * from cities where population like '%{}%' ".format(int(populationQuery)))
        else:
            query = conn.execute("select * from cities")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class CharactersData(Resource):
    def get(self, character_id):
        conn = db_connect.connect()
        query = conn.execute("select * from characters where rowid =%d " % int(character_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self, character_id):
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

    def put(self, location_id):
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

    def put(self, episode_id):
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

    def put(self, city_id):
        type = request.args['type']
        change = request.args['value']
        conn = db_connect.connect()
        query = conn.execute("update cities set '%s' ='%s' where rowid = %s " % (type, change, int(city_id)))
        return {'status': 'Cambio de %s realizado' % type}

    def delete(self, city_id):
        conn = db_connect.connect()
        query = conn.execute("delete from cities where rowid= %d" % int(city_id))
        return {'status': 'Character number %d deleted' % int(city_id)}


api.add_resource(Content, '/api', '/api/')
api.add_resource(Characters, '/api/characters')
api.add_resource(Locations, '/api/locations')
api.add_resource(Cities, '/api/cities')
api.add_resource(Episodes, '/api/episodes')
api.add_resource(CharactersData, '/api/characters/<character_id>')  # route with parameter for changes
api.add_resource(LocationsData, '/api/locations/<location_id>')
api.add_resource(EpisodesData, '/api/episodes/<episode_id>')
api.add_resource(CitiesData, '/api/cities/<city_id>')

if __name__ == '__main__':
    app.run(debug=True)
