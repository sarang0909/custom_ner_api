# custom_ner_api : Production Ready Code


## About  
This is a project developed to create a code template and to understand different Named Entity Recognition(NER) methods for custom entities. This project includes different training notebooks to create different kind of custom NER models. This project also includes a code to make productionaized NER api using standard practices in MLOps.   

### NLP and MLOps techniques to learn/use from this end to end project:
1. collect,clean,annotate text data   
2. implement different methods of NER models    
3. build inference api   
4. create streamlit application    
5. write unit test cases and performance test cases
6. code documentation
7. code formatting 
8. code deployment using docker and circleci



This code can be used for end to end NER project development as well as deployment.  
 
If you are only looking to learn/use model building techniques,directly jump to notebooks:   
1.[Custom NER using Spacy](src/training/spacy_training/custom_ner_spacy.ipynb)    
2.[Custom NER using transformers](src/training/custom_ner_transformers.ipynb)    
3.[Cusstom NER using custom Neural Network using Pytorch](src/training/custom_ner_dl.ipynb)  


The basic code template for this project is derived from my another repo <a href="https://github.com/sarang0909/Code_Template">code template</a> 

The project considers following phases in ML project development lifecycle:  
Requirement    
Data Collection   
Model Building   
Inference   
Testing     
Deployment   


### Requirement

Create NER api which accepts a news article or a sentence from news article and identifies named Entities defined by businnes user,they are ORG,PLACE,PERSON,ROLE.   
I've taken these entities but we can add any new type of custom entity and train model.   

### Data Collection   

News article data is collected by refering my another repo <a href="https://github.com/sarang0909/news_api">news api</a>. 

Then sample 250 sentences annotated using <a href="https://doccano.github.io/doccano/">doccano</a>,a data annotation tool. Please note that since this is just a demo project,we have not used huge data. We have used only 250 sentences. In reality,data might be huge and any other data annotation technique can be used.  

### Model Building   
 
Input vectors used : TF-IDF, word embeddings from distilbert,word embeddings from sentence transformer

Model techniques used : 

1.Spacy   
Create spacy formatted data and train using Spacy library     
2.transformers   
Create BILOU format data at sentence level i.e 1 sentence per row and train using hugging face transformers trainer api.   
3.custom neural network    
Create BILOU format data at word level i.e 1 word per row and BERT tokenizer will add extra   
tokens like sub word,CLS,SEP. Can we treat this sequence of tokens of a single word as sequence classification for NER?   
I've explored this in custom_ner_dl notebook.   
However,I am not sure about this approach. Need to do more research.Hence not included this in final models list.    

| Model Name | Library | Description| Named Entites
| --- | --- |--- |--- |
| custom_ner_spacy | Spacy |train spacy for custom NER|CUSTOM_ORG,CUSTOM_PERSON,CUSTOM_PLACE,CUSTOM_ROLE
| custom_ner_transformers | transformers |Finetune DistilBertTokenClassification for custom NER in BILOU format|B-CUSTOM_ORG,I-CUSTOM_ORG,L-CUSTOM_ORG,U-CUSTOM_ORG,B-CUSTOM_PERSON,I-CUSTOM_PERSON,L-CUSTOM_PERSON,U-CUSTOM_PERSON,B-CUSTOM_ROLE,I-CUSTOM_ROLE,L-CUSTOM_ROLE,U-CUSTOM_ROLE,B-CUSTOM_PLACE',I-CUSTOM_PLACE,L-CUSTOM_PLACE,U-CUSTOM_PLACE


How to handle imbalance data?    
Since in BILOU format O stands for non-entity and we are going to have most of words as non-entity,our     
dataset is imbalanced.So we've used class_weights to handle this.   

### Inference   
There are 2 ways to deploy this application.   
1. API using FastAPI.
2. Streamlit application

### Testing     
Unit test cases are written   

### Deployment 
Deployment is done locally using docker.   


## Code Oraganization   
Like any production code,this code is organized in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Keep Data Collection and exploration notebooks  in src/training folder.  data_collection_eda.ipynb
3. Keep datasets in data folder.    
Raw data kept in raw_data csv.
Cleaned sentences stored in sentences_clean_data.jsonl  
Annotated sentences stored in 250_sentences_annotated_data.jsonl used for spacy training   
Annotated data for transformers training stored in BIOUL_data.csv
4. Keep model building notebooks at src/training folder.      
5. Keep generated model files at src/models.  
6. Write and keep inference code in src/inference.   
7. Write Logging and configuration code in src/utility.      
8. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
9. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
10. Build docker image.<a href="https://www.docker.com/">Docker</a>  
11. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
12. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
13. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Clone this repo locally and add/update/delete as per your requirement.   
Since we have used different design patterns like singleton,factory.It is easy to add/remove model to this code. You can remove code files for all models except the model which you want to keep as a final.   
Please note that this template is in no way complete or the best way for your project structure.   
This template is just to get you started quickly with almost all basic phases covered in creating production ready code.   

## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── main_streamlit.py 	    <- A main file to run API server.  
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── model	        <- model files   
│       ├── training 	        <- model training code  
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── data              <- datasets files   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```

 

## Usage
Here we have created ML inference on FastAPI server with dummy model output.

1. Go inside 'custom_ner_api' folder on command line.  
   Run:
  ``` 
      conda activate custom_ner_api  
      python main.py       
  ```
  Open 'http://localhost:5000/docs' in a browser.
![alt text](docs/fastapi_first.jpg?raw=true)
![alt text](docs/fastapi_second.jpg?raw=true)
 
2. Or to start Streamlit application  
5. Run:
  ``` 
      conda activate custom_ner_api  
      streamlit run main_streamlit.py 
  ```  

 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'custom_ner_api' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'custom_ner_api' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'custom_ner_api' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.



## Note
1.custom_ner_dl is not complete/need to be researched more.hence not included in final inference.But notebook is present.   
2.models are not checked in because of size. You can generate  models by running corresponding notebooks.   


## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

