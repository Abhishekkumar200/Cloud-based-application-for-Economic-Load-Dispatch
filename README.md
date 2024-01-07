# Cloud based application for economic load dispatch

## Abstract
Conventional economic load dispatch systems encounter challenges such as computational intensity, data storage limitations, slow real-time responsiveness, difficulty in collaborative optimization, security concerns, insufficient scalability for changing power system capacities, and high upfront costs. We present a cloud computing-based solution
powered by Amazon Web Services for tackling these challenges. Cloud computing addresses these issues by providing scalable resources, efficient data management, real-time
processing, secure collaboration, and cost-effective solutions. Our framework includes
three systems: ”Economic dispatch without constraints”, ”Economic dispatch considering Generator Limits” and ”Economic dispatch considering all constraints” We converted these systems into Python code and deployed them
on AWS Lambda by creating two different Lambda functions, along with other dependencies. And analyzed their performances. The real-time data were also stored in a database
called DynamoDB.
