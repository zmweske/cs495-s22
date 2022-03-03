# Not DCH - a dynamic and containerized software security learning platform!

## Run from Docker!!

After installing Docker, run the following commands to get set up. 

```sh
git clone https://github.com/zmweske/cs495-s22.git
cd cs495-s22/patient-login
docker-compose up -d
```

Visit [`localhost:8000/login`](http://localhost:8000/login) in your browser and start testing the application!

There are several vulnerabilities throughout the website, and you need to find them! Each will have a flag associated with it that you can look up in the local database to tell you what vulnerability it is associated with. 
