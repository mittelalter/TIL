# About basic infos about Data Analytics

Content
> * Understanding Data Repositories and Big Data Platforms
> * Gathering Data
> * Analyzing and Mining Data

<br>

# Data Repositories and Big data Platforms

A Data Repository is a general term that refers to data that has been collected, organized, and isolated so that it can be used for reporting, analytics, and also for archival purposes.  

The different types of Data Repositories include: 

Databases, which can be relational or non-relational, each following a set of organizational principles, the types of data they can store, and the tools that can be used to query, organize, and retrieve data.

* Data Warehouses, that consolidate incoming data into one comprehensive storehouse.  

* Data Marts, that are essentially sub-sections of a data warehouse, built to isolate data for a particular business function or use case. 

* Data Lakes, that serve as storage repositories for large amounts of structured, semi-structured, and unstructured data in their native format. 

* Big Data Stores, that provide distributed computational and storage infrastructure to store, scale, and process very large data sets.

ETL, or Extract Transform and Load, Process is an automated process that converts raw data into analysis-ready data by:

* Extracting data from source locations.

* Transforming raw data by cleaning, enriching, standardizing, and validating it.

* Loading the processed data into a destination system or data repository.

Data Pipeline, sometimes used interchangeably with ETL, encompasses the entire journey of moving data from the source to a destination data lake or application, using the ETL process.  

Big Data refers to the vast amounts of data that is being produced each moment of every day, by people, tools, and machines. The sheer velocity, volume, and variety of data challenge the tools and systems used for conventional data. These challenges led to the emergence of processing tools and platforms designed specifically for Big Data, such as 
Apache Hadoop, Apache Hive, and Apache Spark.

<br>

# Gathering Data

* The process of identifying data begins by determining the information that needs to be collected, which in turn is determined by the goal you seek to achieve. 

* Having identified the data, your next step is to identify the sources from which you will extract the required data and define a plan for data collection. Decisions regarding the timeframe over which you need your data set, and how much data would suffice for arriving at a credible analysis also weigh in at this stage.  

* Data Sources can be internal or external to the organization, and they can be primary, secondary, or third-party, depending on whether you are obtaining the data directly from the original source, retrieving it from externally available data sources, or purchasing it from data aggregators. 

* Some of the data sources from which you could be gathering data include databases, the web, social media, interactive platforms, sensor devices, data exchanges, surveys and observation studies. 

* Data that has been identified and gathered from the various data sources is combined using a variety of tools and methods to provide a single interface using which data can be queried and manipulated. 

* The data you identify, the source of that data, and the practices you employ for gathering the data have implications for quality, security, and privacy, which need to be considered at this stage.  


<br>

# Wrangling Data

Once the data you identified is gathered and imported, your next step is to make it analysis-ready. This is where the process of Data Wrangling, or Data Munging, comes in. Data Wrangling is an iterative process that involves data exploration, transformation, and validation.  

Transformation of raw data includes the tasks you undertake to:

* Structurally manipulate and combine the data using Joins and Unions.

* Normalize data, that is, clean the database of unused and redundant data.

* Denormalize data, that is, combine data from multiple tables into a single table so that it can be queried faster. 

* Clean data, which involves profiling data to uncover quality issues, visualizing data to spot outliers, and fixing issues such as missing values, duplicate data, irrelevant data, inconsistent formats, syntax errors, and outliers.

* Enrich data, which involves considering additional data points that could add value to the existing data set and lead to a more meaningful analysis.

A variety of software and tools are available for the Data Wrangling process. Some of the popularly used ones include Excel Power Query, Spreadsheets, OpenRefine, Google DataPrep, Watson Studio Refinery, Trifacta Wrangler, Python, and R, each with their own set of characteristics, strengths, limitations, and applications. 


<br>

# Analyzing and Mining Data
Statistics is a branch of mathematics dealing with the collection, analysis, interpretation, and presentation of numerical or quantitative data. 

Statistical Analysis involves the use of statistical methods in order to develop an understanding of what the data represents. 

Statistical Analysis can be:

* Descriptive; that which provides a summary of what the data represents. Common measures include Central Tendency, Dispersion, and Skewness.

* Inferential; that which involves making inferences, or generalizations, about data. Common measures include Hypothesis Testing, Confidence Intervals, and Regression Analysis.

Data Mining, simply put, is the process of extracting knowledge from data. It involves the use of pattern recognition technologies, statistical analysis, and mathematical techniques, in order to identify correlations, patterns, variations, and trends in data. 

There are several techniques that can help mine data, such as, classifying attributes of data, clustering data into groups, establishing relationships between events, variables, and input and output.  

A variety of software and tools are available for analyzing and mining data. Some of the popularly used ones include Spreadsheets, R-Language, Python, IBM SPSS Statistics, IBM Watson Studio, and SAS, each with their own set of characteristics, strengths, limitations, and applications. 