# Overview

In this project, we will build  a CI/CD  pipeline from  scraft with  Github Actions and  Azure Pipelines.We will use Github Actions along with a Makefile to perform  to install, verify and test code when submit to Repo Git. Then we will integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

* A [link](https://trello.com/b/0loSqcDf/building-a-ci-cd-pipeline) to a Trello board for the project
* A [link](Plan Project CI-CD Worksheet.xlsx) to a spreadsheet that includes the original and final project plan>

## Instructions

* Architectural Diagram 
![Architectural Diagram](Architectural-Diagram.png)


* Project running on Azure App Service
![Azure App](Output-run-app-service.jpg)

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

https://www.youtube.com/watch?v=CVPaiFHmcYA



