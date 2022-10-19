"""A factory module to get predictor class based on type"""

from src.inference.custom_ner_spacy import SpacyNerPredictor
from src.inference.custom_ner_transformers import (
    CustomNerTransformersPredictor,
)


def get_predictor(model_type):
    """A method to retun Predictor class object

    Args:
        model_type (str): Model type

    Returns:
        Predictor: A predictor class
    """
    if model_type is None:
        return None
    elif model_type == "custom_ner_spacy":
        return SpacyNerPredictor()
    elif model_type == "custom_ner_transformers":
        return CustomNerTransformersPredictor()
