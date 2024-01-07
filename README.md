# Cloud based application for economic load dispatch

## Abstract
Conventional economic load dispatch systems encounter challenges such as computational intensity, data storage limitations, slow real-time responsiveness, difficulty in collaborative optimization, security concerns, insufficient scalability for changing power system capacities, and high upfront costs. We present a cloud computing-based solution
powered by Amazon Web Services for tackling these challenges. Cloud computing addresses these issues by providing scalable resources, efficient data management, real-time
processing, secure collaboration, and cost-effective solutions. Our framework includes
two systems: ”Economic dispatch without constraints” and ”Economic dispatch considering Generator Limits.” We converted these systems into Python code and deployed them
on AWS Lambda by creating two different Lambda functions, along with other dependencies. And analyzed their performances. The real-time data were also stored in a database
called DynamoDB.
