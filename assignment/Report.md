## Cloud Part Report

The database choice was based on the ease of access and usage for everyone in the project. This choice was the familiar Google Sheets.

Using Google App Scripts, a POST endpoint was created for uploading the data. The data is sent as a string in the JSON format. Specifically, the parameters: score, max, average, and min are required.

This endpoint is: https://script.google.com/macros/s/AKfycbzQzmRrAnOQBMbUzcBY5DiffUTnwJNcg2bsnLVUCQ08PEB4I-w_K5zg5PeV98uIegm1/exec

The backend code is found here:
![image](https://github.com/user-attachments/assets/ee54ad54-5a77-44a8-ace2-37da75a1c831)

The Google Sheet can be seen here:
![image](https://github.com/user-attachments/assets/cd6ce610-459a-4618-9c5c-c6214713d2fc)

Each entry contains the data and the time of the request. As can be seen, the edge case of 0 score is also handled(this caused some bugs and was fixed). 



https://github.com/user-attachments/assets/242626cc-ca1a-4a69-9086-6d93df4d2daa

