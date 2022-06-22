from flask import Flask, Response, render_template, request
from flask_cors import CORS, cross_origin

from predictFromModel import prediction
from trainingModel import trainModel
from training_Validation_Insertion import train_validation

app = Flask(__name__)
CORS(app)


@app.route("/", methods = [ "GET" ])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods = [ 'POST' ])
@cross_origin()
def trainRouteClient():
    try:
        if request.json[ "filepath" ] is not None:
            path = request.json[ "filepath" ]
            train_valObj = train_validation(path)  # object initialization
            train_valObj.train_validation()  # calling the train_validation function

            trainModelObj = trainModel()  # Object initialization
            trainModelObj.trainingModel()  # training the model for the files in the table
    except ValueError:
        return Response("Error Occurred! ::" + str(ValueError))
    except KeyError:
        return Response("Error Occurred! ::" + str(KeyError))
    except Exception as e:
        return Response("Error Occurred! Error::" + str(e))
    return Response("Training Successfull!!")


@app.route("/predict", methods = [ 'POST' ])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            if request.form:
                data_req = dict(request.form)
                data = data_req.values()
                data = [ list(data) ]
                pred = prediction(data)

                # predicting the output
                result = pred.predictionFromModel()
                if result == 1:
                    result = "Yes"
                else:
                    result = "No"
                return render_template('result.html', result = result)
            else:
                return ""
        except Exception as e:
            error = {'error': e}
            return render_template('404.html', error = error)
    else:
        return render_template('404.html', error = "Something went wrong!! Try again.")


if __name__ == "__main__":
    app.run(debug = True)
