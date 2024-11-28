# 🏅 Olympic Data Analysis

This project is an interactive data visualization and analytics platform for exploring historical Olympic Games data. Built with Python and Streamlit, it offers an in-depth analysis of medal tallies, athlete statistics, and country-wise performance trends, providing users with powerful insights into the world's biggest sporting event.

---

## 📌 Features

- **Medal Tally Analysis:**
  - Explore medal tallies by year, country, or both.
  - Compare the performance of nations and athletes across Olympic editions.

- **Overall Analysis:**
  - Visualize participation growth in terms of nations, events, and athletes.
  - Examine trends in sports, events, and athlete demographics.

- **Country-Wise Analysis:**
  - Delve into the medal-winning history of specific countries.
  - Identify sports where countries excel using heatmaps.

- **Athlete-Wise Analysis:**
  - Analyze age distributions of medalists across gold, silver, and bronze categories.
  - Study the physical attributes (height, weight) of athletes by sport and gender.
  - Explore the historical participation trends of male and female athletes.

---

## 🚀 Technologies Used

- **Python** for data processing and analysis.
- **Streamlit** for creating the interactive web app.
- **Pandas** for data manipulation and cleaning.
- **Matplotlib**, **Seaborn**, and **Plotly** for visualizing trends and distributions.
- **Scipy** for generating statistical plots.

---

## 📂 Data Sources

1. **Athlete Events Dataset**: Contains details of athletes, their events, and medal outcomes.
2. **NOC Regions Dataset**: Maps National Olympic Committees (NOCs) to their respective regions.

---

## 🛠️ How It Works

1. **Data Preprocessing**:
   - Filtered for Summer Olympics data to ensure relevance.
   - Merged datasets to include regional information.
   - Applied one-hot encoding for medal types for detailed analysis.

2. **Interactive Dashboard**:
   - Users can explore trends via dropdowns and dynamic visualizations.
   - Options to analyze data by year, sport, athlete, or nation.

---

## 📊 Visual Highlights

- **Line Charts**:
  - Growth of participating nations, athletes, and events over time.
- **Heatmaps**:
  - Sports performance trends of countries.
- **Scatter Plots**:
  - Height vs. weight distribution of athletes, categorized by gender and medal type.
- **Distribution Plots**:
  - Age trends among gold, silver, and bronze medalists.

---

## 🖥️ How to Run the Project

1. Visit the live application hosted on Streamlit:  
   [Olympic Data Analysis](https://olympic-data-analysis-bynehul.streamlit.app/)

2. Alternatively, you can run it locally:
   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/Olympic-Data-Analysis.git
     cd Olympic-Data-Analysis
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Streamlit app:
     ```bash
     streamlit run app.py
     ```
   - Open the app in your browser at `http://localhost:8501`.


## 📢 Contributions

- Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request for improvements.

---

## 📧 Contact

- For any queries or suggestions, reach out at nehulkr30582@gmail.com.
