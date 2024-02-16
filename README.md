# SKAI LABS Software Engineering Tasks

This repository contains solutions to the skill assessment tasks provided by SKAI LABS.

## Table of Contents
- [Task 1: Display Polygon on a Map](#taks1)
- [Taks 2: Detecting Unauthorized Sales](#task2)
- [Task 3: Optimal Job Interview Scheduling](#task3)

## Task 1: Display Polygon on a Map

### Task Overview
Create a web application that displays the polygon defined in the provided polygon.json file on a map. Use the OpenLayers library to accomplish this task.

### Solution
My solution fetches the polygon.json file and reads its coordinates. These coordinates are transformed from longitude/latitude to map's projection, which is the Web Mercator projection.
Then, a polygon geometry is initialized using these transformed coordinates. A feature with that geometry is created. Finally, a new vector layer is created to display that polygon.

### Usage
This project utilizes the OpenLayers library. If you don't have it installed already, you can do so by running this command in the terminal:
```bash
npm install ol
```

Run the code by running this command in the terminal:
```bash
npm run start
```
Visit the displayed localhost link.

## Task 2: Detecting Unauthorized Sales

### Task Overview
Develop a REST API endpoint that processes POST requests containing two lists: one containing product listing (including product ID and authorized seller ID) and the other actual sales transactions (including product ID and seller ID). Develop an algorithm that identifies any sales transactions made by unauthorized seller.

### Solution
My solution organizes the JSON data into a dictionary with productID as the key and a list of authorizedSellerIDs as the value. The assumption is made that one product can have multiple authorized sellers. The algorithm iterates through the list of transactions and verifies whether the sellerID exists in the list of authorized sellers.

### Usage
This project utilizes Python package Flask. If you don't have it installed already, you can do so by running this command in the terminal:
```bash
pip install Flask
```
(Optional) This project uses the Requests package for testing. You can install this package by running this command in the terminal:
```bash
pip install requests
```
Otherwise, you can use Postman or curl for testing.

Run the main program by running this command in the terminal:
```bash
python task2.py
```
You can run the testing script in the seperate terminal:
```bash
python post_example.py
```
You can modify the json_example variable in the json_example.py for further testing.

## Taks 3: Optimal Job Interview Scheduling

### Task Overview
Develop a REST API endpoint that processes POST requests containing two lists: start times and end times of job interviews. The goal is to calculate the maximum number of non-overlapping interviews a person can attend, considering that transitioning from one interview to another requires no time if the next interview starts exactly at or after the previous one ends.

### Solution
My solution organizes the data into a sorted list of tuples. The algorithm iterates through the list, comparing each interval to the one before. If the interval starts after the previous one ends, the count for maximum interviews increases by one. If two intervals overlap, the algorithm takes the interview with the smaller end time to compare with the next interview at the next iteration. This choice is made because selecting the interview with the smaller end time reduces the probability of overlap with the next interview compared to choosing the one with the larger end time.

### Usage
This project utilizes Python package Flask. If you don't have it installed already, you can do so by running this command in the terminal:
```bash
pip install Flask
```
(Optional) This project uses the Requests package for testing. You can install this package by running this command in the terminal:
```bash
pip install requests
```
Otherwise, you can use Postman or curl for testing.

Run the main program by running this command in the terminal:
```bash
python task3.py
```
You can run the testing script in the seperate terminal:
```bash
python post_example.py
```
You can modify the json_example variable in the json_example.py for further testing.