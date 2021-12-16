import streamlit as st
from streamlit.elements.alert import AlertMixin
import json

from client.gcloud import GCloud
from feature_map import *

st.title("Data Science Jobs Prediction")
st.markdown("Este é um Data App... ")
st.markdown("Desenvolvido pelos alunos: Andrea Monicque, Francisco Marcelo, Lucas Pereira e Marcos Wenneton " \
            "para a discplina de Infraestrutura em Nuvem para Projetos com Ciência dos Dados do curso de Pós-Graduação "\
            "em Ciência de Dados da Universidade do Estado do Amazonas - UEA.")

identifier = st.number_input(
  "Indentifier",
  value=1,
  key="id")

gender = st.selectbox(
  "Gender",
  gender_map.keys(),
  key='gender')

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

relevant_experience = st.selectbox(
  "Relevant experience",
  relevant_experience_map.keys(),
  key="relevant_experience"
)

training_hours = st.number_input(
  "Training hours",
  key="training_hours"
)

status = {
  "Looking for Job": "Looking for Job",
  "Not Looking for Job": "Not Looking for Job"
}

btn_predict = st.button("Realizar Previsão")



def show_results(response):
  result = response['status']
  if result == status["Looking for job"]:
    st.error("This person is looking for Job")
  elif result == status["LNot Looking for job"]:
    st.success("This person is not looking for Job")


if btn_predict:
  gcloud = GCloud()

  st_input = {
      "id": str(identifier),
      "gender": gender,
      "enrolled_university": enrolled_university,
      "education_level": education_level,
      "major_discipline": major_discipline,
      "experience": experience,
      "company_size": company_size,
      "company_type": company_type,
      "last_new_job": last_new_job,
      "relevent_experience": relevant_experience,
      "training_hours": str(training_hours)
  }

  data = str.encode(json.dumps(st_input))

  try:
    response = gcloud.predict(data)

    print(response)
    show_results(response)
  except Exception as e:
    print("Exception: ", e)
