# Usage Instructions

Follow these steps to use the Docker container `sebbustam/wallmartchallenge:v1`

1. Run the following command to create and run the container:

    `docker run -dit -p 80:80 --name challenge sebbustam/wallmartchallenge:v1`

2. Once this command be execute with succesfull you could test with:

   `curl -sL http://localhost | base64 -d`
3. You should see my name decoded
