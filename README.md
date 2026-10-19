# HealthLens AI 🔬

### Understand Your Lab Results. Prepare Better Questions.

HealthLens AI is an educational web application built with Streamlit. It helps users compare a laboratory result with a reference range they provide and understand what that comparison means.

**HealthLens AI is an educational prototype, not a medical diagnostic tool.**

## 🌟 Features

- **Lab Result Comparison:** Identify whether a supplied result is below, within, or above the supplied reference range.
- **Interactive Demo Cases:** Explore fictional examples for hemoglobin and glucose.
- **Input Validation:** Check that the lower reference limit does not exceed the upper limit.
- **Downloadable Summary:** Export a text summary of the comparison and questions to discuss with a healthcare professional.
- **Health Education Library:** Access educational resources about laboratory tests and understanding results.
- **Simple User Interface:** Use a clean, beginner-friendly Streamlit interface.

## 🛠️ Technology Stack

- Python
- Streamlit
- Basic rule-based comparison logic

## 🚀 Run Locally

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the required dependency:

   ```bash
   python -m pip install streamlit
   ```

4. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL displayed in your terminal.

## 🧪 Try the Demo

The application includes fictional demonstration cases for results that are within, below, and above the supplied reference range.

You can also enter your own test name, result, unit, and reference limits to explore the comparison feature.

## 📚 Educational Resources

- [MedlinePlus: Laboratory Tests](https://medlineplus.gov/lab-tests/)
- [MedlinePlus: Understanding Your Lab Test Results](https://medlineplus.gov/lab-tests/understanding-your-lab-test-results/)
- [NHS: Blood Tests](https://www.nhs.uk/conditions/blood-tests/)

## ⚠️ Important Disclaimer

HealthLens AI does not diagnose diseases, predict health conditions, recommend treatment, or replace professional medical advice. Laboratory results must be interpreted in context by a qualified healthcare professional. Reference ranges may differ between laboratories and individuals.

The examples provided in this prototype are fictional and intended for demonstration and education only.

## 🎯 Project Goal

The goal of HealthLens AI is to make basic laboratory reference-range comparisons easier to understand and help users prepare informed questions for healthcare professionals.

## 👩‍💻 Project Status

Educational hackathon prototype. The current version uses rule-based comparisons and educational links; it does not connect to an AI model or clinical system.

## 👤 Author

**Sunnaina Tanveer**
