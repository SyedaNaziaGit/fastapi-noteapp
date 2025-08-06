from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import notesEntity,noteEntity
from fastapi.responses import Response,HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

note = APIRouter()
note.mount("/static",StaticFiles(directory="static"),name= "static")
templates = Jinja2Templates(directory="templates")
@note.get("/",response_class=HTMLResponse)
async def read_note(request:Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
       newDocs.append({
           "id":doc["_id"],
           "title":doc["title"],
           "description":doc["description"],
           "important":doc["important"]
       })
    return templates.TemplateResponse("index.html",{"request":request,"newDocs":newDocs})

@note.post("/")
async def create_note(request:Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if  formDict.get("important") == "on" else False
    note =conn.notes.notes.insert_one(formDict)
    return {"Success":True}