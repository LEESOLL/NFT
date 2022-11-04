from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.9pyyebx.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.dbsparta


# ------------------------------------------ CONNECTION ----------------------------------------


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/oong')
def oong():
    return render_template('oong.html')


@app.route('/song')
def song():
    return render_template('song.html')


@app.route('/sol')
def sol():
    return render_template('sol.html')


@app.route('/chan')
def chan():
    return render_template('chan.html')


@app.route('/hong')
def hong():
    return render_template('hong.html')


# ------------------------------------------ COMMENTS ------------------------------------------

# ------------------------------------------------------------ POST START
@app.route("/comment/main", methods=["POST"])
def maincomment_post():
    mainname_receive = request.form["mainname_give"]
    maincomment_receive = request.form["maincomment_give"]

    doc = {
        'mainname': mainname_receive,
        'maincomment': maincomment_receive
    }

    db.mainfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/comment/oong", methods=["POST"])
def oongcomment_post():
    oongname_receive = request.form["oongname_give"]
    oongcomment_receive = request.form["oongcomment_give"]

    doc = {
        'oongname': oongname_receive,
        'oongcomment': oongcomment_receive
    }

    db.oongfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/comment/song", methods=["POST"])
def songcomment_post():
    songname_receive = request.form["songname_give"]
    songcomment_receive = request.form["songcomment_give"]

    doc = {
        'songname': songname_receive,
        'songcomment': songcomment_receive
    }

    db.songfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/comment/sol", methods=["POST"])
def solcomment_post():
    solname_receive = request.form["solname_give"]
    solcomment_receive = request.form["solcomment_give"]

    doc = {
        'solname': solname_receive,
        'solcomment': solcomment_receive
    }

    db.solfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/comment/chan", methods=["POST"])
def chancomment_post():
    channame_receive = request.form["channame_give"]
    chancomment_receive = request.form["chancomment_give"]

    doc = {
        'channame': channame_receive,
        'chancomment': chancomment_receive
    }

    db.chanfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/comment/hong", methods=["POST"])
def hongcomment_post():
    hongname_receive = request.form["hongname_give"]
    hongcomment_receive = request.form["hongcomment_give"]

    doc = {
        'hongname': hongname_receive,
        'hongcomment': hongcomment_receive
    }

    db.hongfan.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


# ------------------------------------------------------------------ POST END


#  -----------------------------------------------  GET START
@app.route("/comment/main", methods=["GET"])
def maincomment_get():
    maincomment_list = list(db.mainfan.find({}, {'_id': False}))
    return jsonify({'maincomments': maincomment_list})


@app.route("/comment/oong", methods=["GET"])
def oongcomment_get():
    oongcomment_list = list(db.oongfan.find({}, {'_id': False}))
    return jsonify({'oongcomments': oongcomment_list})


@app.route("/comment/song", methods=["GET"])
def songcomment_get():
    songcomment_list = list(db.songfan.find({}, {'_id': False}))
    return jsonify({'songcomments': songcomment_list})


@app.route("/comment/sol", methods=["GET"])
def solcomment_get():
    solcomment_list = list(db.solfan.find({}, {'_id': False}))
    return jsonify({'solcomments': solcomment_list})


@app.route("/comment/chan", methods=["GET"])
def chancomment_get():
    chancomment_list = list(db.chanfan.find({}, {'_id': False}))
    return jsonify({'chancomments': chancomment_list})


@app.route("/comment/hong", methods=["GET"])
def hongcomment_get():
    hongcomment_list = list(db.hongfan.find({}, {'_id': False}))
    return jsonify({'hongcomments': hongcomment_list})

# ------------------------------- GET END


# ------------------------------------- LIKES ---------------------------------------------
@app.route('/like9', methods=['POST'])
def update_like_cnt9():
    like = db.likes.find_one({'name': '메인'})['likes']
    print(like)

    db.likes.update_one({'name': '메인'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '메인'})['likes']

    return jsonify({'name': '메인', 'like': like})


@app.route('/like9', methods=['GET'])
def get_like_cnt9():
    like = db.likes.find_one({'name': '메인'})['likes']
    print(like)

    return jsonify({'name': '메인', 'like': like})


@app.route('/like1', methods=['POST'])
def update_like_cnt1():
    like = db.likes.find_one({'name': '김태웅'})['likes']
    print(like)

    db.likes.update_one({'name': '김태웅'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '김태웅'})['likes']

    return jsonify({'name': '김태웅', 'like': like})


@app.route('/like1', methods=['GET'])
def get_like_cnt1():
    like = db.likes.find_one({'name': '김태웅'})['likes']
    print(like)

    return jsonify({'name': '김태웅', 'like': like})


@app.route('/like2', methods=['POST'])
def update_like_cnt2():
    like = db.likes.find_one({'name': '김송미'})['likes']
    print(like)

    db.likes.update_one({'name': '김송미'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '김송미'})['likes']

    return jsonify({'name': '김송미', 'like': like})


@app.route('/like2', methods=['GET'])
def get_like_cnt2():
    like = db.likes.find_one({'name': '김송미'})['likes']
    print(like)

    return jsonify({'name': '김송미', 'like': like})


@app.route('/like3', methods=['POST'])
def update_like_cnt3():
    like = db.likes.find_one({'name': '이솔'})['likes']
    print(like)

    db.likes.update_one({'name': '이솔'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '이솔'})['likes']

    return jsonify({'name': '이솔', 'like': like})


@app.route('/like3', methods=['GET'])
def get_like_cnt3():
    like = db.likes.find_one({'name': '이솔'})['likes']
    print(like)

    return jsonify({'name': '이솔', 'like': like})


@app.route('/like4', methods=['POST'])
def update_like_cnt4():
    like = db.likes.find_one({'name': '박찬환'})['likes']
    print(like)

    db.likes.update_one({'name': '박찬환'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '박찬환'})['likes']

    return jsonify({'name': '박찬환', 'like': like})


@app.route('/like4', methods=['GET'])
def get_like_cnt4():
    like = db.likes.find_one({'name': '박찬환'})['likes']
    print(like)

    return jsonify({'name': '박찬환', 'like': like})


@app.route('/like5', methods=['POST'])
def update_like_cnt5():
    like = db.likes.find_one({'name': '홍승엽'})['likes']
    print(like)

    db.likes.update_one({'name': '홍승엽'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '홍승엽'})['likes']

    return jsonify({'name': '홍승엽', 'like': like})


@app.route('/like5', methods=['GET'])
def get_like_cnt5():
    like = db.likes.find_one({'name': '홍승엽'})['likes']
    print(like)

    return jsonify({'name': '홍승엽', 'like': like})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
