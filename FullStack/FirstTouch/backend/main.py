from flask import jsonify, request
from sqlalchemy import *
from model import PLCLIST
from config import db, app

@app.route("/Lists", methods=["GET"])
def get_plcs():
    plc_list = PLCLIST.query.all()
    plc_list_json = list(map(lambda x: x.to_json(), plc_list))
    return jsonify({"plc_list": plc_list_json})

@app.route("/create_plc", methods=["POST"])
def create_plc():
    if request.json is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    ip = request.json.get("ip")
    name = request.json.get("name")

    if not ip or not name:
        return jsonify({"error": "Both 'ip' and 'name' fields are required"}), 400

    new_plc = PLCLIST(ip=ip, name=name)
    try:
        db.session.add(new_plc)
        db.session.commit()

    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify(new_plc.to_json()), 201

@app.route("/update_plc/<int:user_id>", methods=["PATCH"])
def update_plc(user_id):
    plc = PLCLIST.query.get(user_id)

    if not plc:
        return jsonify({"message": "User Not Found"}), 404
    
    data = request.json
    plc.ip = data.get("ip", plc.ip)
    plc.name = data.get("name", plc.name)

    db.session.commit()
    return jsonify({"message": "user updated"}), 200

@app.route("/delete_plc/<int:user_id>", methods=["DELETE"])
def delete_plc(user_id):
    plc = PLCLIST.query.get(user_id)

    if not plc:
        return jsonify({"message": "User Not Found"}), 404
    
    db.session.delete(plc)
    db.session.commit()

    return jsonify({"message": "user deleted"}), 200



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)