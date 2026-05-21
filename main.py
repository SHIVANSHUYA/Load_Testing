from locust import HttpUser, task, between
import os

TARGET = os.getenv("TARGET_URL", "xyz.com")

class WebsiteUser(HttpUser):
    host = TARGET
    wait_time = between(1, 3)

    @task(3)
    def homepage(self):
        self.client.get("/", name="GET /")

    @task(2)
    def about(self):
        self.client.get("/about", name="GET /about")

    @task(1)
    def api(self):
        self.client.get("/api/health", name="GET /api/health")
