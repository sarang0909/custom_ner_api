"""A main script to run streamlit application.

"""
import streamlit as st
import streamlit.components.v1 as components
import spacy
import pandas as pd
from src.utility.loggers import logger
from src.inference.predictor_factory import get_predictor

# st.set_page_config(layout="wide")
st.title("Custom Named Entity Recognition")
st.text(
    "Models are trained on small sample of news data to find custom named entities"
)
data = [
    (
        "custom_ner_spacy",
        "Spacy",
        "train spacy for custom NER",
        "CUSTOM_ORG,CUSTOM_PERSON,CUSTOM_PLACE,CUSTOM_ROLE",
    ),
    (
        "custom_ner_transformers",
        "transformers",
        "Finetune DistilBertTokenClassification for custom NER in BILOU format",
        "B-CUSTOM_ORG,I-CUSTOM_ORG,L-CUSTOM_ORG,U-CUSTOM_ORG,"
        "B-CUSTOM_PERSON,I-CUSTOM_PERSON,L-CUSTOM_PERSON,U-CUSTOM_PERSON,"
        "B-CUSTOM_ROLE,I-CUSTOM_ROLE,L-CUSTOM_ROLE,U-CUSTOM_ROLE,"
        "B-CUSTOM_PLACE',I-CUSTOM_PLACE,L-CUSTOM_PLACE,U-CUSTOM_PLACE",
    ),
]
df = pd.DataFrame(
    data, columns=["Model Name", "Library", "Description", "Named Entites"]
)
st.dataframe(df, use_container_width=False)
form = st.form(key="my-form")
input_data = form.text_area("Enter text for NER extraction")

classification_method = form.radio(
    "Choose a NER model",
    (
        "custom_ner_spacy",
        "custom_ner_transformers",
    ),
)
submit = form.form_submit_button("Submit")


if submit:
    try:
        predictor = get_predictor(classification_method)

        output = predictor.get_model_output(input_data)

        ex = [{"text": input_data, "ents": output}]
        st.write("model_selected:", classification_method)

        st.write("model_output:")
        colors = {
            "CUSTOM_ORG": "#BE5525",
            "CUSTOM_PERSON": "#95CFDC",
            "CUSTOM_PLACE": "#55BB6A",
            "CUSTOM_ROLE": "#BE55DE",
            "L-CUSTOM_ORG": "#BE5525",
            "B-CUSTOM_PERSON": "#95CFDC",
            "B-CUSTOM_ROLE": "#BE55DE",
            "U-CUSTOM_PERSON": "#95CFDC",
            "I-CUSTOM_ROLE": "#BE55DE",
            "I-CUSTOM_PLACE": "#55BB6A",
            "U-CUSTOM_PLACE": "#55BB6A",
            "L-CUSTOM_ROLE": "#BE55DE",
            "I-CUSTOM_PERSON": "#95CFDC",
            "U-CUSTOM_ROLE": "#BE55DE",
            "L-CUSTOM_PERSON": "#95CFDC",
            "I-CUSTOM_ORG": "#BE5525",
            "U-CUSTOM_ORG": "#BE5525",
            "L-CUSTOM_PLACE": "#55BB6A",
            "B-CUSTOM_ORG": "#BE5525",
            "B-CUSTOM_PLACE": "#55BB6A",
        }
        options = {"colors": colors}
        components.html(
            spacy.displacy.render(
                ex, style="ent", options=options, manual=True
            )
        )
    except Exception as error:
        message = "Error while creating output"
        logger.error(message, str(error))
