import problematica_python as app

def setup_function():
    app.clientes.clear()
    app.idcliente = 0

def test_guardar_datos_cliente():
    nuevo_id = app.guardar_datos_cliente(
        run="12345678-9",
        nombre="Juan",
        apellido="Pérez",
        direccion="Calle Falsa 123",
        fono="912345678",
        correo="juan@mail.com",
        tipo="101",
        monto="50000"
    )
    assert nuevo_id == 1
    assert nuevo_id in app.clientes
    cliente = app.clientes[nuevo_id]
    assert cliente[2] == "Juan"
    assert cliente[7] == "101"

def test_aplicar_modificacion_cliente():
    nuevo_id = app.guardar_datos_cliente(
        run="12345678-9",
        nombre="Juan",
        apellido="Pérez",
        direccion="Calle Falsa 123",
        fono="912345678",
        correo="juan@mail.com",
        tipo="101",
        monto="50000"
    )
    nuevos_datos = [
        nuevo_id, "12345678-9", "Pedro", "Gómez", "Nueva 456", 
        "987654321", "pedro@mail.com", "102", "75000", 0
    ]
    resultado = app.aplicar_modificacion_cliente(nuevo_id, nuevos_datos)
    assert resultado is True
    cliente = app.clientes[nuevo_id]
    assert cliente[2] == "Pedro"
    assert cliente[7] == "102"

def test_eliminar_datos_cliente():
    # 1. Crear un cliente primero
    nuevo_id = app.guardar_datos_cliente(
        run="12345678-9",
        nombre="Juan",
        apellido="Pérez",
        direccion="Calle Falsa 123",
        fono="912345678",
        correo="juan@mail.com",
        tipo="101",
        monto="50000"
    )
    assert nuevo_id in app.clientes

    # 2. Eliminarlo
    resultado = app.eliminar_datos_cliente(nuevo_id)
    assert resultado is True
    assert nuevo_id not in app.clientes