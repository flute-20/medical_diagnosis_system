project is deployed on streamlit the link is provided below 

link = 'https://medicaldiagnosis-multidiseasepredictive-system.streamlit.app/'
search this url in chrome you will see the application.

This project is a Machine Learning-based Medical Diagnosis System that predicts the likelihood of multiple diseases based on user input parameters. The system is built using Python, Streamlit, and scikit-learn. It includes models for predicting diseases like:

Diabetes
Heart Disease
Hypothyroid
Lung Cancer
Parkinson’s Disease
🚀 Features
✅ Predict multiple diseases using a single interface
✅ User-friendly Streamlit-based frontend
✅ Real-time data processing and model prediction
✅ Supports multiple machine learning models
✅ Scalable and easy to deploy

🛠️ Tech Stack
Python
Streamlit
scikit-learn
NumPy
Pickle
Pandas
📁 Project Structure
php
Copy
Edit
📂 Medical_Diagnosis
├── 📂 models                # Saved ML models in .sav format
├── 📂 data                  # Sample datasets for training
├── 📂 static                # Static files (CSS, images)
├── 📂 templates             # HTML templates (if any)
├── app.py                   # Main Streamlit app
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignore unnecessary files
🚦 Setup Instructions
Clone the Repository
bash
Copy
Edit
git clone https://github.com/flute-20/medical_diagnosis_system.git
Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate the Virtual Environment
Windows:
bash
Copy
Edit
.\venv\Scripts\activate
Linux/macOS:
bash
Copy
Edit
source venv/bin/activate
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🏋️‍♂️ How to Use
Open the app in your browser after running the command.
Enter the required health parameters for prediction.
Click the "Predict" button to get the results.
The app will display the likelihood of each disease.
🤖 Model Details
Disease	Model Used	Accuracy
Diabetes	Support Vector Machine (SVM)	85%
Heart Disease	Logistic Regression	83%
Hypothyroid	Random Forest	89%
Lung Cancer	Decision Tree	80%
Parkinson's Disease	Gradient Boosting	87%
🐞 Troubleshooting
Ensure all dependencies are installed correctly using pip list.
If the app fails to load, check for version conflicts using pip freeze.
If prediction fails, check the model paths and update app.py accordingly.
📌 Future Scope
Add more diseases and expand dataset coverage.
Improve model accuracy with hyperparameter tuning.
Deploy using cloud-based services (e.g., Render, Heroku).
👥 Contributors
Vijaya Sri Sangepu
📜 License
This project is licensed under the MIT License.

