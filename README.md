# ml_projects
This is first ml projec t

create a virtual environment by:
```
conda create -p env_name python==3.8 -y
```

activate virtual environment by:
```
 conda activate env_name/
```

To add files to git
```
git add.
```

Or
```
git add <file_name>
```

To ifnore the file or folder write its name in .gitignore

To check the git status
```
git status
```

To check the versions

```
git log
```

To create versions/commit/save the changes to git use
```
git commit -m <message>
```
 To send the changes to the git
 ```
 git push origin main
 ```

 To check remote url: basicallu origin save the link of github repo tp fetch or push the changes

 ```
git remote -v
 ```
  
TO check the branch

```
git branch
```
To setup cI/CD pipeline we require 3 information from Heruku
```
1 HERUKU_EMAIL_ID
2)HERUKU_API-KEY
3)HERUKU_APP_NAME
```

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> . 
```
> docker image name should always be in lowercasef
