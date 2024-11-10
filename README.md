## Text_Summarization 
This project is an end-to-end machine learning pipeline designed for text summarization using NLP techniques. The project includes:
Data versioning with DVC (Data Version Control).

Model training and evaluation using state-of-the-art NLP models.
API deployment using FastAPI with SwaggerUI for API documentation.
Modular code structure for easy scalability and maintainability.
Notebook to modular programming transition for reproducibility.

The project allows users to input text and receive a summarized version of the text using pre-trained or fine-tuned NLP models.

## 🚀 Features
End-to-End Pipeline: Data ingestion, preprocessing, model training, evaluation, and deployment.
FastAPI Integration: Expose the summarization model as an API with SwaggerUI documentation.
DVC Pipeline: Track data, models, and experiments with DVC.
Modular Programming: Transitioned from Jupyter Notebooks to a modular Python codebase.
NLP Techniques: Uses transformer-based model PEGASUS for text summarization.


## Install Dependencies

### Create a virtual environment:
```bash
conda create -p  ./summaryvenv python==3.8 -y  
```

### Activate the virtual environment:

- :
    ```bash
  conda activate ./summaryvenv
    ```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```
![Screenshot 2024-11-10 at 1 20 28 PM](https://github.com/user-attachments/assets/00873056-dc88-4ec4-a7eb-bfed281d51e5)

![Screenshot 2024-11-10 at 1 20 15 PM](https://github.com/user-attachments/assets/287c83ac-6ba2-4c94-8470-73b136784bbc)



## 4. Run the Application Locally

To run the FastAPI app locally using Uvicorn:
```bash
uvicorn application:app --reload --host 0.0.0.0 --port 8000
