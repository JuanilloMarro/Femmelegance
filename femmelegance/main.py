import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import sqlite3 as sql


class SqldatabaseReferencias:

    def __init__(self):
        self.connection = sql.connect("referencias.db")

    def creatDB(self):
        self.connection.commit()
        self.connection.close()

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''CREATE TABLE referencias (
                codigo text,
                nombre_de_quien_refiere text,
                referido text,
                telefono text,
                programacion_cita text,
                parentezco text
            )'''
        )
        self.connection.commit()
        self.connection.close()

    def insertRow(self, codigo, nombre_de_quien_refiere, referido, telefono, programacion_cita, parentezco):
        cursor = self.connection.cursor()
        instruccion = f"INSERT INTO referencias VALUES ('{codigo}', '{nombre_de_quien_refiere}', '{referido}', " \
                      f"'{telefono}', '{programacion_cita}','{parentezco}')"
        cursor.execute(instruccion)
        self.connection.commit()

    def updateFields(self, codigo, nombre_de_quien_refiere, referido, telefono, programacion_cita, parentezco):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE referencias SET nombre_de_quien_refiere = '{nombre_de_quien_refiere}' " \
                      f"WHERE codigo like '{codigo}%' "
        instruccion_2 = f"UPDATE referencias SET referido = '{referido}' WHERE codigo like '{codigo}%' "
        instruccion_3 = f"UPDATE referencias SET telefono = '{telefono}' WHERE codigo like '{codigo}%'  "
        instruccion_4 = f"UPDATE referencias SET programacion_cita = '{programacion_cita}' WHERE codigo " \
                        f"like '{codigo}%'  "
        instruccion_5 = f"UPDATE referencias SET parentezco = '{parentezco}' WHERE codigo like '{codigo}%' "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        cursor.execute(instruccion_5)
        self.connection.commit()

    def deleteRow(self, codigo):
        cursor = self.connection.cursor()
        instruccion = f"DELETE FROM referencias WHERE codigo like '{codigo}%'"
        cursor.execute(instruccion)
        self.connection.commit()

    def referencias(self, tablewidgetreferencias):
        cursor = self.connection.cursor()
        instruccion = f"SELECT * FROM referencias"
        result = cursor.execute(instruccion)
        tablewidgetreferencias.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tablewidgetreferencias.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablewidgetreferencias.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def getNumRows(self):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM referencias"
        cursor.execute(query)
        num_rows = cursor.fetchone()[0]
        cursor.close()
        return num_rows


class SqldatabaseClientesPreferencias:

    def __init__(self):
        self.connection = sql.connect("preferencias_clientes.db")

    def createDB(self):
        self.connection.commit()
        self.connection.close()

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''CREATE TABLE preferencias_clientes (
                nombre text,
                intereses text,
                compartir_con text,
                lista_de_deseos text,
                cotizacion text
            )'''
        )
        self.connection.commit()
        self.connection.close()

    def insertRow(self, nombre, intereses, compartir_con, lista_de_deseos, cotizacion):
        cursor = self.connection.cursor()
        instruccion = f"INSERT INTO preferencias_clientes VALUES ('{nombre}', '{intereses}', '{compartir_con}'" \
                      f", '{lista_de_deseos}', '{cotizacion}')"
        cursor.execute(instruccion)
        self.connection.commit()

    def updateFields(self, nombre, intereses, compartir_con, lista_de_deseos, cotizacion):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE preferencias_clientes SET intereses = '{intereses}' WHERE nombre like '{nombre}%'  "
        instruccion_2 = f"UPDATE preferencias_clientes SET compartir_con = '{compartir_con}' WHERE nombre " \
                        f"like '{nombre}%'  "
        instruccion_3 = f"UPDATE preferencias_clientes SET lista_de_deseos = '{lista_de_deseos}' WHERE nombre " \
                        f"like '{nombre}%'  "
        instruccion_4 = f"UPDATE preferencias_clientes SET cotizacion = '{cotizacion}' WHERE nombre like '{nombre}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        self.connection.commit()

    def deleteRow(self, nombre):
        cursor = self.connection.cursor()
        instruccion = f"DELETE FROM preferencias_clientes WHERE nombre like '{nombre}%'"
        cursor.execute(instruccion)
        self.connection.commit()

    def preferencias(self, tablewidgetpreferencias):
        cursor = self.connection.cursor()
        instruccion = f"SELECT * FROM preferencias_clientes"
        result = cursor.execute(instruccion)
        tablewidgetpreferencias.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tablewidgetpreferencias.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablewidgetpreferencias.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


class SqldatabaseCredito:
    def __init__(self):
        self.connection = sql.connect("credito.db")

    def createDB(self):
        self.connection.commit()
        self.connection.close()

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''CREATE TABLE credito (
                codigo_credito text,
                nombre_cliente text,
                producto text,
                forma_de_pago text,
                tipo_de_pago text,
                valor_de_credito float,
                cuotas float,
                plazos integer,
                pago_1 float,
                fecha_primer_pago text,
                pago_2 float,
                fecha_segundo_pago text,
                pago_3 float,
                fecha_tercer_pago text,
                saldo_pendiente float,
                egresos float,
                saldo float,
                estado text
            )'''
        )
        self.connection.commit()
        self.connection.close()

    def insertRow(
            self, codigo_credito, nombre_cliente, producto,
            forma_de_pago, tipo_de_pago, valor_de_credito,
            cuotas, plazos, pago_1, fecha_primer_pago, pago_2,
            fecha_segundo_pago, pago_3, fecha_tercer_pago, saldo_pendiente,
            egresos, saldo, estado
    ):
        cursor = self.connection.cursor()
        instruccion = f"INSERT INTO credito VALUES ('{codigo_credito}', '{nombre_cliente}', '{producto}', " \
                      f"'{forma_de_pago}', '{tipo_de_pago}'," \
                      f" {valor_de_credito}, {cuotas}, {plazos}, {pago_1}, '{fecha_primer_pago}', {pago_2}," \
                      f" '{fecha_segundo_pago}', {pago_3}," \
                      f"'{fecha_tercer_pago}', {saldo_pendiente}, {egresos}, {saldo}, '{estado}')"
        cursor.execute(instruccion)
        self.connection.commit()

    def updateFields_pago1(self, codigo, pago_1, fecha_primer_pago, saldo_pendiente, estado):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE credito SET pago_1 = {pago_1} WHERE codigo_credito like '{codigo}%' "
        instruccion_2 = f"UPDATE credito SET fecha_primer_pago = '{fecha_primer_pago}' WHERE codigo_credito " \
                        f"like '{codigo}%' "
        instruccion_3 = f"UPDATE credito SET saldo_pendiente = {saldo_pendiente} WHERE codigo_credito " \
                        f"like '{codigo}%'  "
        instruccion_4 = f"UPDATE credito SET estado = '{estado}' WHERE codigo_credito like '{codigo}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        self.connection.commit()

    def updateFields_pago2(self, codigo, pago_2, fecha_segundo_pago, saldo_pendiente, estado):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE credito SET pago_2 = {pago_2} WHERE codigo_credito like '{codigo}%' "
        instruccion_2 = f"UPDATE credito SET fecha_segundo_pago = '{fecha_segundo_pago}' WHERE codigo_credito like '{codigo}%' "
        instruccion_3 = f"UPDATE credito SET saldo_pendiente = {saldo_pendiente} WHERE codigo_credito like '{codigo}%'  "
        instruccion_4 = f"UPDATE credito SET estado = '{estado}' WHERE codigo_credito like '{codigo}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        self.connection.commit()

    def updateFields_pago3(self, codigo, pago_3, fecha_tercer_pago, saldo_pendiente, estado):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE credito SET pago_3 = {pago_3} WHERE codigo_credito like '{codigo}%' "
        instruccion_2 = f"UPDATE credito SET fecha_tercer_pago = '{fecha_tercer_pago}' WHERE codigo_credito like '{codigo}%' "
        instruccion_3 = f"UPDATE credito SET saldo_pendiente = {saldo_pendiente} WHERE codigo_credito like '{codigo}%'  "
        instruccion_4 = f"UPDATE credito SET estado = '{estado}' WHERE codigo_credito like '{codigo}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        self.connection.commit()

    def getpago_1(self, codigo):
        cursor = self.connection.cursor()
        query = f"SELECT pago_1 FROM credito WHERE codigo_credito like '{codigo}%'"
        cursor.execute(query)
        pago_1 = cursor.fetchone()[0]
        return pago_1

    def getpago_2(self, codigo):
        cursor = self.connection.cursor()
        query = f"SELECT pago_2 FROM credito WHERE codigo_credito like '{codigo}%'"
        cursor.execute(query)
        pago_2 = cursor.fetchone()[0]
        return pago_2

    def getpago_3(self, codigo):
        cursor = self.connection.cursor()
        query = f"SELECT pago_3 FROM credito WHERE codigo_credito like '{codigo}%'"
        cursor.execute(query)
        pago_3 = cursor.fetchone()[0]
        return pago_3

    def get_credito(self, codigo):
        cursor = self.connection.cursor()
        query = f"SELECT valor_de_credito FROM credito WHERE codigo_credito like '{codigo}%'"
        cursor.execute(query)
        credito = cursor.fetchone()[0]
        return credito

    def getNumRows(self):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM credito"
        cursor.execute(query)
        num_rows = cursor.fetchone()[0]
        cursor.close()
        return num_rows

    def credito(self, twcredito):
        cursor = self.connection.cursor()
        instruccion = f"SELECT * FROM credito"
        result = cursor.execute(instruccion)
        twcredito.setRowCount(0)

        for row_number, row_data in enumerate(result):
            twcredito.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                twcredito.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


class SqldatabaseContado:
    def __init__(self):
        self.connection = sql.connect("contado.db")

    def createDB(self):
        self.connection.commit()
        self.connection.close()

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''CREATE TABLE contado (
                codigo_credito text,
                nombre_cliente text,
                producto text,
                forma_de_pago text,
                fecha_de_pago text,
                ingreso float,
                egreso float,
                saldo float
            )'''
        )
        self.connection.commit()
        self.connection.close()

    def insertRow(
            self, codigo_credito, nombre_cliente, producto,
            forma_de_pago, fecha_de_pago, ingreso,
            egreso, saldo
    ):
        cursor = self.connection.cursor()
        instruccion = f" INSERT INTO contado VALUES ('{codigo_credito}', '{nombre_cliente}', '{producto}', '{forma_de_pago}', '{fecha_de_pago}'," \
                      f" {ingreso}, {egreso}, {saldo})"
        cursor.execute(instruccion)
        self.connection.commit()

    def getNumRows(self):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM contado"
        cursor.execute(query)
        num_rows = cursor.fetchone()[0]
        cursor.close()
        return num_rows

    def contado(self, tablewidgetcontado):
        cursor = self.connection.cursor()
        instruccion = f"SELECT * FROM contado"
        result = cursor.execute(instruccion)
        tablewidgetcontado.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tablewidgetcontado.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablewidgetcontado.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


class SqldatabaseClientes:

    def __init__(self):
        self.connection = sql.connect("clientes.db")

    def creatDB(self):
        self.connection.commit()
        self.connection.close()

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            '''CREATE TABLE clientes (
                codigo text,
                nombre text,
                ciudad text,
                telefono text,
                cumpleanos text,
                aniversario text,
                edad text,
                ocupacion text,
                necesidades text,
                humectacion text,
                otras_necesidades text,
                area_de_ojos text,
                area_de_labios text,
                acabado_tipo_tono text,
                look text	
            )'''
        )
        self.connection.commit()
        self.connection.close()

    def insertRow(
            self, codigo, nombre, ciudad, telefono,
            cumpleanos, aniversario, edad,
            ocupacion, necesidades, humectacion,
            otras_necesidades, area_de_ojos, area_de_labios,
            acabado_tipo_tono, look
    ):
        cursor = self.connection.cursor()
        instruccion = f"INSERT INTO clientes VALUES ('{codigo}', '{nombre}', '{ciudad}', '{telefono}', '{cumpleanos}', '{aniversario}'," \
                      f" '{edad}', '{ocupacion}', '{necesidades}', '{humectacion}','{otras_necesidades}', '{area_de_ojos}'," \
                      f" '{area_de_labios}', '{acabado_tipo_tono}','{look}')"
        cursor.execute(instruccion)
        self.connection.commit()

    def updateFields(self, codigo,  nombre, telefono, aniversario, edad, ocupacion, necesidades, humectacion, otras_necesidades, area_de_ojos, area_de_labios, look):
        cursor = self.connection.cursor()
        instruccion = f"UPDATE clientes SET telefono = '{telefono}' WHERE codigo like '{codigo}%'  "
        instruccion_ = f"UPDATE clientes set nombre = '{nombre}' WHERE codigo like '{codigo}'"
        instruccion_2 = f"UPDATE clientes SET edad = '{edad}' WHERE codigo like '{codigo}%'  "
        instruccion_3 = f"UPDATE clientes SET aniversario = '{aniversario}' WHERE codigo like '{codigo}%'  "
        instruccion_4 = f"UPDATE clientes SET ocupacion = '{ocupacion}' WHERE codigo like '{codigo}%'  "
        instruccion_5 = f"UPDATE clientes SET necesidades = '{necesidades}' WHERE codigo like '{codigo}%'  "
        instruccion_6 = f"UPDATE clientes SET humectacion = '{humectacion}' WHERE codigo like '{codigo}%'  "
        instruccion_7 = f"UPDATE clientes SET otras_necesidades = '{otras_necesidades}' WHERE codigo like '{codigo}%'  "
        instruccion_8 = f"UPDATE clientes SET area_de_ojos = '{area_de_ojos}' WHERE codigo like '{codigo}%'  "
        instruccion_9 = f"UPDATE clientes SET area_de_labios = '{area_de_labios}' WHERE codigo like '{codigo}%'  "
        instruccion_10 = f"UPDATE clientes SET look = '{look}' WHERE codigo like '{codigo}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        cursor.execute(instruccion_5)
        cursor.execute(instruccion_6)
        cursor.execute(instruccion_7)
        cursor.execute(instruccion_8)
        cursor.execute(instruccion_9)
        cursor.execute(instruccion_10)
        self.connection.commit()

    def deleteRow(self, codigo):
        cursor = self.connection.cursor()
        instruccion = f"DELETE FROM clientes WHERE codigo like '{codigo}%'"
        cursor.execute(instruccion)
        self.connection.commit()

    def clientes(self, tablewidgetclientes):
        cursor = self.connection.cursor()
        instruccion = f"SELECT * FROM clientes"
        result = cursor.execute(instruccion)
        tablewidgetclientes.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tablewidgetclientes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablewidgetclientes.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def getNumRows(self):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM clientes"
        cursor.execute(query)
        num_rows = cursor.fetchone()[0]
        cursor.close()
        return num_rows


class FaltaCampos(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("warning.ui", self)
        self.setWindowTitle('Información de la interfaz')

        self.btn_ok.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.close)


class FaltaNombre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("warning_2.ui", self)
        self.setWindowTitle('Información de la interfaz')

        self.btn_ok.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.close)


class FaltaCodigoBD(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("warning_3.ui", self)
        self.setWindowTitle('Información de la interfaz')

        self.btn_ok.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.close)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('graphicinterface.ui', self)

        self.setWindowTitle('Femme elegance')

        self.DB_Clientes = SqldatabaseClientes()
        self.DB_Contado = SqldatabaseContado()
        self.DB_Credito = SqldatabaseCredito()
        self.DB_ClientesPreferencias = SqldatabaseClientesPreferencias()
        self.DB_Referencias = SqldatabaseReferencias()

        self.btn_hide_menu.hide()
        self.frame_menu.hide()

        self.btn_show_menu.clicked.connect(self.show_menu)
        self.btn_hide_menu.clicked.connect(self.hide_menu)

        self.btn_registro_cliente.clicked.connect(self.change_page_registro_clientes)
        self.btn_volver_preferencias.clicked.connect(self.change_page_registro_clientes)
        self.btn_volver_clientes.clicked.connect(self.change_page_registro_clientes)
        self.btn_femmelegance.clicked.connect(self.change_page_femmelegance)
        self.btn_referencias.clicked.connect(self.change_page_referencia)
        self.btn_base_de_datos_clientes.clicked.connect(self.change_page_bd_clientes)
        self.btn_preferencias.clicked.connect(self.change_page_preferencia)
        self.btn_finanzas.clicked.connect(self.change_page_finanzas)
        self.btn_bd_al_contado.clicked.connect(self.change_page_bd_contado)
        self.btn_volver_al_contado.clicked.connect(self.change_page_finanzas)
        self.btn_bd_credito.clicked.connect(self.change_page_bd_credito)
        self.btn_volver_creditos.clicked.connect(self.change_page_finanzas)

        self.btn_load_clientes.clicked.connect(self.load_clientes)
        self.btn_guardar_clientes.clicked.connect(self.registrar_clientes)
        self.btn_actualizar_cliente.clicked.connect(self.actualizar_clientes)
        self.btn_eliminar_cliente.clicked.connect(self.eliminar_clientes)
        self.btn_load_CP.clicked.connect(self.load_clientes_preferencias)
        self.btn_actualizar_preferencias.clicked.connect(self.actualizar_preferencias)
        self.btn_eliminar_pref.clicked.connect(self.eliminar_preferencia)
        self.btn_load_ref.clicked.connect(self.load_clientes_referencias)
        self.btn_registrar_ref.clicked.connect(self.registrar_referencias)
        self.btn_actu_ref.clicked.connect(self.actualizar_referencias)
        self.btn_eliminar_ref.clicked.connect(self.eliminar_referencia)
        self.btn_guardar_contado.clicked.connect(self.registrar_al_contado)
        self.btn_load_al_contado.clicked.connect(self.load_al_contado)
        self.guardar_credito.clicked.connect(self.registrar_creditos)
        self.btn_pago_1.clicked.connect(self.actualizar_pago_1)
        self.btn_pago_2.clicked.connect(self.actualizar_pago_2)
        self.btn_pago_3.clicked.connect(self.actualizar_pago_3)
        self.btn_load_credito.clicked.connect(self.load_credito)

    def show_warning(self):
        warning_dialog = FaltaCampos()
        warning_dialog.exec_()

    def show_warning_2(self):
        warning_dialog = FaltaNombre()
        warning_dialog.exec_()

    def show_warning_3(self):
        warning_dialog = FaltaCodigoBD()
        warning_dialog.exec_()

    def hide_menu(self):
        self.btn_hide_menu.hide()
        self.btn_show_menu.show()
        self.frame_menu.hide()

    def show_menu(self):
        self.btn_hide_menu.show()
        self.btn_show_menu.hide()
        self.frame_menu.show()

    def change_page_registro_clientes(self):
        self.stackedWidget.setCurrentWidget(self.page_registro_clientes)

    def change_page_femmelegance(self):
        self.stackedWidget.setCurrentWidget(self.page_femmelegance)

    def change_page_referencia(self):
        self.stackedWidget.setCurrentWidget(self.page_referencias)

    def change_page_bd_clientes(self):
        self.stackedWidget.setCurrentWidget(self.page_bd_clientes)

    def change_page_preferencia(self):
        self.stackedWidget.setCurrentWidget(self.page_preferencias)

    def change_page_finanzas(self):
        self.stackedWidget.setCurrentWidget(self.page_finanzas)

    def change_page_bd_contado(self):
        self.stackedWidget.setCurrentWidget(self.page_bd_contado)

    def change_page_bd_credito(self):
        self.stackedWidget.setCurrentWidget(self.page_bd_credito)

    def registrar_clientes(self):
        try:
            num_filas = int(self.DB_Clientes.getNumRows())
            codigo = str(num_filas + 1).zfill(3)
            nombre = str(self.nombre_cliente.text())
            ciudad = str(self.ciudad_cliente.text())
            telefono = str(self.telefono_cliente.text())
            cumpleanos = str(self.cumpleanos_cliente.text())
            aniversario = str(self.aniversario_cliente.text())
            edad = str(self.edad_cliente.text())
            ocupacion = str(self.ocupacion_cliente.currentText())
            necesidades = str(self.necesidades_cliente.currentText())
            humectacion = str(self.humectacion_cliente.currentText())
            otras_necesidades = str(self.otras_necesidades_cliente.currentText())
            area_de_ojos = str(self.area_de_ojos_cliente.currentText())
            area_de_labios = str(self.area_de_labios_cliente.currentText())
            acabado_tipo_tono = str(self.acabado_tipo_tono_cliente.text())
            look = str(self.look_cliente.currentText())

            nombre_preferencias = str(self.nombre_cliente.text())
            intereses = str(self.intereses_cliente.text())
            compartir_con = str(self.compartir_con_cliente.text())
            lista_de_deseos = str(self.lista_de_desos_cliente.text())
            cotizacion = str(self.cotizacion_cliente.text())

            if not self.nombre_cliente.text() or not self.ciudad_cliente.text() or not self.telefono_cliente.text() or not self.cumpleanos_cliente.text() or not self.aniversario_cliente.text() or not self.edad_cliente.text() or not self.intereses_cliente.text() or not self.compartir_con_cliente.text() or not self.lista_de_desos_cliente.text() or not self.cotizacion_cliente.text():
                self.show_warning()
            else:
                self.DB_ClientesPreferencias.insertRow(nombre_preferencias, intereses, compartir_con, lista_de_deseos, cotizacion)
                self.DB_Clientes.insertRow(codigo, nombre, ciudad, telefono, cumpleanos, aniversario, edad, ocupacion, necesidades, humectacion, otras_necesidades, area_de_ojos, area_de_labios, acabado_tipo_tono, look)
                self.nombre_cliente.setText(" ")
                self.ciudad_cliente.setText(" ")
                self.telefono_cliente.setText(" ")
                self.cumpleanos_cliente.setText(" ")
                self.aniversario_cliente.setText(" ")
                self.edad_cliente.setText(" ")
                self.acabado_tipo_tono_cliente.setText(" ")
                self.intereses_cliente.setText(" ")
                self.compartir_con_cliente.setText(" ")
                self.lista_de_desos_cliente.setText(" ")
                self.cotizacion_cliente.setText(" ")
        except:
            self.show_warning()

    def actualizar_clientes(self):
        try:
            codigo = str(self.codigo_cliente.text())
            nombre = str(self.nombre_cliente.text())
            telefono = str(self.telefono_cliente.text())
            aniversario = str(self.aniversario_cliente.text())
            edad = str(self.edad_cliente.text())
            ocupacion = str(self.ocupacion_cliente.currentText())
            necesidades = str(self.necesidades_cliente.currentText())
            humectacion = str(self.humectacion_cliente.currentText())
            otras_necesidades = str(self.otras_necesidades_cliente.currentText())
            area_de_ojos = str(self.area_de_ojos_cliente.currentText())
            area_de_labios = str(self.area_de_labios_cliente.currentText())
            look = str(self.look_cliente.currentText())

            if not self.codigo_cliente.text() or not self.nombre_cliente.text() or not self.telefono_cliente.text() or not self.aniversario_cliente.text() or not self.edad_cliente:
                self.show_warning_3()
            else:
                self.DB_Clientes.updateFields(codigo, nombre, telefono, edad, aniversario, ocupacion, necesidades, humectacion, otras_necesidades, area_de_ojos,
                                      area_de_labios, look)
                self.codigo_cliente.setText(" ")
                self.nombre_cliente.setText(" ")
                self.telefono_cliente.setText(" ")
                self.aniversario_cliente.setText(" ")
                self.edad_cliente.setText(" ")
        except:
            self.show_warning_3()

    def eliminar_clientes(self):
        try:
            codigo = str(self.codigo_cliente.text())
            if not self.codigo_cliente.text():
                self.show_warning_3()
            else:
                self.DB_Clientes.deleteRow(codigo)
                self.codigo_cliente.setText("")
        except:
            self.show_warning_3()

    def actualizar_preferencias(self):
        try:
            nombre = str(self.actu_nombre_p.text())
            intereses = str(self.actu_intereses_p.text())
            compartir_con = str(self.actu_compartir_con_p.text())
            lista_de_deseos = str(self.actu_lista_p.text())
            cotizacion = str(self.actu_cotizacion_p.text())

            if not self.actu_nombre_p.text() or not self.actu_intereses_p.text() or not self.actu_compartir_con_p.text() or not self.actu_lista_p.text() or not self.actu_cotizacion_p.text():
                self.show_warning_2()
            else:
                self.DB_ClientesPreferencias.updateFields(nombre, intereses, compartir_con, lista_de_deseos, cotizacion)
                self.actu_nombre_p.setText(" ")
                self.actu_intereses_p.setText(" ")
                self.actu_compartir_con_p.setText(" ")
                self.actu_lista_p.setText(" ")
                self.actu_cotizacion_p.setText(" ")
        except:
            self.show_warning_2()

    def eliminar_preferencia(self):
        try:
            nombre = str(self.actu_nombre_p.text())
            if not self.actu_nombre_p.text():
                self.show_warning_2()
            else:
                self.DB_ClientesPreferencias.deleteRow(nombre)
                self.actu_nombre_p.setText("")
        except:
            self.show_warning_2()

    def registrar_referencias(self):
        try:
            nombre_de_quien_refiere = str(self.nombre_ref.text())
            referido = str(self.ref_ref.text())
            telefono = str(self.telefono_ref.text())
            cita = str(self.cita_ref.text())
            parentezco = str(self.parentezco_ref.currentText())

            if not self.nombre_ref.text() or not self.ref_ref.text() or not self.telefono_ref.text() or not self.cita_ref.text():
                self.show_warning()
            else:
                num_filas = int(self.DB_Referencias.getNumRows())

                codigo = str(num_filas + 1).zfill(3)

                self.DB_Referencias.insertRow(codigo, nombre_de_quien_refiere, referido, telefono, cita, parentezco)
                self.nombre_ref.setText(" ")
                self.ref_ref.setText(" ")
                self.telefono_ref.setText(" ")
                self.cita_ref.setText(" ")
        except:
            self.show_warning()

    def actualizar_referencias(self):
        try:
            codigo = str(self.codigo_ref.text())
            nombre_de_quien_refiere = str(self.nombre_ref.text())
            referido = str(self.ref_ref.text())
            telefono = str(self.telefono_ref.text())
            cita = str(self.cita_ref.text())
            parentezco = str(self.parentezco_ref.currentText())

            if not self.codigo_ref.text() or not self.nombre_ref.text() or not self.ref_ref.text() or not self.telefono_ref.text() or not self.cita_ref.text() or not self.parentezco_ref.currentText():
                self.show_warning_3()
            else:
                self.DB_Referencias.updateFields(codigo, nombre_de_quien_refiere, referido, telefono, cita, parentezco)

            self.codigo_ref.setText("")
            self.nombre_ref.setText(" ")
            self.ref_ref.setText(" ")
            self.telefono_ref.setText(" ")
            self.cita_ref.setText(" ")
        except:
            self.show_warning_3()

    def eliminar_referencia(self):
        try:
            codigo = str(self.codigo_ref.text())
            if not self.codigo_ref.text():
                self.show_warning_3()
            else:
                self.DB_Referencias.deleteRow(codigo)
            self.codigo_ref.setText("")
        except:
            self.show_warning_3()

    def registrar_al_contado(self):
        try:
            nombre_cliente = str(self.cliente_nombre.text())
            producto = str(self.producto.text())
            forma_de_pago = str(self.forma_de_pago_c.currentText())
            fecha_de_pago = str(self.fecha_de_pago_c.text())
            ingreso = float(self.venta_c.text())
            egreso = float(self.egreso_c.text())
            saldo = float(self.saldo_c.text())

            num_filas = int(self.DB_Contado.getNumRows())

            codigo = str(num_filas + 1).zfill(3)

            self.DB_Contado.insertRow(str(codigo), nombre_cliente, producto, forma_de_pago, fecha_de_pago, ingreso, egreso, saldo)

            self.cliente_nombre.setText(" ")
            self.producto.setText(" ")
            self.fecha_de_pago_c.setText(" ")
            self.venta_c.setText(" ")
            self.egreso_c.setText(" ")
            self.saldo_c.setText(" ")
        except:
            self.show_warning()

    def registrar_creditos(self):
        try:
            num_filas = int(self.DB_Credito.getNumRows())
            codigo = str(num_filas + 1).zfill(3)
            nombre_cliente = str(self.cliente_nombre.text())
            producto = str(self.producto.text())
            forma_de_pago = str(self.forma_pago_credito.currentText())
            tipo_de_pago = str(self.tipo_pago_credito.currentText())
            valor_del_credito = float(self.valor_del_credito.text())
            cuota = float(self.cuotas_credito.text())
            plazos = int(self.plazos_credito.text())
            pago_1 = 0
            fecha_primer_pago = '-'
            pago_2 = 0
            fecha_segundo_pago = '-'
            pago_3 = 0
            fecha_tercer_pago = '-'
            saldo_pendiente = valor_del_credito - (pago_1 + pago_2 + pago_3)
            egreso = float(self.egresos_credito.text())
            saldo = float(self.saldo_credito.text())
            estado = 'Pendiente'

            self.DB_Credito.insertRow(codigo, nombre_cliente, producto, forma_de_pago, tipo_de_pago,
                                 valor_del_credito, cuota, plazos, pago_1, fecha_primer_pago,
                                 pago_2, fecha_segundo_pago, pago_3, fecha_tercer_pago,
                                 saldo_pendiente, egreso, saldo, estado)
            self.cliente_nombre.setText(" ")
            self.producto.setText(" ")
            self.valor_del_credito.setText(" ")
            self.cuotas_credito.setText(" ")
            self.plazos_credito.setText(" ")
            self.egresos_credito.setText(" ")
            self.saldo_credito.setText(" ")
        except:
            self.show_warning()

    def actualizar_pago_1(self):
        try:
            codigo = str(self.actu_codigo.text())
            pago_one = float(self.actu_pago.text())
            fecha_primer_pago = str(self.actu_fecha.text())
            valor_del_credito = float(self.DB_Credito.get_credito(codigo))
            pago_1 = float(pago_one)
            pago_2 = float(self.DB_Credito.getpago_2(codigo))
            pago_3 = float(self.DB_Credito.getpago_3(codigo))
            saldo_pendiente = (valor_del_credito - (pago_1 + pago_2 + pago_3))
            if saldo_pendiente == 0:
                estado = 'Cancelado'
            else:
                estado = 'Pendiente'

            self.DB_Credito.updateFields_pago1(codigo, pago_one, fecha_primer_pago, saldo_pendiente, estado)

            self.actu_codigo.setText(" ")
            self.actu_pago.setText(" ")
            self.actu_fecha.setText(" ")
        except:
            self.show_warning()

    def actualizar_pago_2(self):
        try:
            codigo = str(self.actu_codigo.text())
            pago_two = float(self.actu_pago.text())
            fecha_primer_pago = str(self.actu_fecha.text())
            valor_del_credito = float(self.DB_Credito.get_credito(codigo))
            pago_1 = float(self.DB_Credito.getpago_1(codigo))
            pago_2 = float(pago_two)
            pago_3 = float(self.DB_Credito.getpago_3(codigo))
            saldo_pendiente = (valor_del_credito - (pago_1 + pago_2 + pago_3))
            if saldo_pendiente == 0:
                estado = 'Cancelado'
            else:
                estado = 'Pendiente'

            self.DB_Credito.updateFields_pago2(codigo, pago_two, fecha_primer_pago, saldo_pendiente, estado)

            self.actu_codigo.setText(" ")
            self.actu_pago.setText(" ")
            self.actu_fecha.setText(" ")
        except:
            self.show_warning()

    def actualizar_pago_3(self):
        try:
            codigo = str(self.actu_codigo.text())
            pago_three = float(self.actu_pago.text())
            fecha_primer_pago = str(self.actu_fecha.text())
            valor_del_credito = float(self.DB_Credito.get_credito(codigo))
            pago_1 = float(self.DB_Credito.getpago_1(codigo))
            pago_2 = float(self.DB_Credito.getpago_2(codigo))
            pago_3 = float(pago_three)
            saldo_pendiente = (valor_del_credito - (pago_1 + pago_2 + pago_3))
            if saldo_pendiente == 0:
                estado = 'Cancelado'
            else:
                estado = 'Pendiente'

            self.actu_codigo.setText(" ")
            self.actu_pago.setText(" ")
            self.actu_fecha.setText(" ")

            self.DB_Credito.updateFields_pago3(codigo, pago_three, fecha_primer_pago, saldo_pendiente, estado)
        except:
            self.show_warning()

    def load_clientes(self):
        tablewidgetclientes = self.tablewidgetclientes
        self.DB_Clientes.clientes(tablewidgetclientes)

    def load_clientes_preferencias(self):
        tablewidgetpreferencias = self.tablewidgetpreferencias
        self.DB_ClientesPreferencias.preferencias(tablewidgetpreferencias)

    def load_clientes_referencias(self):
        tablewidgetreferencias = self.tablewidgetreferencias
        self.DB_Referencias.referencias(tablewidgetreferencias)

    def load_al_contado(self):
        tablewidgetcontado = self.tablewidgetcontado
        self.DB_Contado.contado(tablewidgetcontado)

    def load_credito(self):
        twcredito = self.twcredito
        self.DB_Credito.credito(twcredito)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()