## API this stands for application programming interface. Basically is a collection of pre-defined ways of, 
# or rules for interacting with a web application;s data, usually through HTTP requests and responses. These 
# requests interact with the data, ie read, create, update or delete and then receives back some data as a response. 

## CRUD = create, read, update, delete. 



### Basic RESTful API to manage student data 

from fastapi import FastAPI, Path, HTTPException## This is used to create the API, Path used to extract params from URL, and HTTPException class to be imported so can be used 
from typing import Optional ##Used for optional params
from pydantic import BaseModel ##Used to define data schemes 

app = FastAPI()

#creating an endpoint 
# GET - RETURN INFORMATION
# POST - CREATE SOMETHING NEW 
# PUT - UPDATE THE DATA 
# DELETE - DELETE

## type uvicorn myapi:app --reload to the command line. 
## open the server. 
## type /docs to the enter of the url and it will open api page that will show the  get request, index etc and can test things from here rsther than using postman
## click execute and it provides information within response body  and headers etc 

students = {  ### this is a dictionary soring student information, the student IDs are the keys 
    1: {
        "name": "John",
        "age": 17, 
        "year": "year 12"
    },
    2: {
        "name": "Kate",
        "age": 12,
        "year": "year 7"
    }
}

#### these are all models....

class Student(BaseModel):  ##initial model which sets out how each student should look, ie the info and data type - used for creating a new student 
    name: str
    age: int
    year: str
    
    
class UpdateStudent(BaseModel): ##this model is used for updating data 
    name: Optional[str] = None ## use optional as may only want to change one piece of data so makes optional to update all 
    age: Optional[int] = None
    year: Optional[str] = None
    
## to get to the end point .. could be url www.google.come/students/1.. the below is just a test and not related to student 

@app.get("/")  ##simple endpoint which gives a json response 
def index():
    return {"name": "First Data"} ## return my first data 

#######


@app.get("/get-student/{student_id}")   ## this is how we can get the info on the student by using the student id key - simple version 
def get_student(student_id: int):
    return students[student_id]

## can use above, or below, the below adds a comment within fastAPI which has a comment above the student ID box. 

@app.get("/get-student/{student_id}")  # Get student info by student ID key
def get_student(student_id: int = Path(..., description="The ID of the student you want to view")): ## this version gives a desription of what is required 
    if student_id not in students: #states if student id not in dictionary
        raise HTTPException(status_code=404, detail="Student not found") #error message raised 
    return students[student_id] #otherwise returns student data 

## can add conditions too, like number/index must be greater than0, less than 100 etc etc 

@app.get("/get-by-name")
def get_student(name : Optional[str] = None): ##creates function (for query parameters)  ##if put (name : str=None) will no longer require the name on API 
    for student_id in students: ##looping through a student dictionary with key of student id 
        if students[student_id]["name"] == name: ##if name is equal to name being passed 
            return students[student_id] ##return student details 
    return {"data": "Not found"} ##otheriwse return message that data not found 

@app.get("/get-by-name/{student_id}") ##this one requires student ID, with name as optional. Search by both. 
def get_student(student_id: int, name : Optional[str] = None): ##creates function (for query parameters)  ##if put (name : str=None) will no longer require the name on API 
    for student_id in students: ##looping through a student dictionary with key of student id 
        if students[student_id]["name"] == name: ##if name is equal to name being passed 
            return students[student_id] ##return sudent details 
    return {"data": "Not found"}

### to create 

@app.post("/create-student/{student_id}") ##creates with given id 
def create_student(student_id : int, student : Student): #id should be int, student to be added to Student 
    if student_id in students: 
        return {"error": "Student exists"} ##if student already exists  - error given 
    
    students[student_id] = student #otherwise returns new student 
    return students[student_id]


@app.put("/update-student/{student_id}")  ##to update student with given id 
def update_student(student_id: int, student: UpdateStudent):  #function for student id (nteger), for student to be updated using update student class
    if student_id not in students: #if student id does not exist 
        return {"Error": "Student does not exist"} #error given 
    
    if student.name is not None: #if name not given - then name not updated 
        students[student_id]["name"] = student.name 
     
    if student.age is not None:  #if age not givem age not updated 
        students[student_id]["age"] = student.age   
        
    if student.year is not None:  #if year not given, name not updated 
        students[student_id]["year"] = student.year
    
    return students[student_id] #return student data 

@app.delete("/delete-student/{student_id}") ##to delete a student by id 
def delete_student(student_id: int): #student id should be integer 
    if student_id not in students: #if id does not exist 
        return {"Error": "Student does not exist"} #error raised 
    
    del students[student_id] #otherwise student deleted 
    return {"Message": "Student deleted successfully"} #message given to confirm 

####to run 
# pip install fastapi uvicorn

# uvicorn main: app --reload

# then test via api use / docs at end of url to test

#### CAN ALSO LOOK AT PATCH OR HEAD REQUESTS 


