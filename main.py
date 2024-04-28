#uvicorn main:app --reload
#http://127.0.0.1:8000
import uvicorn
import requests
import json

from fastapi import FastAPI
from pydantic import BaseModel

class Menu(BaseModel):
    name: str
    price: float
    description: str
    categoryName: str

def generate_menu_prompt(menu: Menu):
    menu_prompt = f'다음 메뉴를 등록해줘 메뉴명: {menu.name}, 메뉴 가격: {menu.price}, 메뉴 설명: {menu.description}, 메뉴 카테고리: {menu.categoryName}'
    return menu_prompt

app = FastAPI()

@app.post("/api/menu-register")
async def register_menu(menu: Menu):
    menu_prompt = generate_menu_prompt(menu=menu)
    return menu_prompt
