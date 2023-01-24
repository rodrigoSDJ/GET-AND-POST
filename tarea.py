#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn 3_crud:app --reload-
#{"id"="3","Name":"Alfredo", "LastName":"Garcia", "Age":"30"}
#Definimos nuestra entidad: user

@app.get("/usersjson")
async def usersjson():
     return [{"Name":"Owens", "LastName":"Harris", "Age":"22", "Sex":"male", "Supervided":"0"},
            {"Name":"Owens", "LastName":"Harris", "Age":"22", "Sex":"male", "Supervided":"0"},
            {"Name":"Owens", "LastName":"Harris", "Age":"22", "Sex":"male", "Supervided":"0"},]
            
             
class User(BaseModel):
    id:int
    Name: str
    LastName:str
    Age:int
    Sex: str
    Survived:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  

users_list= [User(id=1,Name="Owens", LastName="Harris", Age="22", Sex="male", Survived="0"),
            User(id=2,Name="Jhon", LastName="Bradley", Age="38", Sex="female" , Survived="1"),
            User(id=3,Name="Laina", LastName="Heikkinen", Age="26", Sex="female" , Survived="1"),
            User(id=4,Name="Henry", LastName="Allen", Age="35", Sex="male" , Survived="0"),
            User(id=5,Name="James", LastName="Mooran", Age="34", Sex="male" , Survived="1"),
            User(id=6,Name="Timothy", LastName="Mcmarthy", Age="54", Sex="male" , Survived="0"),
            User(id=7,Name="Elizabeth", LastName="Bonnell", Age="58", Sex="female" , Survived="1"),
            User(id=8,Name="William", LastName="Henry", Age="20", Sex="male" , Survived="1"),
            User(id=9,Name="Johan", LastName="Andersson", Age="39", Sex="male" , Survived="0"),
            User(id=10,Name="Adolfina", LastName="Vestrom", Age="14", Sex="female" , Survived="0"),
            User(id=11,Name="Mary", LastName="Hewlett", Age="55", Sex="female" , Survived="1"),
            User(id=12,Name="Eugene", LastName="Rice", Age="17", Sex="female" , Survived="0"),
            User(id=13,Name="Fatima", LastName="Masselmani", Age="20", Sex="female" , Survived="0"),
            User(id=14,Name="Joseph", LastName="Fynney", Age="21", Sex="male" , Survived="0"),
            User(id=15,Name="Anna", LastName="Mcgowan", Age="23", Sex="female" , Survived="1"),
            User(id=16,Name="Danira", LastName="Palsson", Age="25", Sex="female" , Survived="1"),
            User(id=17,Name="Alexander", LastName="Fortune", Age="28", Sex="male" , Survived="0"),
            User(id=18,Name="Lalio", LastName="Todoroff", Age="30", Sex="male" , Survived="1"),
            User(id=19,Name="Manuel", LastName="Uruchutu", Age="31", Sex="male" , Survived="1"),
            User(id=20,Name="Agatha", LastName="Glyn", Age="33", Sex="female" , Survived="0"),
            User(id=21,Name="Jamila", LastName="Nicola", Age="40", Sex="female" , Survived="1"),
            User(id=22,Name="Theodor", LastName="Kraeff", Age="43", Sex="male" , Survived="1"),
            User(id=23,Name="Denis", LastName="Lennon", Age="45", Sex="female" , Survived="0"),
            User(id=24,Name="Richard", LastName="Cater", Age="36", Sex="male" , Survived="1"),
            User(id=25,Name="Emily", LastName="Rugg", Age="57", Sex="female" , Survived="1") ]


#***Get
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


#***Get con Filtro Query
@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@app.put("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@app.delete("/usersclass/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1