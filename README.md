# Magical World 🌟

Un sitio web interactivo inspirado en el mundo de Hogwarts, desarrollado en Django. El proyecto incluye autenticación, validaciones en tiempo real y consumo de APIs.

## **Características Principales**

- **Registro de Usuario:** Validación en tiempo real de nombre de usuario, contraseña y correo electrónico.
- **Autenticación:** Inicio de sesión seguro y restricción de acceso a secciones privadas.
- **Consumo de APIs:** Información de personajes, hechizos y profesores usando servicios externos.
- **Filtros Dinámicos:** Permite filtrar personajes vivos/muertos y profesores activos/inactivos.
- **Frontend Responsivo:** Diseño estilizado con Materialize CSS y animaciones interactivas.

---

## **Requisitos**

Antes de iniciar, asegúrate de tener instalado lo siguiente:

- **Python 3.8+**
- **Django 3.x o superior**
- **pip** (Gestor de paquetes de Python)

---

## **Instalación y Configuración**

### **1. Clonar el Repositorio**

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/magical-world.git
cd magical-world
```

### **2. Crear y Activar un Entorno Virtual**

**Linux/MacOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Instalar las Dependencias**

Instala todas las librerías necesarias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si no tienes `requirements.txt`, instala manualmente:

```bash
pip install django requests
```

### **4. Configurar la Base de Datos**

Aplica las migraciones para crear la base de datos SQLite:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Crear un Superusuario**

Crea un usuario administrador para el panel de Django:

```bash
python manage.py createsuperuser
```

Ingresa un nombre de usuario, correo electrónico y contraseña.

### **6. Ejecutar el Servidor**

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Accede a la aplicación en tu navegador:

```bash
http://127.0.0.1:8000/
```