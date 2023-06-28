from django.db import models

class Cliente(models.Model):
    ID_CLIENTE = models.AutoField(primary_key=True)
    NOMBRE_CLI = models.CharField(max_length=30)
    APELLIDO_CLI = models.CharField(max_length=30)
    UBICACION_CLI = models.CharField(max_length=30)
    
    class Meta:
        managed = False  # Indica que no se debe administrar automáticamente la tabla por Django
        db_table = 'cliente'


class Requerimiento(models.Model):
    ID_REQUERIMIENTO = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.IntegerField(null=True, blank=True)
    ID_CLIENTE = models.IntegerField(null=True, blank=True)
    ID_REQ_ESP = models.IntegerField(null=True, blank=True)
    FECHA_REGISTRO_REQ = models.DateField()
    PRECIO_MIN_REQ = models.FloatField()
    PRECIO_MAX_REQ = models.FloatField()
    ZONA_REQ = models.CharField(max_length=50)
    ESTADO_ADQUISICION = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'requerimiento'

class Inmueble(models.Model):
    ID_INMUEBLE = models.AutoField(primary_key=True)
    ID_UBICACION = models.IntegerField(null=True, blank=True)
    ESTADO = models.CharField(max_length=50, default='Disponible')
    DETALLE_INM = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'inmueble'

class Ubicacion(models.Model):
    ID_UBICACION = models.AutoField(primary_key=True)
    ZONA_UBI = models.CharField(max_length=50)
    CALLE_PRINCIPAL = models.CharField(max_length=50)
    CALLE_COLINDANTES = models.CharField(max_length=20)
    REFERENCIA_UBI = models.CharField(max_length=50)
    PROVINCIA = models.CharField(max_length=50, null=True, blank=True)
    UBI_MAPS = models.TextField()
    IMAGEN_IMN = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'

class RequerimientoEspecif(models.Model):
    ID_REQ_ESP = models.IntegerField(primary_key=True)
    ID_REQUERIMIENTO = models.IntegerField()
    NRO_DORMITORIOS = models.IntegerField()
    NRO_BANOS = models.IntegerField()
    NRO_GARAJES = models.IntegerField()
    NRO_SALAS = models.IntegerField()
    NRO_PISOS = models.IntegerField()
    NRO_COCINAS = models.IntegerField()
    ANIMALES = models.SmallIntegerField()
    AMUEBLADO = models.SmallIntegerField()
    PATIO = models.SmallIntegerField()
    PISCINA = models.SmallIntegerField()
    OTROS_REQ = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'requerimiento_especif'

class Alquiler(models.Model):
    ID_ALQUILER = models.AutoField(primary_key=True)
    ID_TRANSACCION = models.IntegerField(null=True, blank=True)
    FECHAINI_ALQ = models.DateField()
    FECHAFIN_AQL = models.DateField()

    class Meta:
        db_table = 'alquiler'

class Anticretico(models.Model):
    ID_ANTICRETICO = models.AutoField(primary_key=True)
    ID_TRANSACCION = models.IntegerField(null=True, blank=True)
    FECHAINI_ANTI = models.DateField()
    FECHAFIN_ANTI = models.DateField()
    OBS_ANTI = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'anticretico'

class Casa(models.Model):
    ID_CASA = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.IntegerField(null=True, blank=True)
    DORMITORIOS_CASA = models.IntegerField()
    BANOS_CASA = models.IntegerField()
    SALA_CASA = models.SmallIntegerField()
    COMEDOR_CASA = models.SmallIntegerField()
    COCINA_CASA = models.SmallIntegerField()
    GARAJE_CASA = models.SmallIntegerField()
    PISOS_CASA = models.IntegerField()
    SUP_CONST_CASA = models.FloatField()
    SUP_LOTE_CASA = models.FloatField()
    FECHA_CONSTR_CASA = models.DateField()

    class Meta:
        db_table = 'casa'

class Comision(models.Model):
    ID_COMISION = models.AutoField(primary_key=True)
    ID_TRANSACCION = models.IntegerField(null=True, blank=True)
    PORCENTAJE_COM = models.DecimalField(max_digits=10, decimal_places=0)
    MONTO_COM = models.FloatField()

    class Meta:
        db_table = 'comision'
        
class Contrato(models.Model):
    ID_CONTRATO = models.AutoField(primary_key=True)
    ID_SUCURSAL = models.IntegerField(null=True, blank=True)
    MONTO_CONT = models.FloatField()
    FECHA_INI_CONT = models.DateField()
    FECHA_FIN_CONT = models.DateField()
    DETALLE_CONT = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'contrato'

class Demanda(models.Model):
    ID_DEM_CLIENTE = models.AutoField(primary_key=True)
    ID_CLIENTE = models.IntegerField(null=True, blank=True)
    ID_EMPLEADO = models.IntegerField(null=True, blank=True)
    COSTO_DEMANDA = models.FloatField()
    INMUEBLE_DEM = models.CharField(max_length=50)
    FECHA_DEM = models.DateField()
    TIPO_REQ_BUSCADO = models.CharField(max_length=10)

    class Meta:
        db_table = 'demanda'

class Departamento(models.Model):
    ID_DEPARTAMENTO = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.IntegerField(null=True, blank=True)
    DORMITORIOS_DEP = models.IntegerField()
    BANOS_DEP = models.IntegerField()
    SALA_DEP = models.SmallIntegerField()
    COMEDOR_DEP = models.SmallIntegerField()
    COCINA_DEP = models.SmallIntegerField()
    SUP_CONSTR_DEP = models.FloatField()
    FECHA_CONSTR_DEP = models.DateField()

    class Meta:
        db_table = 'departamento'

class Empleado(models.Model):
    ID_EMPLEADO = models.AutoField(primary_key=True)
    NOMBRE_EMP = models.CharField(max_length=30)
    APELLIDO_EMP = models.CharField(max_length=30)
    DIRECCION_EMP = models.CharField(max_length=50)
    CARGO_EMP = models.CharField(max_length=20, null=True, blank=True)
    HORA_ENTRADA = models.TimeField()

    class Meta:
        db_table = 'empleado'

class EntradaEmpleado(models.Model):
    ID_ENTRADA = models.AutoField(primary_key=True)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    ENTRADA = models.TimeField()
    TIEMPO_RETRASO = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'entrada_emp'

class EsRealizado(models.Model):
    ID_CONTRATO = models.AutoField(primary_key=True)
    ID_PROPIETARIO = models.ForeignKey('Propietario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'es_realizado'
        unique_together = (('ID_CONTRATO', 'ID_PROPIETARIO'),)

class Garzonier(models.Model):
    ID_GARZONIER = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.ForeignKey('Inmueble', on_delete=models.CASCADE)
    SUP_CONST_GAR = models.FloatField()
    FECHA_CONSTR_GAR = models.DateField()

    class Meta:
        db_table = 'garzonier'

class Lote(models.Model):
    ID_LOTE = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.ForeignKey('Inmueble', on_delete=models.CASCADE)
    SUP_LOTE = models.FloatField()

    class Meta:
        db_table = 'lote'

class Maneja(models.Model):
    ID_PROPIETARIO = models.ForeignKey('Propietario', on_delete=models.CASCADE)
    ID_INMUEBLE = models.ForeignKey('Inmueble', on_delete=models.CASCADE)

    class Meta:
        db_table = 'maneja'
        unique_together = (('ID_PROPIETARIO', 'ID_INMUEBLE'),)

class Oferta(models.Model):
    ID_OFERTA = models.AutoField(primary_key=True)
    ID_INMUEBLE = models.ForeignKey('Inmueble', on_delete=models.SET_NULL, null=True)
    ID_PROPIETARIO = models.ForeignKey('Propietario', on_delete=models.SET_NULL, null=True)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True)
    PORCENTAJE_OFERTA = models.DecimalField(max_digits=10, decimal_places=0)
    INMUEBLE_OFERTA = models.CharField(max_length=50)
    FECHA_OFERTA = models.DateField()
    TIPO_REQ_OFERTA = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'oferta'

class PrecioOferta(models.Model):
    ID_OFERTA = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    FECHA_PRECIO = models.DateField()
    MONTO_PRECIO_OF = models.FloatField()

    class Meta:
        db_table = 'precio_oferta'

class Propietario(models.Model):
    ID_PROPIETARIO = models.AutoField(primary_key=True)
    NOMBRE_PROP = models.CharField(max_length=50)
    APELLIDO_PROP = models.CharField(max_length=50)
    DIRECCION_PROP = models.CharField(max_length=50)

    class Meta:
        db_table = 'propietario'

class Publicidad(models.Model):
    ID_PUBL = models.AutoField(primary_key=True)
    ID_OFERTA = models.ForeignKey('Oferta', on_delete=models.CASCADE, null=True)
    TIPO_PUB = models.CharField(max_length=20)
    TELEFONO_PUB = models.CharField(max_length=11)
    FECHAINI_PUB = models.DateField()
    FECHAFIN_PUB = models.DateField(null=True)
    COSTO_PUB = models.FloatField()

    class Meta:
        db_table = 'publicidad'

class Retraso(models.Model):
    ID_RETRASO = models.AutoField(primary_key=True)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    FECHA_RETRASO = models.DateField()
    RETRASO_MINUTOS = models.IntegerField(default=0)

    class Meta:
        db_table = 'retraso'

class Salario(models.Model):
    ID_SALARIO = models.AutoField(primary_key=True)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    MES_SALARIO = models.CharField(max_length=10)
    MONTO_SALARIO = models.FloatField()
    FECHAIN_SALARIO = models.DateField()
    FECHAFIN_SALARIO = models.DateField()

    class Meta:
        db_table = 'salario'

class Subcomision(models.Model):
    ID_SUBCOMISION = models.AutoField(primary_key=True)
    ID_COMISION = models.ForeignKey('Comision', on_delete=models.CASCADE)
    ID_SALARIO = models.ForeignKey('Salario', on_delete=models.CASCADE)
    PORCENTAJE_SUBCOM = models.FloatField()
    MONTO_SUBCOM = models.FloatField()
    FECHA_SUBCOM = models.DateField()

    class Meta:
        db_table = 'subcomision'

class Sucursal(models.Model):
    ID_SUCURSAL = models.AutoField(primary_key=True)
    DIRECCION_SUC = models.CharField(max_length=50)

    class Meta:
        db_table = 'sucursal'

class TelefonoProp(models.Model):
    ID_TELF_PROP = models.AutoField(primary_key=True)
    ID_PROPIETARIO = models.ForeignKey('Propietario', on_delete=models.CASCADE)
    NUMERO_PROP = models.CharField(max_length=11)

    class Meta:
        db_table = 'telefono_prop'

class TelfCliente(models.Model):
    ID_TELF_CLIENTE = models.AutoField(primary_key=True)
    ID_CLIENTE = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    NUMERO_CLI = models.CharField(max_length=11)

    class Meta:
        db_table = 'telf_cliente'

class TelfEmp(models.Model):
    ID_TELF_EMP = models.AutoField(primary_key=True)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    NUMERO_EMP = models.CharField(max_length=11)

    class Meta:
        db_table = 'telf_emp'

class Transaccion(models.Model):
    ID_TRANSACCION = models.AutoField(primary_key=True)
    ID_CLIENTE = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    ID_INMUEBLE = models.ForeignKey('Inmueble', on_delete=models.CASCADE)
    ID_EMPLEADO = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    ID_VENTA = models.ForeignKey('Venta', on_delete=models.SET_NULL, null=True, blank=True)
    ID_ALQUILER = models.ForeignKey('Alquiler', on_delete=models.SET_NULL, null=True, blank=True)
    ID_ANTICRETICO = models.ForeignKey('Anticretico', on_delete=models.SET_NULL, null=True, blank=True)
    FECHA_TRANSACCION = models.DateField()
    CUENTA_ORIGEN = models.CharField(max_length=9, null=True, blank=True)
    MONTO_TRANSACCION = models.FloatField()

    class Meta:
        db_table = 'transaccion'

class Venta(models.Model):
    ID_VENTA = models.AutoField(primary_key=True)
    ID_TRANSACCION = models.ForeignKey('Transaccion', on_delete=models.CASCADE, null=True, blank=True)
    FECHA_VENTA = models.DateField()
    OBS_VENTA = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'venta'