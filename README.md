# NYC Taxi Time Prediction  

This project focuses on the deployment and integration of various frameworks to streamline experimentation, versioning, retraining, and deployment processes for predicting NYC taxi ride times.  

## Key Objectives  

- **Experimentation and Versioning**: Leveraging DagsHub and MLflow for experiment tracking and model versioning.  
- **Model Saving and Retraining**: Creating a robust pipeline to save models and enable seamless retraining as new data becomes available.  
- **App Deployment**: Deploying the predictive model as a functional app using AWS EC2, Docker, FastAPI, and Streamlit.  

## Workflow Overview  

1. **Experimentation with DagsHub and MLflow**:  
   - Use MLflow for tracking experiments, recording metrics, and managing model versions.  
   - Collaborate and version control datasets and code using DagsHub.  

2. **Model Pipeline Creation**:  
   - Build a pipeline to preprocess data, train models, and save them for future use.  
   - Enable retraining of models with updated datasets for continuous improvement.  

3. **Deployment to AWS EC2**:  
   - Utilize Docker for containerizing the app for consistent deployment.  
   - Deploy the backend API using FastAPI and the frontend interface using Streamlit.  

4. **Frontend and Backend Integration**:  
   - **FastAPI**: Backend API for handling model predictions and data processing.  
   - **Streamlit**: Frontend application for user interaction and visualization.  

## Technologies Used  

- **DagsHub**: For data and code versioning.  
- **MLflow**: For tracking experiments and managing model versions.  
- **Docker**: For containerizing the application.  
- **FastAPI**: For building the backend API.  
- **Streamlit**: For creating an interactive frontend interface.  
- **AWS EC2**: For hosting the deployed application.  

## Getting Started  

### Prerequisites  

- Python 3.x  
- Docker installed on your machine  
- AWS account with access to EC2  
- MLflow and DagsHub accounts  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repository.git  
   cd your-repository  
   ```  

2. Set up a Python virtual environment and install dependencies:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # For Linux/Mac  
   venv\Scripts\activate  # For Windows  
   pip install -r requirements.txt  
   ```  

3. Set up AWS credentials and configure EC2 for deployment.  

### Usage  

1. **Experimentation and Versioning**:  
   - Track your experiments using MLflow.  
   - Push data and code to DagsHub for version control.  

2. **Pipeline Execution**:  
   - Train models and save them to the appropriate directory.  
   - Use the pipeline to retrain models with new data as needed.  

3. **Deploy the App**:  
   - Build and run the Docker container:  
     ```bash  
     docker build -t nyc-taxi-time .  
     docker run -p 80:80 nyc-taxi-time  
     ```  
   - Access the app through the EC2 public IP or DNS.  

4. **Frontend Interface**:  
   - Use Streamlit for visualizing predictions and interacting with the model.  

## Contributions  

Contributions are welcome! Submit a pull request or create an issue if you have ideas or find bugs.  

## License  

This project is licensed under the [MIT License](LICENSE).  

---  

Let me know if you'd like to add more details!
