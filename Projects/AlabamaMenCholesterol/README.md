# 📊 BRFSS Data Analysis: Lifestyle & Cholesterol in Alabama Men

This project investigates the association between **lifestyle choices** (physical activity and alcohol consumption) and **cholesterol levels** specifically among the male population in Alabama. 

---

## 🎯 Research Objectives
1. **Exercise & Cholesterol:** Does regular physical activity correlate with a lower prevalence of high cholesterol?
2. **Alcohol's Impact:** How does monthly alcohol intake relate to cholesterol, and does exercise moderate this relationship?
3. **Outlier Analysis:** How do extreme drinking habits (heavy drinkers) affect data distribution and health outcomes?

---

## 🛠 Programming Language & Tools
*   **Language:** R
*   **Key Libraries:** `ggplot2`, `dplyr`
*   **Output Formats:** R Markdown (`.Rmd`), PDF Report

---

## 📂 Project Structure
*   `intro_data_prob_project.rmd`: The complete R code and narrative analysis.
*   `Analysis_Report.pdf`: The final rendered report with visualizations and conclusions.
*   `alabama_male.RData`: A filtered subset of the data (Alabama Men only) used for the analysis. 
    > *Note: The original `brfss2013` dataset was excluded due to its large size (>100MB).*

---

## 📊 Key Findings
*   **Exercise Matters:** Inactive men showed a significantly higher proportion of high cholesterol compared to active men.
*   **Moderating Effect:** For those who do not exercise, lower alcohol consumption is more strongly associated with maintaining normal cholesterol levels.
*   **Median Importance:** Due to significant right-skewness caused by heavy drinkers, **medians** were used for a more accurate representative comparison.

---

## 📥 Data Source
The data was sourced from the **Behavioral Risk Factor Surveillance System (BRFSS)**.
*   [Official CDC BRFSS Website](http://www.cdc.gov/brfss/)
*   Data processed via [Duke University Data and Visualization Services](http://guides.library.duke.edu/c.php?g=289704&p=1930838)

---

## 🚀 How to Run
1. Clone this repository.
2. Ensure `alabama_male.RData` is in the same directory as the `.Rmd` file.
3. Open the `.Rmd` file in RStudio and click **Knit**.
