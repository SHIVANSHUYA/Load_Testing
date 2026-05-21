from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "xyz.com"
    wait_time = between(1, 3)

    @task(3)
    def homepage(self):
        with self.client.get("/", catch_response=True) as response:
            print("HOME:", response.status_code)

    @task(2)
    def about(self):
        with self.client.get("/about", catch_response=True) as response:
            print("ABOUT:", response.status_code)

    @task(1)
    def api(self):
        with self.client.get("/api/health", catch_response=True) as response:
            print("API:", response.status_code)
