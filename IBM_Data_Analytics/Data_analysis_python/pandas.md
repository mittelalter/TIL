# Data Wraningling (Week 2)
* Normalization
    * Simple Feature scaling
        * df['length'] / df['length'].max()
    * Min-Max
        * df['length'] - df['length'].min() / df['length'].max() - df['length'].min()
    * Z-Score
        * df['length'] - df['length'].mean() / df['length'].std() (standard deviation, 표준 편차)


* Convert categorical variables to dummy variables (0 or 1)
* pd.get_dummies(df[''])

<br>

# EDA (Week 3)
* pivot() Method
* Pearson Correaltion
    * +1 positive
    * -1 native
    * 0 no correlation
    * P value less than 0.001d

* Association between two categorical variables: Chi-Square
    * Chi-Square Test for association
        * The Chi-square tests a null hypothesis that the variables are independent
        * The Chi-square does not tell you the type of realationship that exists between both variables; but only that a realationship exists
    * x2 = chi-square value
    * P-value > 0.05 -> reject the null hypothesis, there is a association between two variables
    * scipy.stats.chi2_contingency(con_table, correction=True)

* Define correlation as the linear association between two numerical variables: Use Pearson correlation as a measure of the correlation between two continuous variables

* Define the association between two categorical variables: Understand how to find the association of two variables using the Chi-square test for association and how to interpret them.

<br>

# (Week 4)