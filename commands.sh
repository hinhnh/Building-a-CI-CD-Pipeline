az group create -l eastus2 -n "hinhnh-project2-rg"
az webapp up --sku F1 -l eastus2 -g "hinhnh-project2-rg" -n "my-app-flask"