# Martial Religious Association Analysis Project

### Summary
This project analyzes the association between __marital status__ and __religious affiliation__ using data from the 2024 General Social Survey(GSS) data.
To determine if the observed patterns reflects a statistically significant relationship in the population, I performed a __Chi-square test of independence__.

### Repository Contents
- `analysis.pdf` : The final report covering GSS background, the sampling methodology, hypothesis testing, and analytical findings.
- `stat_inf_project.rmd` : R markdown source file containing the complete analysis code.
- `Final_Project.rproject` : The RStudio project file; open this to ensure all paths and dependencies are correctly set.
- `GSS 2024 Codebook R3.pdf` : Official documentation from GSS detailing survey variables and methodology.
- *Note on sample data* : The raw dataset used for this analysis is not included in this repository. Please follow the instructions below to prepare the data.

### Data Sources & References
- __Analysis Guidelines__: Provided by *Inferential Statistics* course (Duke University, Coursera)
- __Data Source__: General Social Survey(GSS) 2024. Access the data here: https://gss.norc.org/get-the-data/stata.html

### Getting Sample Data Ready
To reproduce the analysis, please follow these steps:
1. Download the raw GSS2014 data in Stata format on the official GSS website.
2. Place the file in the project folder and name it as `gss2024.dta` (ensure the file extension is correct!).
3. Run the provided R script within the RStudio project to process the data and perform the analysis.
