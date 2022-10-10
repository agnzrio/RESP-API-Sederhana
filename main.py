from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

databarang = {}


class MyResource(Resource):
    def get(self):
        return databarang

    def post(self):
        nama_barang = request.form["namabarang"]
        jumlah_barang = request.form["jumlahbarang"]
        databarang["namabarang"] = nama_barang
        databarang["jumlahbarang"] = jumlah_barang
        response = {"msg": "Data berhasil disimpan"}
        return response


api.add_resource(MyResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
