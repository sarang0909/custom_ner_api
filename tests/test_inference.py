"""
Module for functional test cases of inference code
"""

from pathlib import Path
from src.utility.utils import config
from src.utility import constants
from src.inference.predictor import Predictor

'''
class TestPredictor:
    """Test class for unit test cases of Predictor."""

    def test_model_files_exist(self):
        """Tests if model files are present."""

        path = Path(config.get(constants.MODELS_DIR)) / config.get(
            constants.MODEL_FILE
        )

        assert path.is_file()

    def test_model_output(self):
        """Tests model output."""

        assert isinstance(Predictor.get_model_output("input"), str)
'''