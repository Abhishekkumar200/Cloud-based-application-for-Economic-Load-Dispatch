import json
import boto3
import numpy as np

def lambda_handler(event, context):
    # TODO implement
    
    lower_bound = np.array([200, 150, 100])
    PD = 975
    ans = ''
    
    def calculate_dispatch():
        alpha = np.array([500, 400, 200])
        beta = np.array([5.3, 5.5, 5.8])
        gamma = np.array([0.004, 0.006, 0.009])
        lower_bound = np.array([200, 150, 100])
        upper_bound = np.array([450, 350, 225])
        
        PD = 975  # demanded load
        Delp = 10
        # Error in Delp is set to a high value
        lambda_val = 6
        
        iter = 0
        DelP = 1  # Initialize DelP
        P = np.array(lower_bound) + 1
        # global iter, DelP, P, lambda_val  # Use global instead of nonlocal
        while abs(DelP) > 0.001 and (all(lower_bound <= P) and all(P <= upper_bound)):
            iter += 1
    
            P = (lambda_val - np.array(beta)) / (2 * np.array(gamma))
    
            # Clip P values to be within the bounds
    
            for i in range(len(P)):
                if P[i] > upper_bound[i]:
                    P[i] = upper_bound[i]
    
            for i in range(len(P)):
                if P[i] < lower_bound[i]:
                    P[i] = lower_bound[i]
    
            DelP = PD - np.sum(P)
    
            J = np.sum(1 / (2 * np.array(gamma)))  # Gradient sum
    
            Delambda = DelP / J
    
            # if DelP <= 0.001:
            #     print([lambda_val, P[0], P[1], P[2], DelP, J, Delambda])
    
            lambda_val += Delambda
    
        totalcost = np.sum(np.array(alpha) + np.array(beta) * P + np.array(gamma) * P**2)
        
        return 'Total fuel cost will be consumed :' + str(totalcost) + '$/hour'
    
    lower_Bound_sum = np.sum(np.array(lower_bound))
    if lower_Bound_sum >= PD:
        ans = "Bounding not possible"
    else:
        ans = calculate_dispatch()
    
    return {
        'statusCode': 200,
        'body': json.dumps(ans)
    }
