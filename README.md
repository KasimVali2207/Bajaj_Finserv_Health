

```markdown
# Bajaj Finserv Health API (BFHL)

## 📌 Project Objective
This project implements a REST API for the **Bajaj Finserv Health Hackathon Challenge**.  
The API processes an array of strings, classifying input into numbers, alphabets, and special characters, while returning additional computed details.

The API is built using **FastAPI** and deployed on **Render**.

---

## 🚀 Hosted API
- **POST Endpoint:**  
```

[https://bajaj-finserv-health-07o6.onrender.com/bfhl](https://bajaj-finserv-health-07o6.onrender.com/bfhl)

````

- **Example cURL Request:**
```bash
curl -X POST "https://bajaj-finserv-health-07o6.onrender.com/bfhl" \
-H "Content-Type: application/json" \
-d '{"data": ["a", "1", "334", "4", "R", "$"]}'
````

* **Example Response:**

  ```json
  {
    "is_success": true,
    "user_id": "dudekula_kasim_vali_22072004",
    "email": "kasim.22bcb7285@vitapstudent.ac.in",
    "roll_number": "22BCB7285",
    "odd_numbers": ["1"],
    "even_numbers": ["334", "4"],
    "alphabets": ["A", "R"],
    "special_characters": ["$"],
    "sum": "339",
    "concat_string": "Ra"
  }
  ```

---

## ⚙️ Features & Logic

* ✅ Accepts an array of strings as input
* ✅ Separates **odd numbers**, **even numbers**, **alphabets**, and **special characters**
* ✅ Returns the **sum of all numbers**
* ✅ Generates a special `concat_string` from alphabets (reverse + alternating case)
* ✅ Every response contains:

  * `user_id` → format `{full_name_ddmmyyyy}` (lowercase)
  * `is_success` → operation status (true/false)

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Hosting:** Render
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
Bajaj_Finserv_Health/
│── main.py            # FastAPI app
│── requirements.txt   # Dependencies
│── README.md          # Project Documentation
```

---

## 🖥 Local Setup & Run

1. Clone the repository:

   ```bash
   git clone https://github.com/KasimVali2207/Bajaj_Finserv_Health.git
   cd Bajaj_Finserv_Health
   ```

2. Create a virtual environment & activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server locally:

   ```bash
   uvicorn main:app --reload
   ```

5. Test API locally:

   ```bash
   curl -X POST "http://127.0.0.1:8000/bfhl" \
   -H "Content-Type: application/json" \
   -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
   ```

---

## 📜 Author

**Name:** Dudekula Kasim Vali
**Email:** [kasim.22bcb7285@vitapstudent.ac.in](mailto:kasim.22bcb7285@vitapstudent.ac.in)
**Roll Number:** 22BCB7285

---

```

---


