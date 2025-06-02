from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Tea data model - id, name aur options fields hain
class Tea(BaseModel):
    id: int
    name: str
    options: str

# In-memory list jisme teas store hongi
teas: List[Tea] = []

@app.get("/")
def home():
    return {"message": "Welcome to the Tea API! Use /teas endpoint to manage teas."}

@app.get("/teas")
def get_all_teas():
    # Saare teas return karta hai
    return teas

@app.post("/teas")
def add_new_tea(tea: Tea):
    # List mein naya tea add karta hai
    teas.append(tea)
    return {"message": "Tea added successfully!", "tea": tea}

@app.put("/teas/{tea_id}")
def update_existing_tea(tea_id: int, updated_tea: Tea):
    # Tea ko dhoondh kar update karta hai
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return {"message": "Tea updated successfully!", "tea": updated_tea}
    return {"error": "Tea not found!"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    # Tea ko list se delete karta hai
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            removed_tea = teas.pop(index)
            return {"message": "Tea deleted successfully!", "tea": removed_tea}
    return {"error": "Tea not found!"}
