# Cloud based application for economic load dispatch

## Abstract
Conventional economic load dispatch systems encounter challenges such as computational intensity, data storage limitations, slow real-time responsiveness, difficulty in collaborative optimization, security concerns, insufficient scalability for changing power system capacities, and high upfront costs. We present a cloud computing-based solution
powered by Amazon Web Services for tackling these challenges. Cloud computing addresses these issues by providing scalable resources, efficient data management, real-time
processing, secure collaboration, and cost-effective solutions. Our framework includes
three systems: ”Economic dispatch without constraints”, ”Economic dispatch considering Generator Limits” and ”Economic dispatch considering all constraints” We converted these systems into Python code and deployed them
on AWS Lambda by creating two different Lambda functions, along with other dependencies. And analyzed their performances. The real-time data were also stored in a database
called DynamoDB.

## Introduction

An essential aspect of the economic operation of power generation and distribution involves
the principle of economic dispatch, striving to minimize the cost associated with power production. Under specified load conditions, economic dispatch plays an important role in determining the power output for each plant, including individual generating units within those
plants. The primary objective is to minimize the overall cost of fuel required, to meet the system load. Essentially, economic dispatch entails orchestrating the distribution of production
costs among all operational power plants within the system.
