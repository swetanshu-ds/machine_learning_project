##  machine_learning_project

## Start machine learning project

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS CODE IDE](https://code.visualstudio.com/download)
4. [Git CLI](https://git-scm.com/downloads)
5. [Git command documentation](https://docs.github.com/en/get-started/using-git/about-git)




my machine learning project

```
Creating conda environment

```
OR
```
conda activate venv/
```
```
pip install -r requirements.txt
```


TO add file to git 

```
git add .
```
OR

```
git add <file_name>
```

> Note: To ignore file or folder from git we can use write name of file/folder in .gitignore


To check the git status

``` 
git status
```

To check all versions maintained by git 
``` 
git log
```

To create version/commit all changes by git

```
git commit -m "message"
```


To send version/changes to github

``` 
git push origin main
```

TO check for which git url you are doing something

```
git remote -v

```
```
Hello 
I am learning git commands

```


To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = sprajpan123@gmail.com
2. HEROKU_API_KEY = **************************
3. HEROKU_APP_NAME =  my_dust



BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
```
> Note: Image name for docker must be lowercase
```

To list docker images
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 6dd5f3b8acaf
```

To check running containers in docker
```
docker ps
```


To stop any container
```
docker stop <container_id>
```



.gitignore
```
All these files that we do not want to be tracked by git ,we write their names in
.gitignore
```

.dockerignore
```
all those files that we do not want to use for the docker ,specify in the dockerignore

```


