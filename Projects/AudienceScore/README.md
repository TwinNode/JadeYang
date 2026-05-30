# Predicting Audience Score Project

There are many factors contributing to a movie's success and popularity. Our primary research question is whether a director's previous track record is associated with the audience reception of their subsequent projects.
In this analysis, I constructed a multiple linear regression model to predict audience scores. To identify significant predictors, I utilized a backward elimination methodology and performed rigorous model diagnostics to ensure all linear regression assumptions were met.
Finally, I validated the model's predictive performance using out-of-sample data.

## Key Findings

- The final model achieved an adjusted $R^2$ of  __0.9293__.
- The director's historical audience performance (`avg_director_score`) was identified as a statistically significant predictor of audience score.
- More detailed analysis can be found in `report.pdf`.

## Key Features

- Data Cleansing
- Research Question
- Exploratory Data Analysis (EDA)
- Modeling (Multiple Linear Regression Model, Backward Elimination)
- Model Diagnosis
- Prediction
- Conclusion

## Technologies Used 

- **Language**: R
- **Core Functions:**  * **Analysis:** `lm()`, `step()`, `predict()`
    * **Visualization & Diagnosis:** `ggplot2` (`geom_jitter`), `GGally` (`ggpairs`), `hist()`, `qqnorm()`, `qqline()`

## Data Sources

- **Main Dataset, Markdown Structure** : Duke University *Linear Regression and Modeling* (via Coursera)
- **Validation Data** : Rotten Tomatoes, IMDb
