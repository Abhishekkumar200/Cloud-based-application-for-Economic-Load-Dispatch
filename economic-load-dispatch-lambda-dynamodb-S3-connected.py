import json
import boto3
import csv
import io
import numpy as np
from datetime import datetime
from time import gmtime, strftime

s3Client = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Get our object
    response = s3Client.get_object(Bucket=bucket, Key=key)
    
    # Process it
    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)
    print(reader)
    alpha_column = []
    beta_column = []
    gamma_column = []
    lower_column = []
    upper_column = []
    for row in reader:
        alpha_column.append(float(row[0]))
        beta_column.append(float(row[1]))
        gamma_column.append(float(row[2]))
        lower_column.append(float(row[3]))
        upper_column.append(float(row[4]))
    
    # Convert to NumPy arrays
    alpha_array = np.array(alpha_column)
    beta_array = np.array(beta_column)
    gamma_array = np.array(gamma_column)
    lower_bound = np.array(lower_column)
    upper_bound = np.array(upper_column)
    #print(alpha_array)
    
    
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LoadDispatchWithoutConstraintsDB')
    # now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    now = datetime.now()
    start = datetime.now()
    #lower_bound = np.array([200, 150, 100])
    PD = 150
    ans = ''
    result = ''
    
    def calculate_dispatch(alpha, beta, gamma, lower_bound, upper_bound):
        B = np.array([[0.0218, 0.0, 0.0],
                               [0.0, 0.0228, 0.0],
                               [0.0, 0.0, 0.0179]])    # associated with p1^2,p2^2,p2^2.. this is the function of the power losses with the generators
        
        B_O=np.array([7.0,6.3,6.8])                     # this is the coefficients of the power losses
        
        # convert the given power losses(B) in MW from Per_Unit
        
        B *= 0.01
        PD = 150
        DelP = 10
        
        # Error in Delp is set to a high value
        lambda_val = 8
        
        print(' Lambda P1 P3 DP...grad Delambda')
        
        iter = 0
        P = lower_bound.copy()-1
        
        # initially consider power losses as 0;
        Power_loss=0.0
        J=0
        
        def checki():
        
          for i in range(len(P)):
              if(P[i]<lower_bound[i]):
                return True
          for i in range(len(P)):
              if(P[i]>upper_bound[i]):
                return True
          return False
        
        while checki(): # check() or abs(DelP)>=0.001
            iter += 1
            for i in range(len(P)):
              P[i]=(lambda_val-B_O[i])/(2*(gamma[i] +lambda_val*B[i][i])) # eq 7.70
            #calculating power losses
            for i in range(len(P)):
              Power_loss+=B[i][i]*pow(P[i],2);
            DelP = PD + Power_loss - np.sum(P)
            # now it's time to find the value of the lembada
            for i in range(len(P)):
              J+=(gamma[i]+B[i][i]*B_O[i])/(2*(gamma[i]+lambda_val*B[i][i])*(gamma[i]+lambda_val*B[i][i]))
            # print(J)
        
        
            Delambda = DelP / J
            print(Delambda)
            lambda_val += Delambda
            # print(lambda_val)
        
        for i in P:
          print(i, end=' ')
        print(DelP, J, Delambda)
        totalcost = np.sum(alpha + beta * P + gamma * P**2)
        
        return totalcost
    
    lower_Bound_sum = np.sum(np.array(lower_bound))
    end = datetime.now()
    #if lower_Bound_sum >= PD:
     #   ans = "Bounding not possible"
    #else:
    result = str(calculate_dispatch(alpha_array, beta_array, gamma_array, lower_bound, upper_bound)) + '$/hour'
    ans = f'Total fuel cost will be consumed : {result} and Time taken: {(end - start).total_seconds() * 10**3} ms' 
    
    print(ans)
    response = table.put_item(
        Item={
    
        'Time': str(now),
        'Total Cost': result
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(ans)
    }
