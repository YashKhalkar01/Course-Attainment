from locust import HttpUser, task

class FirstLocust(HttpUser):
    @task
    def hello(self):
        self.client.get('/')
        self.client.get('/student')
        self.client.get('/insertMarks')
        self.client.get('/excel')
        self.client.get('/remove')
        self.client.get('/setCourceOutcome')
        self.client.get('/setPaper')
        self.client.get('/displayPaper')
        self.client.get('/updateMarks')
        self.client.get('/change_password')
        self.client.get('/user_logout')