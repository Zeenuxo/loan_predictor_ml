#Importing Packages
import pickle
import streamlit as st

#Loading our ML Model
pickle_in = open('./model/model.pkl', mode = "rb")
load_model = pickle.load(pickle_in)



#Main function to define our app
def main():       
    
    #Front End of web app  
    web_app_html = """ 
    <div style ="background-color:blue;padding:15px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction - Machine Learning App</h1> 
    </div> 
    <br>
    <br>
    """

    #Display Web App
    st.markdown(web_app_html, unsafe_allow_html = True) 




    #Take User input using select-box/dropdown options
    #Convert categorical data to numerical using if else 
    
    #Get name of Client
    name = st.text_input('Please enter your Full Name:')

    #Loan ID - LP001002
    loan_id = st.text_input("Please enter your Loan ID:")

    #Gender
    options = "Male","Female"
    gender = st.selectbox('What is your Gender?', options)

    if gender == "Male":
        gender = 1
    else:
        gender = 0

    #Married
    options = "Yes","No"
    married = st.selectbox('Are you Married?', options) 

    if married == "Yes":
        married = 1
    else:
        married = 0

    #Dependents
    options = "0","1","2","3+"
    dependents = st.selectbox('How many dependents do you have?', options) 

    if dependents == "0":
        dependents = 0
    elif dependents == "1":
        dependents = 1
    elif dependents == "2":
        dependents = 2
    else:
        dependents = 3

    #Education
    options = "Graduate","Not Graduate"
    education = st.selectbox('What is your Education level?', options) 

    if education == "Graduate":
        education = 1
    else:
        education = 0

    #Self Employed
    options = "Yes","No"
    self_employed = st.selectbox('Are you Self Employed?', options) 

    if self_employed == "Yes":
        self_employed = 1
    else:
        self_employed = 0

    #Applicant Income
    app1_income = st.number_input("What is Applicant 1's Monthly Income (£)",value=0)

    #Co-Applicant Income
    app2_income = st.number_input("What is Applicant 2's Monthly Income (£)",value=0)

    #Loan Amount
    amount = st.number_input("How much loan do you need?")

    #Loan Term
    options = "5 years","10 years","15 years","20 years","30 years","40 years"
    term = st.selectbox("What is your preferred loan term?", options)

    if term == "5 years":
        term = 60
    elif term == "10 years":
        term = 120
    elif term == "15 years":
        term = 180
    elif term == "20 years":
        term = 240
    elif term == "30 years":
        term = 360
    else: 
        term = 480


    #Credit History
    options = "Unclear Debts","No Debts"
    credit = st.selectbox("What is the status of your Credit History?", options)

    if credit == "Unclear Debts":
        credit = 0
    else:
        credit = 1


    #Property Area
    options = ("Rural", "Semi-Urban", "Urban")
    prop = st.selectbox("What is your Property Area Type?", options)

    if prop == "Rural":
        prop = 0
    elif prop =="Semi-Urban":
        prop = 1
    else:
        prop = 2





    #Storing input data as features
    features = [[gender, married, dependents, education, self_employed, app1_income, app2_income, amount, term, credit, prop]]
    
    #View all input data incoonsole
    print(features)





    #When Predict button is clicked - Model to make a prediction 
    if st.button("Predict"): 
            result = load_model.predict(features) 

            #View Result in console
            print(result)





    #Result to determine display message: Success or Error
    if result[0] == 1:
        #Get Balloons on screen
        st.balloons()
        st.success(           
            "Congratulations!" + " "*2 + name + "\n\n"  
            "Your loan is Approved. \n\n"
            "Loan ID: " + loan_id 
        )
    else:
        st.error(
            "Rejected" + " "*2 + name + "\n\n"  
            "Your loan is Not Approved. \n\n"
            "Loan ID: " + loan_id 
        )



main()



