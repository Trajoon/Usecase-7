# Usecase-7

---

# ⚽ **Football Players Dataset Analysis**

---

## 🎯 **Objective**
The goal of this analysis is to explore the football players' dataset for the seasons 2021-2022 and 2022-2023, understand the factors influencing player value, and predict players' current value based on performance and demographic features. This includes:
- Investigating key performance metrics and their impact on player value.
- Analyzing the influence of team affiliations on player value.
- Identifying trends in player injuries, goals, and other metrics.

---

## 📂 **Dataset Overview**
The dataset contains **10,754 records** with **22 columns** of information. Below is a breakdown of the dataset:

### 📝 **Dataset Information**
- **Number of rows:** 10,754
- **Number of columns:** 22
- **Key Columns:**
  - **Player Details:** `player`, `team`, `name`, `position`, `height`, `age`.
  - **Performance Metrics:** `appearance`, `goals`, `assists`, `yellow cards`, `second yellow cards`, `red cards`, `goals conceded`, `clean sheets`, `minutes played`, `days_injured`, `games_injured`, `award`.
  - **Market Value:** `current_value`, `highest_value`, `Value Change`.
  - **Team-Specific:** `team_*` (e.g., `team_Arsenal FC`, `team_Bayern Munich`).
- **Missing Values:**
  - No missing values across any columns.

---

## 🔍 **Feature Engineering**
- A new feature, `goal+assists`, was created by adding `goals` and `assists`, enhancing the understanding of offensive player output.

---

## 📊 **Correlation and Feature Selection**
- Correlations were calculated to identify features impacting the `current_value` of players.
- A threshold of 0.1 was set to filter for the most significant features.
- **Selected Features:** 
  - Key performance metrics: `appearance`, `goals`, `assists`, `minutes played`, `days_injured`, `games_injured`, `award`.
  - Team affiliations with significant influence on value, such as `team_Arsenal FC`, `team_Bayern Munich`.

---

## 📈 **Model Training and Evaluation**
- **Model Used:**
- Linear Regression to predict `current_value`.
- Ridge Regression: Used to handle multicollinearity and improve generalization.
- Lasso Regression: Used for feature selection by shrinking less important coefficients to zero.

---

## 🔑 **Feature Importance and Prediction Insights**

- **Feature Importance:**
  - Strongest predictors include `goals`, `assists`, and `appearance`.
  - Team affiliation also plays a significant role in player value, especially for top teams.
  
- **Prediction Interpretation:**
  - The model predicts the `current_value` based on a combination of performance metrics and team affiliation.
 
- **Model Deployment:**
  - https://usecase-7-9vww.onrender.com 
  
