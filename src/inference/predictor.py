"""A Predictor abstract module to load models and get their predictions.

"""
from abc import ABC, abstractmethod


class Predictor(ABC):
    """
    This is an abstract class for model load and prediction methods.

    """

    @abstractmethod
    def get_model(self):
        """An abstract method to get and load  model"""

    @abstractmethod
    def get_model_output(self, input_data):
        """An abstract method to get model output

        Args:
            input_data (str): Input text data to model
        """
