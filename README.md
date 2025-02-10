# Welcome Lambda API - AWS SAM

This project uses AWS Serverless Application Model (AWS SAM) to deploy a **Lambda function** triggered by an **API Gateway**. The API responds with a simple welcome message when the `/welcome` endpoint is accessed.

## Overview

This project defines a simple AWS Lambda function triggered by an HTTP request to an API Gateway. The Lambda function calculates and returns a welcome message when called. The SAM template configures:

- A **Lambda function** that handles the GET request at the `/welcome` path.
- A **API Gateway** that routes HTTP requests to the Lambda function.
- **Logging** for monitoring the Lambda function.

## Components

1. **Lambda Function (`WelcomeLambdaFunction`)**:
   - Executes when the `/welcome` endpoint of the API is hit.
   - Responds with a simple JSON message: "Welcome to Cloud Skills Academy".

2. **API Gateway (`MyApi`)**:
   - An API Gateway endpoint exposed to the internet, listening for `GET` requests at the `/welcome` path.

3. **SAM Template (`template.yaml`)**:
   - The SAM template defines the resources and their configurations, including the Lambda function and API Gateway.

## Prerequisites

Before deploying the SAM application, ensure you have the following tools installed:

- **AWS CLI**: Command-line interface for interacting with AWS services.
- **AWS SAM CLI**: Command-line tool for building, testing, and deploying serverless applications.
- **Docker** (for local testing and Lambda container use).

## Getting Started

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install dependencies

Ensure you have the required AWS SAM CLI and Docker installed. You can install AWS SAM CLI by following the instructions in the [AWS documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

### 3. Build the SAM application

Run the following command to build the project:

```bash
sam build
```

This command will package the Lambda function and prepare the resources defined in the `template.yaml` for deployment.

### 4. Deploy the application

To deploy the application to AWS, use the following command:

```bash
sam deploy --guided
```

You will be prompted for various parameters like stack name, region, and permissions. SAM will then create the necessary AWS resources and deploy the application.

### 5. Access the API

After deployment, SAM will output the API Gateway URL. You can access the `/welcome` endpoint by visiting:

```
https://<api-id>.execute-api.<region>.amazonaws.com/prod/welcome
```

You should see a response like:

```json
{
  "The area of the Land is approximately": 600
}
```

### 6. Test the Lambda Function

The Lambda function can also be tested using the API Gateway URL directly in your browser or with tools like **Postman** or **curl**.

## Template Explanation

### AWS Lambda Function (`WelcomeLambdaFunction`)

The Lambda function is defined in the `template.yaml` file with the following properties:

- **FunctionName**: The name of the Lambda function.
- **Handler**: Points to the `lambda_function.lambda_handler` function in the code.
- **Runtime**: Python 3.12 is used for the Lambda runtime environment.
- **MemorySize**: 256 MB.
- **Timeout**: 15 seconds.
- **LoggingConfig**: Configures logs in JSON format.

The Lambda function expects the API Gateway to trigger it when a `GET` request is made to `/welcome`. The function responds with a simple welcome message.

### API Gateway (`MyApi`)

The API Gateway is created using the `AWS::Serverless::Api` resource with the following configuration:

- **EndpointConfiguration**: Set to `REGIONAL` to create a regional API.
- **StageName**: The stage name is `prod` (production).
- **Swagger Definition**: The Swagger file defines the `/welcome` path and the response format.

### SAM Events

The **`Events`** section under `WelcomeLambdaFunction` defines an **API Gateway** event that connects the Lambda function to the `/welcome` endpoint, which triggers the Lambda when a `GET` request is made to that path.

## Cleaning Up

To remove the deployed resources, run the following command:

```bash
sam delete
```

This will remove the Lambda function, API Gateway, and any other resources created during the deployment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
