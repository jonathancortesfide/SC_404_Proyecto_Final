# 🏨 Sistema de Gestión de Reservas - Proyecto Final (SC-404)

Este es un proyecto desarrollado en **Django** como parte del curso de *Lenguajes de Bases de Datos*. El objetivo es crear una plataforma para la administración de un hotel que permita gestionar habitaciones, hoteles, actividades, empleados, suministros y clientes.

---

## 🚀 Tecnologías Utilizadas

- **Python 3.13**
- **Django 5.x**
- **Bootstrap 5** (Frontend)
- **SQLite / Oracle** (Dev/Prod)
- **HTML5 y CSS3**
- **Git / GitHub**

---

## ⚙️ Funcionalidades Principales

### 🏨 Gestión de Hoteles (`Hotels`)
- Administración de hoteles.
- Cada hotel tiene:
  - Nombre.
  - Descripción.

### 🛏️ Gestión de Habitaciones (`Rooms`)
- Crear, editar, eliminar y listar habitaciones.
- Cada habitación está asociada a:
  - Un **Hotel**.
  - Una **Categoría de Habitación** (`RoomCategory`).
  - Un número de camas.
  - Un precio por noche.

### 📦 Suministros (`Supplies`)
- Módulo preparado para administrar inventario del hotel.

### 🧍 Empleados (`Employees`)
- Registro y administración del personal del hotel.

### 🧑‍🤝‍🧑 Clientes (`Customers`)
- Almacén de clientes y sus reservas.

### 🎯 Actividades (`Activities`)
- Administración de actividades dentro del hotel (piscina, tours, etc).

---

## 🔐 Autenticación

> **Superusuario** requerido para acceder a Django Admin (previo a un manejo por base de datos directo):

```bash
python manage.py createsuperuser
