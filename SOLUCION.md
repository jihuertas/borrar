# PASOS

## Pasos iniciales
Lo primero que haremos será crear un entorno virtual con envvirtualwrapper:

```bash
mkvirtualenv tareas
```

Una vez dentro del entorno virtual actualizamos pip
```bash
pip install --upgrade pip
```
Y creamos un archivo **requirements.txt** con los paquetes a instalar. De momento solo Django en su última versión (a 3/11/2023)

```text
Django~=4.2.7
```

Y vamos a instalar los paquetes:

```bash
pip install -r requirements.txt
```

Por último creamos el proyecto
```bash
django-admin startproject todolist
```
