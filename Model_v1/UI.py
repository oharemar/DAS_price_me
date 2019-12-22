from flask import Flask, render_template, request
import numpy as np
from model import predict
# HEROKU!!!

app = Flask(__name__ ,template_folder="c:/users/femat/documents/skola/das/price_me/DAS_price_me/Model_v1")

@app.route("/", methods = ["GET", "POST"]) # Povolíme metody GET a POST
def PriceMe():
    subm = request.args.get('subm');
    hobby = request.args.get('hobby');
    hobby = 0 if hobby is None or hobby is '' else int(hobby);

    employed = request.args.get('employed ');
    employed = 0 if employed is None or employed is '' else int(employed);

    education = [0, 0, 0, 0, 0, 0, 0];
    educationRes = request.args.get('education');
    if educationRes is not None and educationRes is not '':
        education[int(educationRes)] = 1;

    company = [0, 0, 0, 0, 0];
    companyRes = request.args.get('company');
    if companyRes is not None and companyRes is not '':
        company[int(companyRes)] = 1;

    coded = request.args.get('coded');
    if coded is not None and coded is not '':
        coded = int(coded);
        if coded < 1:
            coded = 0;
        if coded > 50:
            coded = 50;
    else:
        coded = 0;

    codedPro = request.args.get('codedPro');
    if codedPro is not None and codedPro is not '':
        codedPro = int(codedPro);
        if codedPro < 1:
            codedPro = 0;
        if codedPro > 50:
            codedPro = 50;
    else:
        codedPro = 0;

    JobeSeeking = [0, 0, 0];
    JobeSeekingPro = request.args.get('JobeSeeking');
    if JobeSeekingPro is not None and JobeSeekingPro is not '':
        JobeSeeking[int(JobeSeekingPro)] = 1;

    platform1 = request.args.get('platform1');
    platform2 = request.args.get('platform2');
    platform3 = request.args.get('platform3');
    platform4 = request.args.get('platform4');

    platform1 = 0 if platform1 is None or platform1 is '' else 1;
    platform2 = 0 if platform2 is None or platform2 is '' else 1;
    platform3 = 0 if platform3 is None or platform3 is '' else 1;
    platform4 = 0 if platform4 is None or platform4 is '' else 1;

    age = request.args.get('age');
    age = int(age) if age is not None and age is not '' else 0;

    gender = request.args.get('gender');
    gender = 0 if gender is None or gender is '' else int(gender);

    dependents = request.args.get('dependents');
    dependents = 0 if dependents is None or dependents is '' else int(dependents);

    student = request.args.get('student');
    student = 0 if student is None or student is '' else int(student);

    lam = lambda x: np.array(x) if isinstance(x, np.ndarray) else np.array([x])

    if subm == "Send":
        result = [hobby, employed,np.array(education), np.array(company), coded, codedPro, np.array(JobeSeeking), platform1, platform2, platform3, platform4, age, gender, dependents,student];
        result = np.hstack(list(map(lam, result)))

        if result is not None:
            y_predict = predict(result);
        print(y_predict)

        return render_template("result_price_me.html", vysledek = y_predict[0] )#y_predict[0]) # Vrátíme naší šablonu s výsledkem
    else:
        return render_template("price_me.html", vysledek="Fill the questioneer!")  # Vrátíme naší šablonu s výsledkem

if __name__ == "__main__":
    app.run(debug=False)