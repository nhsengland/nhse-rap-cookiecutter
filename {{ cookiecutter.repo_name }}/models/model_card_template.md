# {Model Name} Model Card

<!-- Replace {Model Name} with your actual model name -->

## Specification

This section contains top-level information about what the model is. The details of this section are in a table format so as to quickly give the reader the relevant information.

| | |
| --- | --- |
| **Description:** | [General overview of the model, what it does, and motivation for developing it. No more than one paragraph] |
| **Model Type:** | [Specify the type of model (e.g., clustering, time series, deep learning models, reinforcement learning, supervised learning, ensemble, hybrid, etc.) and describe its main characteristics] |
| **Developed By:** | {{ cookiecutter.author_name }} / {{ cookiecutter.team_name }} |
| **Launch Date:** | [Expected or Launch Date - e.g., {% now 'utc', '%B %Y' %}] |
| **Version** | [As in model registry - e.g., 1.0.0] |

## Intended Use

This section goes into more detail about why the model was built and who it was for. This section can go into more depth than previous, but should still be as succinct as possible.

**Development Background:** [A brief description of the model's development purpose and context, this is a chance to expand on the description, any additional background information on the model's focus area, who this originally created for and how the model fits into the wider decision making process.]

**Scope:** [Specific application or functionality of the model. What problem does it solve? What decisions does it support?]

**Intended Users:** [Describe who the model is intended for. E.g., clinical staff, analysts, researchers, policy makers, etc.]

**Use cases out of scope:** [Describe any potential use cases out of scope. What should this model NOT be used for?]

## Data

This section should provide basic details about the data used in and by the model. Any more detail should be provided in supplementary information, such as a DataSheet.

**Data Overview:** [A brief overview of where the data comes from, the type of data and its coverage etc. E.g., NHS administrative data, patient records, etc.]

**Sensitive Data:** [How is any sensitive data handled? What privacy protections are in place? Is data anonymized/pseudonymized?]

**Pre-processing and cleaning:** [How was the data cleansed? Was its suitability verified before use? Why these datasets? Are they representative of the target population?]

**Data Split:**

| | | |
| --- | --- | --- |
| **Training:** | [x%] | [Use this space to describe the training data, expanding on the data overview. Time period, sample size, key characteristics] |
| **Testing:** | [x%] | [Use this space to describe the testing data, expanding on the data overview. Time period, sample size, key characteristics] |
| **Validation:** | [x%] | [Use this space to describe the validation data, expanding on the data overview. Time period, sample size, key characteristics] |

## Methodology and Training

This section should explain how the model was built to do what it does, including any justification where required. Lengthy debate or detail of particular methodology should be provided in user documentation and not in the model card.

**Model Type:** [Specify the type of model (e.g., clustering, time series, deep learning models, reinforcement learning, supervised learning, ensemble, hybrid, etc.) and describe its main characteristics.]

**Models Used:** [What models were used? E.g., XGBoost classifier, LSTM neural network, Random Forest ensemble, etc.]

**Justification:** [Explain here why this approach was taken over another. What makes this the best choice for the problem?]

**Algorithm Details:** [Describe the main steps when data is sent to the model for inference. E.g., how is text data converted into a binary class? What transformations are applied?]

**Feature Engineering:** [Details on the process of creating and selecting features if relevant. What features were created and why? How were they selected?]

**Alternative Methods Considered:**

1. [Option A - e.g., Logistic regression - rejected because...]
2. [Option B - e.g., Neural network - rejected because...]
3. [Option C - etc.]

### Training Methods:

**Training Process:** [Description of the model training process. Include training duration, computational resources, convergence criteria. Link to relevant code: {{ cookiecutter.repository_url }}/tree/main/{{ cookiecutter.module_name }}/modeling]

**Hyperparameter/Fine Tuning:** (optional) [Detail any additional processes to select appropriate hyperparameters or other types of fine tuning. E.g., grid search, Bayesian optimization, cross-validation strategy.]

## Evaluation and Performance

This section details how well the model performs.

**Note:** The metrics and visual in this section is an example only and is not intended to indicate the evaluation methods and visuals you should use. Please adjust the types of metrics and visuals appropriately to suit requirements.

### Model Evaluation

**Evaluation Process:** [How the model is evaluated. E.g., holdout test set, cross-validation, temporal validation, etc.]

**Evaluation Focus:** (optional) [If relevant, provide detail and an explanation for why a particular metric (e.g. F1 score), or performance for/across specific data subset/s was prioritised. Why is this metric most important for your use case?]

**Performance breakdown:** [Details on the model's performance across different subsets or categories of data. E.g., performance by demographic group, time period, geographic region, etc.]

**Metrics:** Use the table below for performance metrics, adjust as appropriate.

| | |
| --- | --- |
| **F1 Score** | [0.00] |
| **Precision** | [0.00] |
| **Recall** | [0.00] |
| **Accuracy** | [0.00] |
| **AUC-ROC** | [0.00] |

The below confusion matrix is an example of how to include an image in this model card - visuals can be helpful but it is not a requirement to use a confusion matrix.

![Confusion Matrix](../reports/figures/confusion_matrix.png)

<!-- To add your own figure, save it to reports/figures/ and update the path above -->

**Performance in Deployment:** [Detail the performance of the model in deployment once monitoring is completed. State any considerations taken for the model inference time and provide the results in brief. E.g., average inference time, throughput, production metrics vs training metrics.]

### Ethical Considerations

**Bias and fairness analysis:** [Describe the approach for analysing error and the insights gained from them. Have you checked for disparate performance across protected characteristics? What did you find?]

**Implications for human safety:** [Potential impact on human life, potential harm and safety and mitigation. What are the consequences of false positives/negatives? How are predictions used in decision-making?]

### Caveats

**Caveats and Limitations:** [Describe here any important information or limitations (e.g. how will an NLP model handle changes in human language like new slang). What are the known failure modes? When should this model not be used?]

## Additional Links

- [Model Documentation]({{ cookiecutter.repository_url }})
- [Code Repository]({{ cookiecutter.repository_url }}/tree/main/{{ cookiecutter.module_name }}/modeling)
- [Issues]({{ cookiecutter.repository_url }}/issues)
- [Contributing Guide](../docs/content/contributing.md)
