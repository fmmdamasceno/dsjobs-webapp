from numpy import min_scalar_type
import streamlit as st
from streamlit.elements.alert import AlertMixin
import json

from client.gcloud import GCloud
from feature_map import *

st.title("Data Science Jobs Prediction")
st.markdown("Este é um Data App... ")
st.markdown("Desenvolvido pelos alunos: Andrea Monicque, Francisco Marcelo, Giovana de Lucca, Lucas Pereira e Marcos Wenneton " \
            "para a discplina de Ciência dos Dados para Negócios do curso de Pós-Graduação "\
            "em Ciência de Dados da Universidade do Estado do Amazonas - UEA.")

identifier = st.text_input(
  "Indentifier",
  key="id"
)

gender = st.selectbox(
  "Gender",
  gender_map.keys(),
  key="gender")

enrolled_university = st.selectbox(
  "Enrolled university",
  enrolled_university_map.keys(),
  key="enrolled_university")

education_level = st.selectbox(
  "Education level",
  education_level_map.keys(),
  key="education_level")

major_discipline = st.selectbox(
  "Major discipline",
  major_map.keys(),
  key="major_discipline")

experience = st.selectbox(
  "Experience (years)",
  experience_map.keys(),
  key="experience"
)

company_size = st.selectbox(
  "Company Size",
  company_size_map.keys(),
  key="company_size"
)

company_type = st.selectbox(
  "Company Type",
  company_type_map.keys(),
  key="company_type"
)

last_new_job = st.selectbox(
  "Last new job",
  last_new_job_map.keys(),
  key="last_new_job"
)

relevent_experience = st.selectbox(
  "Relevent experience",
  relevent_experience_map.keys(),
  key="relevent_experience"
)

training_hours = st.number_input(
  "Training hours",
  key="training_hours",
  min_value=0,
  max_value=1000
)

status = {
  "Looking for Job": True,
  "Not Looking for Job": False
}

btn_predict = st.button("Prediction")



def show_results(response):
  status = response["status"]
  print(f'This person is: {status}')
  if status == "Looking for Job":
    st.error(f'This person is {status}')
  elif status == "Not Looking for Job":
    st.success(f'This person is {status}')


if btn_predict:
  gcloud = GCloud()

  data = {
      "id": identifier,
      "gender": gender,
      "enrolled_university": enrolled_university,
      "education_level": education_level,
      "major_discipline": major_discipline,
      "experience": experience,
      "company_size": company_size,
      "company_type": company_type,
      "last_new_job": last_new_job,
      "relevent_experience": relevent_experience,
      "training_hours": training_hours,
  }

  try: 
    response = gcloud.predict(data)
    show_results(response)
  except Exception as e:
    print("Exception: ", e)
