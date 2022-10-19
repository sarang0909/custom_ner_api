"""A Predictor module to load model and get prediction from custom spacy model.

"""


import spacy
from src.inference.predictor import Predictor


class SpacyNerPredictor(Predictor):
    """A child class to load model and get output

    Args:
        Predictor (Predictor): Parent class

    """

    model = None

    def get_model(self):
        """A method to load model

        Returns:
            model: trained model
        """

        if self.model is None:
            self.model = spacy.load("src/models/spacy_model")
        return self.model

    def get_model_output(self, input_data):
        """A method to get model output from given text input
        Args:
            input_data (text):input text data

        Returns:
            output: model prediction
        """
        output = []
        doc = self.get_model()(input_data)

        for ent in doc.ents:
            # output.append({"start": ent.start_char, "end": ent.end_char, "text":ent.text, "label": ent.label_})
            output.append(
                {
                    "start": ent.start_char,
                    "end": ent.end_char,
                    "label": ent.label_,
                }
            )
        return output
