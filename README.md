### **Lecture Schedule API Documentation**

#### **Base URL**
All API requests are made to:
```
http://[your-server-ip-or-domain]:[port]
```

#### **API Endpoints**

##### **1. Get All Lectures**
- **URL**: `/lectures/`
- **Method**: `GET`
- **Response Format**: JSON
- **Description**: Fetch all lecture details.
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
        "lectures": [
            {
                "id": 1,
                "title": "Intro to Physics",
                "lecturer_name": "Dr. Jane Doe",
                "start_time": "09:00",
                "end_time": "10:00",
                "room": "A101"
            },
            {
                "id": 2,
                "title": "Advanced Math",
                "lecturer_name": "Dr. John Doe",
                "start_time": "10:00",
                "end_time": "11:00",
                "room": "B202"
            }
        ]
    }
    ```
  
##### **2. Add a New Lecture**
- **URL**: `/lectures/`
- **Method**: `POST`
- **Data Params**: 
  - `title`: [string] Title of the lecture.
  - `lecturer_name`: [string] Name of the lecturer.
  - `start_time`: [string] Start time in HH:MM format.
  - `end_time`: [string] End time in HH:MM format.
  - `room`: [string] Room name or number.
- **Response Format**: JSON
- **Description**: Add a new lecture to the schedule.
- **Success Response**:
  - **Code**: 201
  - **Content**:
    ```json
    {
        "message": "Lecture created successfully"
    }
    ```
- **Error Response**:
  - **Code**: 400
  - **Content**:
    ```json
    {
        "error": "Invalid time format"
    }
    ```
  - **Code**: 500
  - **Content**:
    ```json
    {
        "error": "An error occurred, please try again later"
    }
    ```
  
##### **3. Delete a Lecture**
- **URL**: `/lectures/<int:lecture_id>/`
- **Method**: `DELETE`
- **URL Params**: 
  - `lecture_id`: [integer] ID of the lecture to delete.
- **Response Format**: JSON
- **Description**: Delete a lecture from the schedule.
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
        "message": "Lecture deleted successfully"
    }
    ```
- **Error Response**:
  - **Code**: 404
  - **Content**:
    ```json
    {
        "error": "Lecture not found"
    }
    ```
  - **Code**: 500
  - **Content**:
    ```json
    {
        "error": "An error occurred, please try again later"
    }
    ```

---

**Note**: Adjust the error messages and response codes based on your actual implementation in the Flask server. Also, it's a good idea to consistently log errors on the server side to help with troubleshooting and ensure data integrity. Ensure that you verify and test all scenarios with tools like Postman to validate the responses. Finally, securing your API, perhaps with tokens or OAuth, would be crucial when you move to a production environment to safeguard against unauthorized access and modifications.
