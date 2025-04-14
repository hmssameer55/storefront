from locust import HttpUser, task, between
from random import randint

class BrowserProducts(HttpUser):
    wait_time = between(1, 5) # wait time between 1 and 5 seconds between each task

    @task #(2) # 20% of the time
    def view_products(self):
        collection_id = randint(2, 6)
        self.client.get(f"/store/products/?collection_id={collection_id}", name="/store/products/")

    @task #(1) # 10% of the time
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(f"/store/products/{product_id}/", name="/store/products/[product_id]/")
        

    @task
    def say_hello(self):
        self.client.get("/playground/hello/")
        