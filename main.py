from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

# ----- CONFIG -----
FULL_NAME = "dudekula_kasim_vali"   # underscores instead of spaces
DOB = "22072004"                    
EMAIL = "kasim.22bcb7285@vitapstudent.ac.in"
ROLL_NUMBER = "22BCB7285"

# ----- Request Model -----
class DataInput(BaseModel):
    data: List[str]

# ----- Helper Functions -----
def process_data(data: List[str]):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0

    for item in data:
        if re.fullmatch(r"-?\d+", item):  
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num
        elif item.isalpha():  
            alphabets.append(item.upper())
        else:  
            special_characters.append(item)

    concat_string = "".join(alphabets)
    reversed_str = concat_string[::-1]
    alt_caps = "".join(
        ch.upper() if i % 2 == 0 else ch.lower()
        for i, ch in enumerate(reversed_str)
    )

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": alt_caps,
    }

# ----- Routes -----
@app.get("/")
def root():
    return {"message": "BFHL API is running. Use POST /bfhl"}

@app.post("/bfhl")
def bfhl_endpoint(request: DataInput):
    try:
        return process_data(request.data)
    except Exception as e:
        return {"is_success": False, "error": str(e)}
