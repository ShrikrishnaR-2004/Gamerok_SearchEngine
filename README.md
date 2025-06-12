

# 🎮 Gamerok - Game Discovery Platform

**Gamerok** is a full-stack gaming discovery platform built with **Flask**. It integrates with the **RAWG API** and other sources to let users explore games, watch trailers, read and write reviews, and manage favorites — all with secure login options including Google OAuth.

---

## 🌟 Key Features

- 🔍 **Game Search**  
  Search games by name with dynamic suggestions and filters (genre, rating, etc.).

- 🎥 **Game Detail Pages**  
  See game descriptions, trailers, screenshots, and links to official download platforms.

- 🧠 **User Account System**  
  Register or login with email-password or Google account via OAuth 2.0.

- 📝 **User Reviews**  
  Post, edit, and delete reviews for any game.

- ❤️ **Favorites & History**  
  Mark favorites and view your search history across sessions.

- 📰 **Gaming News & Updates**  
  Stay updated with the latest news pulled via API or feeds.

- 🧾 **Credits & Contact Page**  
  Contains contributor names and ways to get in touch.

---

## 🧰 Tech Stack

| Layer        | Tech Used                              |
|--------------|-----------------------------------------|
| **Backend**  | Python, Flask, Flask-Login, Flask-OAuth |
| **Frontend** | HTML, CSS, JavaScript, Jinja2           |
| **Database** | MySQL (user data), MongoDB (media data) |
| **APIs**     | RAWG, YouTube Data API, Google OAuth    |
| **Tools**    | Tesseract OCR, OpenCV, Flask-Migrate    |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gamerok.git
cd gamerok
````

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a `.env` file in the root directory and add:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
MYSQL_URI=mysql+pymysql://username:password@localhost/gamerok_db
MONGO_URI=mongodb://localhost:27017/gamerok
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 5. Initialize MySQL Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the app

```bash
flask run
```

Visit your app at: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
gamerok/
├── app.py
├── .env
├── requirements.txt
├── README.md
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── game.py
│   │   ├── review.py
│   │   └── __init__.py
│   │
│   ├── auth/
│   │   ├── routes.py
│   │   ├── forms.py
│   │   ├── google_auth.py
│   │   └── __init__.py
│   │
│   ├── main/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── user/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── search/
│   │   ├── text.py
│   │   ├── image.py
│   │   ├── video.py
│   │   ├── voice.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── game_api.py
│   │   ├── vision_api.py
│   │   ├── video_frame.py
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── search.html
│   │   ├── profile.html
│   │   ├── contact.html
│   │   └── game_detail.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       │   └── voice.js
│       ├── uploads/
│       └── img/
│
├── migrations/
└── tests/
```

---

## 📡 APIs Used

* [RAWG API](https://rawg.io/apidocs) – Game metadata
* [YouTube Data API](https://developers.google.com/youtube/v3) – Trailers, gameplay
* Google OAuth 2.0 – Login
* Google Vision / Tesseract – Text extraction from images (optional)

---

## 🧪 Tests

You can write tests in the `tests/` folder. Example:

```bash
pytest tests/
```

---

## 📦 Deployment

### Free Hosting Options:

* **Render**
* **Railway**
* **Vercel (Frontend only + Backend as function)**
* **Fly.io**

**Database Hosting:**

* [MongoDB Atlas](https://www.mongodb.com/atlas/database)
* [PlanetScale](https://planetscale.com/) (MySQL cloud)
* [ElephantSQL](https://www.elephantsql.com/) (PostgreSQL)

---

## 🙌 Credits

Built by:

* Shrikrishna R

Special thanks to:

* [RAWG](https://rawg.io/)
* Flask & Open Source Libraries

---

## 📬 Contact

Reach us via the **Contact Us** page in the app or open an issue in this repository.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).




