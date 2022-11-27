# Overview

In this project, we will build  a CI/CD  pipeline from  scraft with  Github Actions and  Azure Pipelines. We will use Github Actions along with a Makefile to perform  to install, verify and test code when submit to Repo Git. Then we will integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

* A [link](https://trello.com/b/0loSqcDf/building-a-ci-cd-pipeline) to a Trello board for the project
* A [link](Plan-Project-CI-CD-Worksheet.xlsx) to a spreadsheet that includes the original and final project plan>

## Instructions

* Architectural Diagram 
![Architectural Diagram](Architectural-Diagram.png)


1. Create the Cloud-Based Development Environment

* Create a GitHub Repo sach as below capture
![GitHub Repo](Create-GitHub-Repo.jpg)

* Create  MakeFile, hello.py, test_hello.py, requirement.txt for GitHubRepo
* Create app.py with Flask framework for for GitHubRepo

* Open Azure Cloud shell
![Azure Bash](Output_open_cloud_shell.jpg)

* Create SSH Key by following command:
```
 ssh-keygen -t rsa
```
![Create SSH Key](Output_create-ssh-key.jpg)

* To show SSH Key we will use below command such as below capture: 
```
cat /home/nguyen/.ssh/id_rsa.pub
```
![Show SSH Key](New%20SSH%20Key.png)

* Then Copy SHH key and add SSH KEY into setting of GitRepo
![Add SSH Key into GitRepo](Oupt-add-ssh-keys-into-Git-setting.jpg)

* To run below git command to clone GitRepo to my workpalce:
```
 git clone https://github.com/hinhnh/Building-a-CI-CD-Pipeline.git
```
![Clone repo](Output_clone-project-code-by-ssh-key.jpg)

2. Running Make tool by step
 - Navigate to Building-a-CI-CD-Pipeline folder wtith commmad: cd Building-a-CI-CD-Pipeline/
 - Then run command "make all" to to install package, verify and test 
 * Output of a test run
 ![Pass test](Output-Test-Pass.jpg)

3. Set up Azure Pipelines point to GitHub Repo.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![Azure Pipelines](Output-Azure-Pipelines.jpg)

4. Running Azure App Service from Azure Pipelines automatic deployment
![Pass Azure Pipelines](Output-run-build-Azure-Pipelines-success.jpg)


5. Project running on Azure App Service will show like below capture:
![Azure App](Output-run-app-service.jpg)


6. To test api prediction from deployed flask app in Azure Cloud Shell.  
![Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
 The output should show such as below capture:
 ![Show port 443](Output_show_port_443.jpg)
 ![Output for running base make_predict_azure_app.sh](Output_show_port_443.jpg)

 7. To use following command to trace streamed log files from deployed application:
 ```
  az webapp log tail -g hinhnh-project2-rg --name my-app-flask
 ``` 
 ![Output-Live-Log-Stream](Output-Live-Log-Stream.jpg)

 8.To test App Service with locust using following command:
 ```
  locust --headless --users 8 --spawn-rate 1 -H https://my-app-flask.azurewebsites.net		
 `` 
![Output-locust](Output-locust.jpg)


## Demo 

https://www.youtube.com/watch



