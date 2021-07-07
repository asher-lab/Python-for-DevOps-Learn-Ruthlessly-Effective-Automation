On Docker:

Premise back then is Virtualization software are expensive. Since running
applications on top of it will add to the cost. VMWare + running application. 
That's why to give the best bang for the buck is to use containers.
Using a Docker  enginer/daemon resources will be easily split up to your application on which efficiency of resources are handled properly.

<br><br>

The filesystem-level object that encapsulates the
application is called a Docker image. When you run the image, it becomes
a Docker container.

<br><br>

Docker containers provide more isolation and resource control than
regular Linux processes, but provide less than full-fledged virtual
machines would. To achieve these properties of isolation and resource
control, the Docker engine makes use of Linux kernel features such as
namespaces, control groups (or cgroups), and Union File Systems
(UnionFS).

<br><br>
The main advantage of Docker containers is portability. Once you create a
Docker image, you can run it as a Docker container on any host OS where
the Docker server-side daemon is available. These days, all the major
operating systems run the Docker daemon: Linux, Windows, and macOS.
<br><br>

<h1>Creating, Building, Running, and Removing
Docker Images and Containers</h1>

<br><br>

$ cat app.py
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! (from a Docker container)'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')```

<br><br>

$ cat requirements.txt
```
Flask==1.0.2```

$ cat Dockerfile
```
FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]```

<br><br>
To create the Docker image for this application, run docker build:<br>
```$ docker build -t hello-world-docker .```

*I have not yet read the full section of Docker, Kubernetes etc. I can go back here. 