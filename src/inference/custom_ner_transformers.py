"""A Predictor module to load model and get prediction from custom transformers model.

"""

import spacy
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch
from src.inference.predictor import Predictor


class CustomNerTransformersPredictor(Predictor):
    """A child class to load model and get output

    Args:
        Predictor (Predictor): Parent class

    """

    model = None

    def __init__(self):
        self.id_to_label = {
            0: "B-CUSTOM_PLACE",
            1: "L-CUSTOM_ORG",
            2: "B-CUSTOM_PERSON",
            3: "B-CUSTOM_ROLE",
            4: "U-CUSTOM_PERSON",
            5: "I-CUSTOM_ROLE",
            6: "I-CUSTOM_PLACE",
            7: "U-CUSTOM_PLACE",
            8: "L-CUSTOM_ROLE",
            9: "I-CUSTOM_PERSON",
            10: "U-CUSTOM_ROLE",
            11: "L-CUSTOM_PERSON",
            12: "I-CUSTOM_ORG",
            13: "U-CUSTOM_ORG",
            14: "L-CUSTOM_PLACE",
            15: "B-CUSTOM_ORG",
            16: "O",
        }
        self.tokenizer = AutoTokenizer.from_pretrained(
            "distilbert-base-uncased"
        )
        self.nlp = spacy.load("en_core_web_lg")

    def get_model(self):
        """A method to load model

        Returns:
            model: trained model
        """

        if self.model is None:
            self.model = AutoModelForTokenClassification.from_pretrained(
                "src/models/custom_ner_transformers"
            )
        return self.model

    def get_model_output(self, text):
        """A method to get model output from given text input
        Args:
            text (text):input text data

        Returns:
            output: model prediction
        """
        # get text token from text,since we used spacy tokenizer for training,we'll use same for inference
        spacy_tokens = self.nlp(text)
        text_tokens = [token.text for token in spacy_tokens]
        tokenized_inputs = self.tokenizer(
            text_tokens,
            truncation=True,
            padding="max_length",
            is_split_into_words=True,
            max_length=200,
            return_tensors="pt",
        )
        outputs = self.get_model()(**tokenized_inputs)
        predictions = torch.argmax(outputs.logits.squeeze(), axis=1)
        predictions = [self.id_to_label[int(i)] for i in predictions]
        word_ids = tokenized_inputs.word_ids()
        # create dictionary of token word and it's entity type
        token_entity = {}
        for idx, word in enumerate(text_tokens):
            for id, word_id in enumerate(word_ids):
                if idx == word_id:
                    if word not in token_entity:
                        token_entity[word] = predictions[id]
        # create final output
        output = []
        for token in spacy_tokens:
            # append only if it is valid entity. O means it is not entity
            if token_entity[token.text] != "O":
                output.append(
                    {
                        "start": token.idx,
                        "end": token.idx + len(token.text),
                        "label": token_entity[token.text],
                    }
                )
        return output
