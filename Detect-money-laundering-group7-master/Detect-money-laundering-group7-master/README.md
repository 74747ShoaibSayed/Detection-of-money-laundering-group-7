# Detection of Money Laundering | Data Engineering AWS Project


## Introduction

Money laundering is a significant challenge in the financial industry, threatening economic stability and enabling criminal activities. This project aims to use Machine Learning (ML) and Artificial Intelligence (AI) to enhance the detection of money laundering using the IBM Transactions for Anti-Money Laundering (AML) dataset. The dataset includes synthetic financial transactions, simulating both legal and illicit activities.

We will leverage AWS services like S3, Lambda, Glue Crawler, EventBridge, Glue Job, Athena, ODBC, and EMR to build and deploy machine learning models. The goal is to improve the accuracy of detecting suspicious transactions while minimizing false positives and negatives, thereby strengthening efforts to combat financial crime.

## Architecture

![Project Architecture.drawio.png](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/Project%20Architecture.drawio.png)

## Technology Used

1. Programming Language - python, pyspark
2. Scripting language - SQL
3. AWS Cloud Platform
   - S3
   - Lambda
   - EMR
   - Glue Crawler
   - Event Bridge Rule
   - Glue ETL Job
   - Athena
4. Data Visualization - Power Bi


## Dataset Used

This dataset contains synthe c financial transac on data designed to simulate a virtual world inhabited by individuals, companies, and banks. The transac ons include various forms of interac ons such as purchase of goods and services, payment of salaries, and repayment of loans. Some individuals and companies in the dataset engage in criminal ac vi es like smuggling, illegal gambling, and extor on, genera ng illicit funds that they a empt to launder through a series of transactions.

Here is the link to the dataset reffer : https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml

## Transaction Data Description

| **Column Name**       | **Description**                                                                     |
|-----------------------|-------------------------------------------------------------------------------------|
| **Timestamp**         | Date and time of the transaction (format: DD-MM-YYYY HH)                             |
| **From Bank**         | Identifier for the bank sending the funds                                            |
| **From Account**      | Identifier for the account sending the funds                                         |
| **To Bank**           | Identifier for the bank receiving the funds                                          |
| **To Account**        | Identifier for the account receiving the funds                                       |
| **Amount Received**   | Amount of money received by the receiving account                                    |
| **Receiving Currency**| Currency in which the amount was received                                            |
| **Amount Paid**       | Amount of money paid by the sending account                                          |
| **Payment Currency**  | Currency in which the amount was paid                                                |
| **Payment Format**    | Format of the payment (e.g., Cheque, ACH, Credit Card, Reinvestment)                 |
| **Is Laundering**     | Binary indicator (0 or 1) showing if the transaction is laundering (1) or legitimate (0) |


## Scripts for Project
### Lambda

1. [Bucket_Trigger.py](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/Lambda%20Codes/1.Glue%20Crawler.py)
2. [Event_Bridge_Trigger.py](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/Lambda%20Codes/1.Glue%20Crawler.py)
3. [Bucket_Trigger_2.py](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/Lambda%20Codes/3.Glue%20Crawler2.py)

### Event Bridge Rule

1. [Crawler_Rule.yaml](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/Event%20Bridge%20Rule/Rule.json)

### ETL Job

1. [Transfomation.py](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/ETL%20Files/jobgluegroup7aiml.py)

### EMR Pyspark

1. [Model.py](https://github.com/Manis7733/Detect-money-laundering-group7/blob/master/ML%20Files/mlpro.ipynb)


## Outcome of Project
The project successfully implemented two machine learning models, Random Forest and Logistic Regression, to detect money laundering transactions. The models achieved high accuracy, with **Random Forest reaching 96%** and **Logistic Regression achieving 97%**, demonstrating the effectiveness of these techniques in identifying illicit activities within financial transactions.


## Our Contributers
- [Vedant Mahale](https://github.com/VedantMahale30)
- [Mihir Dalvi](https://github.com/mihirda-7)
- [Sudarshan Sangle]()
- [Vaishnavi Kapde](https://github.com/Vaishnavi1041)
- [Shoaib Sayed](https://github.com/74903ShoaibSayed)
- [Manish Parate](https://github.com/Manis7733)
