# Django server API endpoints

### List users
* **URL**: `/api/users/`
* **Method**: `GET`
* **Description**: List users.
* **Example result**:
```json
[
    {
        "id_user": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "pass_hash": "hashedpassword"
    }
]
```

### List notes
* **URL**: `/api/notes/`
* **Method**: `GET`
* **Description**: List notes.
* **Example result**:
```json
[
    {
        "id_note": 1,
        "id_user": 1,
        "content": "SUPER CONTENT CZAISZ?",
        "created_at": "2024-05-23T19:33:48.511940Z",
        "shared_at": "2024-05-23T19:33:48.511956Z"
    }
]
```

### CREATE USER
* **URL**: `/api/create_user/`
* **Method**: `POST`
* **Description**: Creates a new user.
* **Request Body**:
```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "pass_hash": "hashedpassword"
}
```

### CREATE NOTE
* **URL**: `/api/create_note/`
* **Method**: `POST`
* **Description**: Creates a new note.
* **Request Body**:
```json
{
    "id_user": "1",
    "content": "MY note content :3",
    "created_at": <auto_now_add>, // optional
    "shared_at": <auto_now> // optional
}
```
