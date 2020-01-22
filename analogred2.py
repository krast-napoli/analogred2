from flask import Flask, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return render_template('wrapper.html', rugbychamps=rugbychamps)

rugbychamps = {}

class Rugbychampion(Resource):
    def get(self, rug_id):
        return {rug_id: rugbychamps[rug_id]}
        

    def put(self, rug_id):
       rugbychamps[rug_id] = request.form['data']
       return {rug_id: rugbychamps[rug_id]}

# Next part of code is a solution to append data as a new element in list
# If my dictionary rugbychamps has nested list inside, PUT command will append value from "data" to the list
# This function isn't realised yet

#    def put(self, rug_id):
#        if isinstance(rugbychamps[rug_id]) == list:
#            rugbychamps[rug_id].append(request.form['data'])
#        else:
#            rugbychamps[rug_id] = request.form['data']
            
#            return {rug_id: rugbychamps[rug_id]}

    
    def delete(self, rug_id):
        del rugbychamps[rug_id]
        return '', 204

api.add_resource(Rugbychampion, '/<string:rug_id>')
if __name__ == '__main__':
    app.run(debug=True)



        