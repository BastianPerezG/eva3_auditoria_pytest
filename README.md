# eva4_auditoria_pytest
Auditoría de Software – Unidad 4
Este proyecto corresponde a la actividad de Auditoría de Software de la asignatura Tecnologías de Información y Ciberseguridad, Unidad 4.

El objetivo es aplicar buenas prácticas de control de calidad y pruebas unitarias con pytest sobre una aplicación en Python que permite el ingreso y gestión de clientes para fidelización

✅ Estructura del repositorio

    .
    ├── problematica_python.py   # Código original con menú interactivo
    └── test.py                  # código con las pruebas unitarias

✅ Descripción del sistema
  El sistema permite:
  
    - Registrar clientes con sus datos básicos.
    - Modificar datos de clientes existentes.
    - Eliminar clientes del registro.
    - Consultar clientes en distintas vistas.
    - La versión original es interactiva, con menús que piden datos vía consola.

✅ Mejoras para pruebas unitarias

  Para poder aplicar pytest y cumplir los requisitos del proyecto, se crearon tres funciones adicionales (helpers) en el mismo archivo:

    1.- guardar_datos_cliente()
    2.- aplicar_modificacion_cliente()
    3.- eliminar_datos_cliente()
  
  Estas funciones no usan input() y permiten probar la lógica directamente.

  ✅ Archivos principales
   
    problematica_python.py
    Contiene el sistema completo con el menú de usuario.   
    Incluye las nuevas funciones helpers para pruebas.
    Usa el patrón:
      if __name__ == "__main__":
    Esto permite que pytest pueda importar el módulo sin ejecutar el menú.

✅ test.py
    
    Archivo con 3 funciones de test usando pytest.
    Verifica:
      - Registro de cliente (ingresardatos).
      - Modificación de cliente (modificardatos).
      - Eliminación de cliente (eliminardatos).

✅ Requisitos previos
    
     - Python 3.12 (o compatible)
     - Pytest instalado
        Para instalar pytest:
            pip install pytest

✅ Cómo ejecutar la aplicación normal (interactiva)
     
      Para usar el sistema completo con menú:
            python problematica_python.py

✅ Podrás:
    
    - Iniciar sesión
    - Registrar usuarios
    - Gestionar clientes con el menú

✅ Cómo ejecutar las pruebas unitarias

    Para verificar la calidad del código:
        pytest


✅ Resultado esperado:
        
        collected 3 items
        test.py ...                                           [100%]
        3 passed in 0.0Xs

    Significa que las tres funciones críticas están funcionando correctamente.
        
