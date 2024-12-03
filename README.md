# Retail Analysis and Word Count using MRJob

This lab involves using `MRJob`, a Python framework for writing MapReduce jobs, to process and analyze two different datasets:
1. **Retail Dataset**: Analyze sales data to calculate total spending and find the maximum price for each country and month.
2. **Word Count Dataset**: Perform word frequency analysis on product descriptions.

---

## Table of Contents
1. [Overview](#overview)
2. [Scripts](#scripts)
    - [RetailDetail](#retaildetail)
    - [WordCount](#wordcount)
3. [Inputs and Outputs](#inputs-and-outputs)
4. [Execution](#execution)
5. [Expected Output](#expected-output)

---

## Overview
This lab demonstrates how to use MapReduce with MRJob to analyze datasets. Each script contains a `mapper` and `reducer` function, which process data in parallel.

---

## Scripts

### 1. RetailDetail
#### **Purpose**:
Analyze retail data to calculate:
- The total amount spent for each country and month.
- The maximum price of an item in each country and month.

#### **Mapper**:
- Reads the input line by line.
- Extracts `Country`, `Month`, `Quantity`, and `Price` fields from the dataset.
- Calculates the `amount_spent` for each entry and emits `(country, month)` as the key and `(amount_spent, price)` as the value.

#### **Reducer**:
- Aggregates total spending and finds the maximum price for each `(country, month)` key.

---

### 2. WordCount
#### **Purpose**:
Count the frequency of each word in the product description field of the dataset.

#### **Mapper**:
- Reads the input line by line.
- Splits the `Description` field into individual words.
- Emits each word as a key with a value of `1`.

#### **Reducer**:
- Aggregates the count of each word and emits `(word, frequency)`.

---

## Inputs and Outputs

### RetailDetail
#### **Input**:
- A tab-separated retail dataset with fields:
