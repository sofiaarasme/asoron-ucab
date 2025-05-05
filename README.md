# ASORONUCAB Inventory & Sales Management

**Proyecto Universitario** realizado por **Sofía Arasme** y **Romel González**.

## Descripción
AsoRonUCAB es un sistema integral de gestión de datos para una empresa dedicada a la fabricación y venta de ron. Permite administrar inventarios, procesar ventas y compras, gestionar nóminas, usuarios y clientes, así como ofrecer una experiencia de compra en línea a través de un sitio web.

El proyecto está desarrollado con **Django** (backend) y **React** (frontend), integrando funcionalidades clave para la operación diaria y la toma de decisiones estratégicas a través de un dashboard intuitivo.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Instalación](#instalación)
- [Autores](#autores)
- [Licencia](#licencia)

## Características

- **Dashboard Administrativo**: Visión global de KPIs (ventas, compras, inventario, nómina).
- **Gestión de Inventario**: Altas, bajas y ajustes de stock con alertas de bajo inventario.
- **Procesamiento de Ventas**: Creación y seguimiento de facturas, historial de ventas.
- **Módulo de Compras**: Registro de órdenes, proveedores, recepción de productos.
- **Tienda en Línea**: Catálogo de productos, carrito de compras y pasarela de pago.
- **Gestión de Nómina**: Cálculo de salarios y generación de recibos.
- **Administración de Usuarios y Roles**: Control de acceso granular (administrador, vendedor, empleado).
- **Gestión de Clientes**: Perfil de clientes, historial de compras y comunicaciones.

## Tecnologías

- **Backend**: Django, Django REST Framework, PostgreSQL
- **Frontend**: React, React Router, Bootstrap
- **Autenticación**: JWT (JSON Web Tokens)
- **Control de Versiones**: Git, GitHub

## Arquitectura del Proyecto

1. **API REST (Django)**
   - Endpoints para inventario, ventas, compras, nómina, usuarios y clientes.
   - Autenticación y permisos basados en roles.
   - Panel de administración.
2. **Frontend (React)**
   - Dashboard con gráficos (Recharts).
   - Sitio público de e-commerce.
3. **Base de Datos**
   - PostgreSQL como motor de datos.

## Autores
- **Sofía Arasme**
- **Romel González**