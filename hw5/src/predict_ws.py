import pickle

from flask import Flask, request, jsonify

app = Flask("ScoreService")

def load():
    model_loc = "model1.bin"
    dict_vec_loc = "dv.bin"

    with open(model_loc, 'rb') as m_fh:
        model = pickle.load(m_fh)

    with open(dict_vec_loc, 'rb') as dv_fh:
        dict_vec = pickle.load(dv_fh)

    return model, dict_vec

@app.route("/score", methods=["POST"])
def execute():

    customer = request.get_json()
    model, dv =  load()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]

    response = {
        'predicted_score': float(y_pred)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9696)