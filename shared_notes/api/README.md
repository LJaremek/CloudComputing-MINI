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
}
```

### Delete Note
* **URL**: `/api/delete_note/<note_id>`
* **Method**: `DELETE`
* **Description**: Delete note.
* **Request Body**:
```json
{
    "id_note": 1
}
```

### Delete User
* **URL**: `/api/delete_user/<note_id>`
* **Method**: `DELETE`
* **Description**: Delete user.
* **Request Body**:
```json
{
    "id_user": 1
}
```

### Delete Shared Note
* **URL**: `/api/delete_shared_note/<shared_note_id>`
* **Method**: `DELETE`
* **Description**: Delete shared note.
* **Request Body**:
```json
{
    "shared_note_id": 1
}
```

### Share Note
* **URL**: `/api/share_note/`
* **Method**: `POST`
* **Description**: Share a note with another user.
* **Request Body**:
```json
{
    "id_user": 2,
    "id_note": 1,
    "permission_type": "read"
}
```
