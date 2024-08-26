import pandas as pd
import streamlit as st
import re, html

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True



tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

st.title("Welcome to APS Jaipur")
st.subheader("Check your Stress level")

df = pd.read_csv("upload.csv", na_values=['NAN']) 


if 'stresslevel' not in st.session_state:
    st.session_state.stresslevel = ''



with st.form('stress'):
    Gender = st.selectbox('Gender', ['Male ','Female'])

    Financial_Issues = st.selectbox('Financial_Issues', ['None','Repay Loan Issues;Deadline of Fee payment','Payment for Hostel','Repay Loan Issues','Deadline of Fee payment','Deadline of Fee payment;Payment for Hostel','Repay Loan Issues;Deadline of Fee payment;Payment for Hostel','Payment for room rent','Family loan','Repay Loan Issues;Payment for Hostel'])

    Family_Issues = st.selectbox('Family_Issues', ['None','Parental Expectations','Parental Expectations;Poor Communication and misunderstandings','Parental Expectations;Being bullied by siblings','Poor Communication and misunderstandings','Parental Expectations;Poor Communication and misunderstandings;Negligence of Children','Parental Expectations;Internal family dispute','Poor Communication and misunderstandings;Negligence of Children','Parental Expectations;Negligence of Children','Negligence of Children','Parental Expectations;Divorce of Parents','Being bullied by siblings','Divorce of Parents;Poor Communication and misunderstandings','Being bullied by siblings;Divorce of Parents;Poor Communication and misunderstandings','Parental Expectations;Being bullied by siblings;Divorce of Parents','Divorce of Parents;Negligence of Children','Divorce of Parents;Poor Communication and misunderstandings;Negligence of Children','Being bullied by siblings;Poor Communication and misunderstandings;Negligence of Children','Parental Expectations;Divorce of Parents;Negligence of Children','NoParental Expectations;Being bullied by siblings;Poor Communication and misunderstandingsne','Being bullied by siblings;Poor Communication and misunderstandings','Being bullied by siblings;Negligence of Children','Being bullied by siblings;Divorce of Parents;Negligence of Children','Parental Expectations;Divorce of Parents;Poor Communication and misunderstandings','Parental Expectations;Being bullied by siblings;Divorce of Parents;Negligence of Children','Parental Expectations;Being bullied by siblings;Negligence of Children','Being bullied by siblings;Divorce of Parents','Parental Expectations;Being bullied by siblings;Divorce of Parents;Poor Communication and misunderstandings;Negligence of Children','Parental Expectations;Being bullied by siblings;Divorce of Parents;Poor Communication and misunderstandings','Divorce of Parents','Internal family dispute','Poor Communication'])

    Study_Hours = st.slider('Study Hours', 1, 10)
			 
    Health_Issues = st.selectbox('Health_Issues', ['None','Anxiety or Tension','Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Sleeping Problem;Concentration Problem','Concentration Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Anxiety or Tension;Lonliness;Sleeping Problem;Concentration Problem','Anxiety or Tension;Sleeping Problem','Sinus or Migraine or Headaches;Low Energy;Anxiety or Tension;Lonliness;Concentration Problem','Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Concentration Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Low Energy;Lonliness;Sleeping Problem;Concentration Problem','Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Lonliness;Sleeping Problem;Concentration Problem','Insomnia (Sleep Deprivation);Anxiety or Tension;Sleeping Problem','Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Lonliness','Sinus or Migraine or Headaches;Anxiety or Tension;Sleeping Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Anxiety or Tension','Sinus or Migraine or Headaches;Covid;Low Energy;Sleeping Problem','Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Low Energy','Malnutrition;Covid;Anxiety or Tension','Sinus or Migraine or Headaches;Anxiety or Tension','Malnutrition;Insomnia (Sleep Deprivation)','Covid;Anxiety or Tension;Concentration Problem','Insomnia (Sleep Deprivation);Anxiety or Tension;Lonliness','Insomnia (Sleep Deprivation);Anxiety or Tension','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation)','Insomnia (Sleep Deprivation);Lonliness','Insomnia (Sleep Deprivation);Anxiety or Tension;Concentration Problem','Covid;Low Energy;Lonliness','Malnutrition','Sinus or Migraine or Headaches;Low Energy;Lonliness','Malnutrition;Low Energy;Sleeping Problem','Covid;Anxiety or Tension','Sinus or Migraine or Headaches;Low Energy','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Sleeping Problem','Covid;Concentration Problem','Low Energy;Sleeping Problem','Sleeping Problem','Malnutrition;Sinus or Migraine or Headaches;Covid','Covid;Low Energy;Sleeping Problem','Covid;Anxiety or Tension;Sleeping Problem','Covid;Insomnia (Sleep Deprivation);Low Energy','Covid;Low Energy;Concentration Problem','Malnutrition;Anxiety or Tension;Sleeping Problem','Malnutrition;Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension','Malnutrition;Insomnia (Sleep Deprivation);Lonliness;Concentration Problem','Malnutrition;Covid;Lonliness','Malnutrition;Insomnia (Sleep Deprivation);Lonliness','Covid;Lonliness','Malnutrition;Insomnia (Sleep Deprivation);Sleeping Problem','Anxiety or Tension;Lonliness;Concentration Problem','Lonliness','Anxiety or Tension;Lonliness;Sleeping Problem;Concentration Problem','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Low Energy;Lonliness;Sleeping Problem;Concentration Problem','Insomnia (Sleep Deprivation);Anxiety or Tension;Lonliness;Concentration Problem','Covid;Insomnia (Sleep Deprivation);Anxiety or Tension;Sleeping Problem;Concentration Problem','Covid;Insomnia (Sleep Deprivation);Anxiety or Tension;Sleeping Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Anxiety or Tension;Sleeping Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Sleeping Problem','Low Energy;Lonliness','Sinus or Migraine or Headaches;Low Energy;Anxiety or Tension','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Lonliness','Insomnia (Sleep Deprivation);Low Energy','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Anxiety or Tension;Lonliness;Sleeping Problem;Concentration Problem','Malnutrition;Covid;Low Energy','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Lonliness;Concentration Problem','Covid;Low Energy;Anxiety or Tension','Covid;Insomnia (Sleep Deprivation);Low Energy;Sleeping Problem','Low Energy;Lonliness;Sleeping Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Low Energy;Sleeping Problem','Covid;Low Energy;Lonliness;Sleeping Problem','Sinus or Migraine or Headaches;Insomnia (Sleep Deprivation);Low Energy','Malnutrition;Anxiety or Tension','Low Energy;Lonliness;Concentration Problem','Sinus or Migraine or Headaches;Covid;Low Energy;Anxiety or Tension','Covid;Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Lonliness;Sleeping Problem;Concentration Problem','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Concentration Problem','Malnutrition;Insomnia (Sleep Deprivation);Low Energy;Anxiety or Tension;Lonliness','Sinus or Migraine or Headaches;Covid;Insomnia (Sleep Deprivation);Low Energy;Lonliness','Covid;Insomnia (Sleep Deprivation)','Sinus or Migraine or Headaches;Covid;Anxiety or Tension','Covid;Lonliness;Sleeping Problem','Sinus or Migraine or Headaches;Low Energy;Sleeping Problem','Covid;Anxiety or Tension;Lonliness','Sinus or Migraine or Headaches;Lonliness','Sinus or Migraine or Headaches;Covid;Sleeping Problem','Low Energy;Anxiety or Tension;Concentration Problem','Sinus or Migraine or Headaches;Sleeping Problem','Covid;Low Energy;Anxiety or Tension;Sleeping Problem','Insomnia (Sleep Deprivation);Low Energy;Lonliness','Covid;Low Energy;Anxiety or Tension;Concentration Problem','Sinus or Migraine or Headaches','Sleeping Problem;Concentration Problem','Low Energy'])

    Friends_Issues = st.selectbox('Friends_Issues', ['No Issue','Comparison between them','Mistrust','Jealousy;Mistrust','Betrayal','Comparison between them;Jealousy','Conflicts','Conflicts;Comparison between them;Betrayal','Jealousy','Comparison between them;Mistrust','Conflicts;Comparison between them;Jealousy','Conflicts;Comparison between them;Mistrust','Comparison between them;lack of deep communication','friendly','Jealousy;Betrayal','Conflicts;Jealousy','Conflicts;Comparison between them','Comparison between them;Jealousy;Mistrust','Conflicts;Jealousy;Betrayal','Comparison between them;Betrayale','Mistrust;Betrayal','Conflicts;Comparison between them;Jealousy;Mistrust;Betrayal','Jealousy;Mistrust;Betrayal','Conflicts;Mistrust','Comparison between them;Jealousy;Betrayal','Comparison between them;Mistrust;Betrayal','Conflicts;Jealousy;Mistrust','Comparison between them;Jealousy;Mistrust;Betrayal','Conflicts;Jealousy;Mistrust;Betrayal'])

    Friends_Time = st.slider('Friends Time', 1, 10)

    Overload = st.selectbox('Feel Overload', ['No','Yes'])

    Unpleasant = st.selectbox('Unpleasant', ['No ','Yes'])

    Academic = st.selectbox('Academic Load', ['No','Yes'])

    Career = st.selectbox('Career Confusion', ['No','Yes'])

    Criticism = st.selectbox('Criticism', ['No','Yes'])
     
    Conflicts = st.selectbox('Conflicts', ['No','Yes'])

    submit = st.form_submit_button('Check It', on_click=click_button)

# The value of st.session_state.stresslevel is updated at the end of the script rerun,
# so the displayed value at the top in col2 does not show the new stresslevel. Trigger
# a second rerun when the form is submitted to update the value above.

Gender=Gender.strip()
Financial_Issues=Financial_Issues.strip()
Family_Issues=Family_Issues.strip()
#Study_Hours=Study_Hours.strip()
Health_Issues=Health_Issues.strip()
Friends_Issues=Friends_Issues.strip()
#Friends_Time=Friends_Time.strip()
Overload=Overload.strip()
Unpleasant=Unpleasant.strip()
Academic=Academic.strip()
Career=Career.strip()
Criticism=Criticism.strip()
Conflicts=Conflicts.strip()

col1,col2 = st.columns(2)
col1.title('Stress Level:')

if isinstance(st.session_state.stresslevel, str):
    col2.title(st.session_state.stresslevel)
if submit:
    st.rerun()
    #getstresslevel()
    
i=0
for i in range(213):
    Gender_df=df.loc[i,"Gender"]
    #Gender_df = tag_re.sub('', Gender_df)
    #Gender_df = html.escape(Gender_df)

    Financial_Issues_df=df.loc[i,"financial_issues"]
    #Financial_Issues_df = tag_re.sub('', Financial_Issues_df)
    #Financial_Issues_df = html.escape(Financial_Issues_df)

    Family_Issues_df=df.loc[i,"family_issues"]
    #Family_Issues_df = tag_re.sub('', Family_Issues_df)
    #Family_Issues_df = html.escape(Family_Issues_df)

    Study_Hours_df=df.loc[i,"study_hours"]
    #Study_Hours_df = tag_re.sub('', Study_Hours_df)
    #Study_Hours_df = html.escape(Study_Hours_df)

    Health_Issues_df=df.loc[i,"health_issues"]
    #Health_Issues_df = tag_re.sub('', Health_Issues_df)
    #Health_Issues_df = html.escape(Health_Issues_df)

    Friends_Issues_df=str(df.loc[i,"friends_issues"])
    #Friends_Issues_df = tag_re.sub('', Friends_Issues_df)
    #Friends_Issues_df = html.escape(Friends_Issues_df)

    Friends_Time_df=df.loc[i,"friends_time"]
    #Friends_Time_df = tag_re.sub('', Friends_Time_df)
    #Friends_Time_df = html.escape(Friends_Time_df)

    Overload_df=df.loc[i,"overload"]
    #Overload_df = tag_re.sub('', Overload_df)
    #Overload_df = html.escape(Overload_df)

    Unpleasant_df=df.loc[i,"unpleasant"]
    #Unpleasant_df = tag_re.sub('', Unpleasant_df)
    #Unpleasant_df = html.escape(Unpleasant_df)

    Academic_df=df.loc[i,"academic"]
    #Academic_df = tag_re.sub('', Academic_df)
    #Academic_df = html.escape(Academic_df)

    Career_df=df.loc[i,"career"]
    #Career_df = tag_re.sub('', Career_df)
    #Career_df = html.escape(Career_df)

    Criticism_df=df.loc[i,"criticism"]
    #Criticism_df = tag_re.sub('', Criticism_df)
    #Criticism_df = html.escape(Criticism_df)

    Conflicts_df=df.loc[i,"conflicts"]
    #Conflicts_df = tag_re.sub('', Conflicts_df)
    #Conflicts_df = html.escape(Conflicts_df)

    #st.text(Gender_df); st.text(Gender); st.text(Financial_Issues_df);  st.text(Financial_Issues); st.text(Family_Issues_df); st.text(Family_Issues); st.text(Study_Hours_df);  st.text(Study_Hours); st.text(Health_Issues_df); st.text(Health_Issues); st.text(Friends_Issues_df);  st.text(Friends_Issues); st.text(Friends_Time_df); st.text(Friends_Time); st.text(Overload_df);  st.text(Overload); st.text(Unpleasant_df); st.text(Unpleasant); st.text(Academic_df);  st.text(Academic); st.text(Career_df); st.text(Career); st.text(Criticism_df);  st.text(Criticism); st.text(Conflicts_df);  st.text(Conflicts)
    if Gender==Gender_df and Financial_Issues==Financial_Issues_df and Family_Issues==Family_Issues_df and Study_Hours==Study_Hours_df and Health_Issues==Health_Issues_df and Friends_Issues==Friends_Issues_df and Friends_Time==Friends_Time_df and Overload==Overload_df and Unpleasant==Unpleasant_df and Academic==Academic_df and Career==Career_df and Criticism==Criticism_df and Conflicts==Conflicts_df:
        #st.text(i)
        #st.text("in if")
        st.session_state.stresslevel = df.loc[i,"stress_level"] 
        break
    else:
        #st.text(i)
        #st.text("in else")
        if st.session_state.clicked:
            st.session_state.stresslevel = "Normal"
        else:
            st.session_state.stresslevel = "-------"
    







  
