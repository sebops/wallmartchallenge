# Usage Instructions

Follow these steps to use the Docker container `sebbustam/wallmartchallenge:v1`

1. Run the following command to create and run the container:

```
	docker run -dit sebbustam/wallmartchallenge:v1 -p 80:80 --name challenge
```

2. Once this command be execute with succesfull you could test with:

   ```bash
   curl -sL http://localhost | base64 -d
   ```
