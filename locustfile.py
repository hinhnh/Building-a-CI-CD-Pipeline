from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "https://my-app-flask.azurewebsites.net:443"
    wait_time = between(5, 10)

    @task
    def task1(self):
        self.client.get("/")
    
    @task
    def task2(self):
        self.client.post("/predict", json={
        "CHAS": {
            "0": 0
        },
        "RM": {
            "0": 6.575
        },
        "TAX": {
            "0": 296
        },
        "PTRATIO": {
            "0": 15.3
        },
        "B": {
            "0": 396.9
        },
        "LSTAT": {
            "0": 4.98
        }
        })