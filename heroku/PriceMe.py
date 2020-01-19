from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from model import predict
import plotly
import plotly.graph_objs as go
import json
# HEROKU!!!

app = Flask(__name__ ,template_folder="./")

@app.route("/", methods = ["GET", "POST"]) # Povolíme metody GET a POST
def PriceMe():
    subm = request.args.get('subm')
    hobby = request.args.get('hobby')
    hobby = "No" if hobby is None or hobby is '' else hobby

    employed = request.args.get('employed')
    employed = "Independent" if employed is None or employed is '' else employed

    student = request.args.get('student')
    student = "No" if student is None or student is '' else student

    education = request.args.get('education')
    education = "basic" if education is None or education is '' else education

    majorStud = request.args.get('majorStud')
    majorStud = "no_major" if majorStud is None or majorStud is '' else majorStud

    company = request.args.get('company')
    company = "1_19" if company is None or company is '' else company

    devType1 = request.args.get('devType1')
    devType2 = request.args.get('devType2')
    devType3 = request.args.get('devType3')
    devType4 = request.args.get('devType4')
    devType5 = request.args.get('devType5')
    devType6 = request.args.get('devType6')
    devType7 = request.args.get('devType7')
    devType8 = request.args.get('devType8')
    devType9 = request.args.get('devType9')
    devType10 = request.args.get('devType10')
    devType11 = request.args.get('devType11')
    devType12 = request.args.get('devType12')
    devType13 = request.args.get('devType13')
    devType14 = request.args.get('devType14')
    devType15 = request.args.get('devType15')
    devType16 = request.args.get('devType16')
    devType17 = request.args.get('devType17')

    devType1 = 0 if devType1 is None or devType1 is '' else 1
    devType2 = 0 if devType2 is None or devType2 is '' else 1
    devType3 = 0 if devType3 is None or devType3 is '' else 1
    devType4 = 0 if devType4 is None or devType4 is '' else 1
    devType5 = 0 if devType5 is None or devType5 is '' else 1
    devType6 = 0 if devType6 is None or devType6 is '' else 1
    devType7 = 0 if devType7 is None or devType7 is '' else 1
    devType8 = 0 if devType8 is None or devType8 is '' else 1
    devType9 = 0 if devType9 is None or devType9 is '' else 1
    devType10 = 0 if devType10 is None or devType10 is '' else 1
    devType11 = 0 if devType11 is None or devType11 is '' else 1
    devType12 = 0 if devType12 is None or devType12 is '' else 1
    devType13 = 0 if devType13 is None or devType13 is '' else 1
    devType14 = 0 if devType14 is None or devType14 is '' else 1
    devType15 = 0 if devType15 is None or devType15 is '' else 1
    devType16 = 0 if devType16 is None or devType16 is '' else 1
    devType17 = 0 if devType17 is None or devType17 is '' else 1

    coded = request.args.get('coded')
    if coded is not None and coded is not '':
        coded = int(coded)
        if coded < 1:
            coded = 0
        if coded > 50:
            coded = 50
    else:
        coded = 0

    codedPro = request.args.get('codedPro')
    if codedPro is not None and codedPro is not '':
        codedPro = int(codedPro)
        if codedPro < 1:
            codedPro = 0
        if codedPro > 50:
            codedPro = 50
    else:
        codedPro = 0

    CarSatis = request.args.get('CarSatis')
    CarSatis = 0 if CarSatis is None or CarSatis is '' else CarSatis

    JobeSeeking = request.args.get('JobeSeeking')
    JobeSeeking = "nointerest" if JobeSeeking is None or JobeSeeking is '' else JobeSeeking


    OS = request.args.get('OS')

    OS = "Windows" if OS is None or OS is '' else OS

    age = request.args.get('age')
    age = int(age) if age is not None and age is not '' else 18

    gender = request.args.get('gender')
    gender = "Man" if gender is None or gender is '' else gender

    dependents = request.args.get('dependents')
    dependents = "No" if dependents is None or dependents is '' else dependents

    laguages1 = request.args.get('laguages1')
    laguages2 = request.args.get('laguages2')
    laguages3 = request.args.get('laguages3')
    laguages4 = request.args.get('laguages4')
    laguages5 = request.args.get('laguages5')
    laguages6 = request.args.get('laguages6')
    laguages7 = request.args.get('laguages7')
    laguages8 = request.args.get('laguages8')
    laguages9 = request.args.get('laguages9')
    laguages10 = request.args.get('laguages10')
    laguages11 = request.args.get('laguages11')

    laguages1 = 0 if laguages1 is None or laguages1 is '' else 1
    laguages2 = 0 if laguages2 is None or laguages2 is '' else 1
    laguages3 = 0 if laguages3 is None or laguages6 is '' else 1
    laguages4 = 0 if laguages4 is None or laguages4 is '' else 1
    laguages5 = 0 if laguages5 is None or laguages5 is '' else 1
    laguages6 = 0 if laguages6 is None or laguages6 is '' else 1
    laguages7 = 0 if laguages7 is None or laguages7 is '' else 1
    laguages8 = 0 if laguages8 is None or laguages8 is '' else 1
    laguages9 = 0 if laguages9 is None or laguages9 is '' else 1
    laguages10 = 0 if laguages10 is None or laguages10 is '' else 1
    laguages11 = 0 if laguages11 is None or laguages11 is '' else 1

    database1 = request.args.get('database1')
    database2 = request.args.get('database2')
    database3 = request.args.get('database3')

    database1 = 0 if database1 is None or database1 is '' else 1
    database2 = 0 if database2 is None or database2 is '' else 1
    database3 = 0 if database3 is None or database3 is '' else 1

    platforms1 = request.args.get('platforms1')
    platforms2 = request.args.get('platforms2')
    platforms3 = request.args.get('platforms3')
    platforms4 = request.args.get('platforms4')
    platforms5 = request.args.get('platforms5')
    platforms6 = request.args.get('platforms6')
    platforms7 = request.args.get('platforms7')
    platforms8 = request.args.get('platforms8')
    platforms1 = 0 if platforms1 is None or platforms1 is '' else 1
    platforms2 = 0 if platforms2 is None or platforms2 is '' else 1
    platforms3 = 0 if platforms3 is None or platforms3 is '' else 1
    platforms4 = 0 if platforms4 is None or platforms4 is '' else 1
    platforms5 = 0 if platforms5 is None or platforms5 is '' else 1
    platforms6 = 0 if platforms6 is None or platforms6 is '' else 1
    platforms7 = 0 if platforms7 is None or platforms7 is '' else 1
    platforms8 = 0 if platforms8 is None or platforms8 is '' else 1

    frameworks1 = request.args.get('frameworks1')
    frameworks2 = request.args.get('frameworks2')
    frameworks3 = request.args.get('frameworks3')
    frameworks4 = request.args.get('frameworks4')

    frameworks1 = 0 if frameworks1 is None or frameworks1 is '' else 1
    frameworks2 = 0 if frameworks2 is None or frameworks2 is '' else 1
    frameworks3 = 0 if frameworks3 is None or frameworks3 is '' else 1
    frameworks4 = 0 if frameworks4 is None or frameworks4 is '' else 1

    country = request.args.get('country')
    country = "Czech Republic" if country is None or country is '' else country
    '''lam = lambda x: np.array(x) if isinstance(x, np.ndarray) else np.array([x])'''

    if subm == "Send":


        df = pd.DataFrame({'Code as a hobby': hobby,
                           'Employment': [employed],
                           'Student': student,
                           'Highest Education level': education,
                           'Undergrad Major': majorStud,
                           'Organization Size': company,
                           'Years Coding': coded,
                           'Years Coding professional': codedPro,
                           'Career Satisfaction': CarSatis,
                           'Job Seek': JobeSeeking,
                           'Operating system': OS,
                           'Age': age,
                           'Gender': gender,
                           'Dependants': dependents,
                           'dev_back': devType1,
                           'dev_front': devType2,
                           'dev_full': devType3,
                           'desktop': devType4,
                           'mobile': devType5,
                           'em_app': devType6,
                           'academic': devType7,
                           'database': devType8,
                           'dev_ops': devType9,
                           'system_admin': devType10,
                           'dev_game': devType11,
                           'dev_test': devType12,
                           'design': devType13,
                           'eng_man': devType14,
                           'business': devType15,
                           'ml': devType16,
                           'product': devType17,
                           'Web_Framework': frameworks1,
                           'Big_Data_Framework': frameworks2,
                           'App_Framework': frameworks3,
                           'ML_Framework': frameworks4,
                           'Relational_DB': database1,
                           'NoSQL_DB': database2,
                           'Multi-model_DB': database3,
                           'Java/JavaScript': laguages1,
                           'Python': laguages2,
                           'HTML/CSS': laguages3,
                           'C/C++/C#/Objective-C': laguages4,
                           'R': laguages5,
                           'SQL': laguages6,
                           'PHP': laguages7,
                           'TypeScript': laguages8,
                           'Swift': laguages9,
                           'Bash': laguages10,
                           'Other': laguages11,
                           'Linux': platforms1,
                           'Singleboard_Computers': platforms2,
                           'Cloud_Technologies': platforms3,
                           'MacOS': platforms4,
                           'iOS': platforms5,
                           'Android': platforms6,
                           'WordPress': platforms7,
                           'Windows': platforms8},
                          columns=['Code as a hobby', 'Employment', 'Student', 'Highest Education level',
                                   'Undergrad Major',
                                   'Organization Size', 'Years Coding', 'Years Coding professional',
                                   'Career Satisfaction',
                                   'Job Seek', 'Operating system', 'Age', 'Gender', 'Dependants', 'dev_back',
                                   'dev_front',
                                   'dev_full', 'desktop', 'mobile', 'em_app', 'academic', 'database', 'dev_ops',
                                   'system_admin',
                                   'dev_game', 'dev_test', 'design', 'eng_man', 'business', 'ml', 'product',
                                   'Web_Framework',
                                   'Big_Data_Framework', 'App_Framework', 'ML_Framework', 'Relational_DB', 'NoSQL_DB',
                                   'Multi-model_DB', 'Java/JavaScript', 'Python', 'HTML/CSS', 'C/C++/C#/Objective-C',
                                   'R', 'SQL',
                                   'PHP', 'TypeScript', 'Swift', 'Bash', 'Other', 'Linux', 'Singleboard_Computers',
                                   'Cloud_Technologies', 'MacOS', 'iOS', 'Android', 'WordPress', 'Windows'], index=[0])



        y_predict = predict(df, country)


        df = pd.read_csv('./data/salary_final.csv', sep=';')
        data = df.Salary
        data = data[~np.isnan(data)]/12
        y, be = np.histogram(data, bins=100)
        bc = be[0:-1] + (be[1:] - be[0:-1]) / 2

        index = 0
        for i in range(len(be)):
            if y_predict <= be[i + 1] and y_predict > be[i]:
                index = i
                break

        color = len(y)*["rgba(58,200,225,0.8)"]
        color[index] = "rgba(222,45,38,1)"
        if y[index] < 5000:
            y[index] = 5000

        data = [ go.Bar(
                    x=bc,
                    y=y,
                    marker=dict(
                        color=color), ) ]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template("result_price_me.html", plot = graphJSON, vysledek = np.floor(y_predict[0]/12) ) # Vrátíme naší šablonu s výsledkem

    else:
        return render_template("price_me.html", vysledek="Fill the questioneer!")  # Vrátíme naší šablonu s výsledkem


if __name__ == "__main__":
    app.run(debug=False)
