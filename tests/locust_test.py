"""
Module for performance test cases
"""

import json
from locust import HttpUser, task


class PerformanceTests(HttpUser):
    """Test class for performance tests"""

    @task(1)
    def test_model_inference(self):
        """A method to test performance of model inference API"""

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        sample = {"data": "I am Elon", "model": "custom_ner_spacy"}
        self.client.post(
            "/model_inference", data=json.dumps(sample), headers=headers
        )
