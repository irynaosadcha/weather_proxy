# weather_proxy

## For build image
```
docker build -t weather_proxy .
```
## For run container
```
docker run -d --name weather_proxy -p 0.0.0.0:5000:5000 weather_proxy:latest
```
