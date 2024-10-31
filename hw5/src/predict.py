import pickle


def load():
    model_loc = "../model/model1.bin"
    dict_vec_loc = "../model/dv.bin"

    with open(model_loc, 'rb') as m_fh:
        model = pickle.load(m_fh)

    with open(dict_vec_loc, 'rb') as dv_fh:
        dict_vec = pickle.load(dv_fh)

    return model, dict_vec


def predict(customer):

    model, dv =  load()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]

    print(y_pred)


if __name__ == '__main__':
    c = {"job": "management", "duration": 400, "poutcome": "success"}
    predict(c)