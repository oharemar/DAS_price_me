import pandas as pd
import pickle


# ### Example of prediction:
#df ... filled form
#country ... selected country
def predict(input_array, country):
    model = pickle.load(open("model_price_me.dat", "rb"))
    y_pred_norm = model.predict(input_array)
    coef = pd.read_csv('data/country_coefficients.csv', sep=';', index_col=0)
    country_coef = float(coef.loc[country].values)
    y_pred = y_pred_norm*country_coef
    return y_pred

'''
df = pd.DataFrame({'Code as a hobby': 'No',
 'Employment': ['Employed full-time'],
 'Student': 'No',
 'Highest Education level':'bachelor',
 'Undergrad Major': 'IT',
 'Organization Size': '5000_',
 'Years Coding': 10,
 'Years Coding professional': 10,
 'Career Satisfaction': 0.8,
 'Job Seek': 'open',
 'Operating system': 'MacOS',
 'Age': 20,
 'Gender': 'Man',
 'Dependants': 'No',
 'dev_back': 1,
 'dev_front': 1,
 'dev_full': 1,
 'desktop': 1,
 'mobile': 1,
 'em_app': 1,
 'academic': 1,
 'database': 1,
 'dev_ops': 1,
 'system_admin': 1,
 'dev_game': 1,
 'dev_test': 1,
 'design': 1,
 'eng_man': 1,
 'business': 1,
 'ml': 1,
 'product': 1,
 'Web_Framework': 1,
 'Big_Data_Framework': 1,
 'App_Framework': 1,
 'ML_Framework': 1,
 'Relational_DB': 1,
 'NoSQL_DB': 1,
 'Multi-model_DB': 1,
 'Java/JavaScript': 1,
 'Python': 1,
 'HTML/CSS': 1,
 'C/C++/C#/Objective-C': 1,
 'R': 1,
 'SQL': 1,
 'PHP': 1,
 'TypeScript': 1,
 'Swift': 1,
 'Bash': 1,
 'Other': 1,
 'Linux': 1,
 'Singleboard_Computers': 1,
 'Cloud_Technologies': 1,
 'MacOS': 1,
 'iOS': 1,
 'Android': 1,
 'WordPress': 1,
 'Windows': 1}, columns=['Code as a hobby', 'Employment', 'Student', 'Highest Education level', 'Undergrad Major',
                         'Organization Size', 'Years Coding', 'Years Coding professional', 'Career Satisfaction',
                         'Job Seek', 'Operating system', 'Age', 'Gender', 'Dependants', 'dev_back', 'dev_front',
                         'dev_full', 'desktop', 'mobile', 'em_app', 'academic', 'database', 'dev_ops', 'system_admin',
                         'dev_game', 'dev_test', 'design', 'eng_man', 'business', 'ml', 'product', 'Web_Framework',
                         'Big_Data_Framework', 'App_Framework', 'ML_Framework', 'Relational_DB', 'NoSQL_DB',
                         'Multi-model_DB', 'Java/JavaScript', 'Python', 'HTML/CSS', 'C/C++/C#/Objective-C', 'R', 'SQL',
                         'PHP', 'TypeScript', 'Swift', 'Bash', 'Other', 'Linux', 'Singleboard_Computers',
                         'Cloud_Technologies', 'MacOS', 'iOS', 'Android', 'WordPress', 'Windows'], index=[0])

country = 'Iceland'



print(predict(df, country))
'''
