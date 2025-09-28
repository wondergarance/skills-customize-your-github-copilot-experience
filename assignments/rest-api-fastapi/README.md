# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Apprendre à créer une API REST simple en Python avec le framework FastAPI. Les élèves découvriront la structure d’une API, la gestion des routes, des requêtes et des réponses JSON.

## 📝 Tasks

### 🛠️ Task 1: FastAPI Setup & First Route

#### Description
Installer FastAPI et Uvicorn, puis créer un fichier Python qui lance une application FastAPI avec une route GET `/hello` qui retourne un message JSON.

#### Requirements
Completed program should:

- Installer FastAPI et Uvicorn
- Créer un fichier Python avec une application FastAPI
- Ajouter une route GET `/hello` qui retourne `{"message": "Hello, world!"}`

### 🛠️ Task 2: Add a Dynamic Route

#### Description
Ajouter une route GET `/greet/{name}` qui retourne un message personnalisé en fonction du nom passé dans l’URL.

#### Requirements
Completed program should:

- Ajouter une route GET `/greet/{name}`
- Retourner un JSON avec le message `Hello, <name>!`
- Gérer au moins deux exemples de noms différents

### 🛠️ Task 3: Create a POST Endpoint

#### Description
Créer une route POST `/items` qui accepte un objet JSON avec un champ `name` et retourne une confirmation avec le nom reçu.

#### Requirements
Completed program should:

- Créer une route POST `/items`
- Accepter un JSON avec le champ `name`
- Retourner un JSON `{"received": "<name>"}`

