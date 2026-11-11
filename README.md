# Data Science 6105 — Machine Learning Projects

A collection of data science coursework and projects covering exploratory data analysis, predictive modeling, automated machine learning, model explainability, and deep learning. The repository also includes a Streamlit application for electrical fault prediction.

## Projects and Assignments

| File | Focus |
| --- | --- |
| [Assignment 1](Assignment1-1.ipynb) | Exploratory analysis of laptop specifications and prices, feature selection, outlier analysis, missing-value treatment, and predictive modeling. |
| [Assignment 2](Assignment2%20%281%29.ipynb) | Laptop price prediction using H2O AutoML, model comparison, and global and local explanations. |
| [Assignment 3](Assignment3%20%281%29.ipynb) | Regression modeling, preprocessing pipelines, H2O models, and SHAP-based interpretation. |
| [Assignment 4](assignment4%20%281%29.ipynb) | Data preparation, regression and classification experiments, imputation, feature importance, and model interpretability. |
| [Assignment 5](Assignment5.ipynb) | Typeface digit recognition using the TMNIST dataset and a convolutional neural network built with TensorFlow/Keras. |
| [Final Learnings](Final/Final_learnings.ipynb) | Implementations and explanations of linear regression, logistic regression, and Naive Bayes using Python and NumPy. |
| [Fault Prediction App](test.py) | A Streamlit interface that uses a saved Random Forest classifier to predict electrical fault types from current and voltage measurements. |

## Laptop Dataset

The included [laptop_data_cleaned.csv](laptop_data_cleaned.csv) contains **1,273 records and 13 columns** describing laptop specifications and prices.

Features include manufacturer, laptop type, RAM, weight, touchscreen support, IPS display, pixel density, CPU brand, HDD and SSD capacity, GPU brand, and operating system. The notebooks use the `Price` column for regression and derive price categories for some classification experiments.

## Technologies

- **Data processing:** Python, pandas, NumPy, SciPy
- **Visualization:** Matplotlib, Seaborn
- **Machine learning:** scikit-learn, H2O AutoML, statsmodels
- **Explainability:** SHAP, ELI5, Graphviz
- **Deep learning:** TensorFlow/Keras
- **Application:** Streamlit, joblib
- **Notebooks:** Jupyter Notebook or Google Colab

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vamsi2215/Data-science-6105-.git
cd Data-science-6105-
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install packages for the notebooks you want to explore

For the laptop analysis notebooks:

```bash
python -m pip install jupyter pandas numpy scipy matplotlib seaborn scikit-learn statsmodels h2o shap eli5 graphviz
```

For the digit recognition notebook, also install TensorFlow:

```bash
python -m pip install tensorflow
```

H2O requires Java, and rendering Graphviz diagrams requires the Graphviz system application in addition to its Python package. These commands are a starting point; the repository does not provide a complete, tested environment for all notebooks.

### 4. Open the notebooks

```bash
jupyter notebook
```

Select an assignment and run its cells in order. Update dataset paths for your environment before running cells that load local files.

## Electrical Fault Prediction App

The app loads `model.joblib` and accepts six measurements:

| Input | Measurement |
| --- | --- |
| `Ia`, `Ib`, `Ic` | Phase currents in amperes |
| `Va`, `Vb`, `Vc` | Phase voltages in volts |

After entering the measurements, select **Predict** to display the fault category returned through the app's label mapping.

To run the app, use a separate virtual environment with Python 3.10 or 3.11 as a starting point for the older scikit-learn dependency:

```bash
python -m pip install streamlit pandas scikit-learn==1.3.2 joblib==1.4.0
streamlit run test.py
```

Run this command from the repository root so the app can find `model.joblib`. Streamlit will display the local URL in the terminal.

The `Capstone project/` folder also contains copies of the app and a model artifact.

## Reproducibility Notes

- The existing requirements files list `sklearn==1.3.2`. The installation package name is **`scikit-learn`**, while Python imports use `sklearn`. The commands above use the installation package name.
- `Assignment5.ipynb` expects `TMNIST_Data.csv` at `/content/TMNIST_Data.csv`. That dataset is not included; obtain it separately and update the path, or upload it to a Colab session.
- The linear regression example in `Final/Final_learnings.ipynb` references `insurance.csv`, which is not included.
- Some laptop notebooks fetch the included CSV through a GitHub URL and require internet access unless those cells are changed to use the local file.
- Saved model compatibility depends on the training environment. The app checks that the loaded artifact is a `RandomForestClassifier`; its fault label mapping should be verified against the original training labels before relying on predictions.
- The repository includes a saved fault prediction model, but does not include its training dataset or a dedicated training notebook. Full reproduction of that model requires those additional resources.

## Learning Outcomes

These projects explore how to prepare data, compare regression and classification approaches, interpret model behavior, build a convolutional neural network, and expose a trained model through an interactive interface.

## Author

[Vamsi2215](https://github.com/Vamsi2215)

## License

This repository is licensed under the [MIT License](LICENSE).
