# Setting up a Databricks Account
We'll be using a Databricks for many of our exercises. If you already have an account or access to a workspaces, there's nothing for you to do here! Else, follow the instructions below to create a Databricks account. 

## Create a Databricks Account
1. Navigate the [Databricks Login Page](https://accounts.cloud.databricks.com/login)
2. Login with your existing Databricks account (or click **Signup** to create one)

   <img src="./assets/databricks-signup.png" alt="databricks-signup.png" width="500"/>

3. Choose your Cloud Provider. If you don't already have a Cloud Provider account somewhere, please [set one up](#set-up-a-cloud-provider)

   <img src="./assets/databricks-choose-cloud-provider.png" alt="databricks-choose-cloud-provider.png" width="200"/>

4. Choose a workspace name

5. You will have set everything up properly if you see an entry under [workspaces](https://accounts.cloud.databricks.com/workspaces)

## Set up a Cloud Provider
There are three Cloud Providers that Databricks supports: AWS, Azure, and Google Cloud Platform and you'll need one of these to set up a Databricks account. These Cloud Providers have a free trial if this is the first time that you're signing up for them. The expected compute and storage required for these exercises are minimal but it is your responsibility to keep an eye on the workloads that you create and that your clusters are shut down when you're done using them. 

* [Set up an AWS Account](https://aws.amazon.com/free/)
* [Set up an Azure Account](https://azure.microsoft.com/en-gb/free/)
* [Set up a GCP Account](https://console.cloud.google.com/)

## FAQ
### Why aren't we using the Community Edition?
We ran into several consistency issues in the Community Edition such that the same notebook deployed in different regions or clusters would result in different behaviour, particularly around mounting files that are required for these exercises. Some exercises, as a result, became un-runnable. After trialling the Community Edition several times, we concluded that the pay-as-you go version of Databricks provided more consistent behaviour and a better experience for learning despite the added complexity of signing up for a Cloud Provider. You're welcome to try the Community Edition, but we expect you experience similar degraded effects.