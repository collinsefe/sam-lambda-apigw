import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    # Get the length and width parameters from the event object. The 
    # runtime converts the event object to a Python dictionary
    # length = event['length']
    # width = event['width']

    length = 6
    width = 7
    
    # Calculate the area
    area = calculate_area(length, width)
    print(f"The area is {area}")
        
    logger.info(f"CloudWatch logs group: {context.log_group_name}")
    
    # Prepare the response data
    data = {"Hello everyone, The area of the Land is approximately = ": area}
    
    # Return the proper response for Lambda Proxy Integration
    return {
        'statusCode': 200,  # HTTP status code
        'body': json.dumps(data),  # The body should be a JSON string
        'headers': {
            'Content-Type': 'application/json'  # Ensure content type is JSON
        }
    }

def calculate_area(length, width):
    return length * width