# Not DCH - a dynamic and containerized software security learning platform!

Visit https://jake-cloud.github.io/GitPagesTesting/index.html for more information about our project. 

## Run from Docker!!

After installing Docker, run the following commands to get set up. 

```sh
git clone https://github.com/zmweske/cs495-s22.git
cd cs495-s22/
docker-compose up -d
```

Visit http://localhost:8000 in your browser and start testing the application!

There are several vulnerabilities throughout the website, and you need to find them! Each will have a flag associated with it that you can look up in the local database to tell you what vulnerability it is associated with. 

### To remove/uninstall:
```sh
# cd cs495-s22/
docker-compose down
cd ..
rm -r ./cs495-s22/
```

## Vulnerabilities Baked In!
Basic vulnerabilities
- [x] SQLi for first user access
- [x] SQLi for admin access
- [x] leaked creds

Password vulnerabilities
- [ ] SQLi password extraction
- [x] plaintext pwds
- [ ] simple hashed pwds
- [ ] complex hashed pwds
- [ ] salted+hash pwds

Framework vulnerabilities
- [ ] brute force login (rate limiting)
- [x] Error information gathering
- [ ] Reset password info recon
