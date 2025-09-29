import pandas as pd
from sodapy import Socrata
client = Socrata("www.datos.gov.co", None, timeout=100)

query = """
SELECT DISTINCT nit_entidad, nombre_entidad, orden, sector, rama, entidad_centralizada, codigo_entidad
"""
results = client.get("jbjy-vk9h", query=query)

dim_entidades = pd.DataFrame.from_records(results)

dim_entidades = dim_entidades[[
     "nit_entidad", "nombre_entidad",
    "orden", "sector", "rama", "entidad_centralizada",
    "codigo_entidad"
]]

dim_entidades.head()

query = """
SELECT DISTINCT documento_proveedor, proveedor_adjudicado, tipodocproveedor, es_pyme, es_grupo
"""
results = client.get("jbjy-vk9h", query=query)

dim_proveedores = pd.DataFrame.from_records(results)

dim_proveedores = dim_proveedores[[
    "documento_proveedor", "proveedor_adjudicado",
    "tipodocproveedor", "es_pyme", "es_grupo"
]]

dim_proveedores.head()

query = """
SELECT DISTINCT departamento, ciudad, localizaci_n
"""
results = client.get("jbjy-vk9h", query=query)

dim_geografia = pd.DataFrame.from_records(results)

dim_geografia = dim_geografia[[
     "departamento", "ciudad", "localizaci_n"
]]

dim_geografia.head()


query = """
SELECT DISTINCT tipo_de_contrato, modalidad_de_contratacion, justificacion_modalidad_de, codigo_de_categoria_principal
"""
results = client.get("jbjy-vk9h", query=query)

dim_tipo_contrato = pd.DataFrame.from_records(results)

dim_tipo_contrato = dim_tipo_contrato[[
    "tipo_de_contrato", "modalidad_de_contratacion",
    "justificacion_modalidad_de", "codigo_de_categoria_principal"
]]

dim_tipo_contrato.head()


query = """
SELECT DISTINCT fecha_de_firma, fecha_de_inicio_del_contrato, fecha_de_fin_del_contrato,
       fecha_inicio_liquidacion, fecha_fin_liquidacion,
       fecha_de_notificaci_n_de_prorrogaci_n, ultima_actualizacion
"""
results = client.get("jbjy-vk9h", query=query)

dim_tiempo = pd.DataFrame.from_records(results)

dim_tiempo = dim_tiempo[[
     "fecha_de_firma", "fecha_de_inicio_del_contrato",
    "fecha_de_fin_del_contrato", "fecha_inicio_liquidacion",
    "fecha_fin_liquidacion", "fecha_de_notificaci_n_de_prorrogaci_n",
    "ultima_actualizacion"
]]

dim_tiempo.head()


query = """
SELECT DISTINCT estado_contrato, liquidaci_n, habilita_pago_adelantado, el_contrato_puede_ser_prorrogado
"""
results = client.get("jbjy-vk9h", query=query)

dim_estado_contrato = pd.DataFrame.from_records(results)

dim_estado_contrato = dim_estado_contrato[[
    "estado_contrato", "liquidaci_n",
    "habilita_pago_adelantado", "el_contrato_puede_ser_prorrogado"
]]

dim_estado_contrato.head()


query = """
SELECT DISTINCT origen_de_los_recursos, destino_gasto
"""
results = client.get("jbjy-vk9h", query=query)

dim_recursos_financieros = pd.DataFrame.from_records(results)

dim_recursos_financieros = dim_recursos_financieros[[
     "origen_de_los_recursos", "destino_gasto"
]]

dim_recursos_financieros.head()


query = """
SELECT DISTINCT espostconflicto, obligaci_n_ambiental, obligaciones_postconsumo,
       reversion, puntos_del_acuerdo, pilares_del_acuerdo, estado_bpin
"""
results = client.get("jbjy-vk9h", query=query)

dim_marcadores = pd.DataFrame.from_records(results)

dim_marcadores = dim_marcadores[[
     "espostconflicto", "obligaci_n_ambiental",
    "obligaciones_postconsumo", "reversion",
    "puntos_del_acuerdo", "pilares_del_acuerdo", "estado_bpin"
]]

dim_marcadores.head()


query = """
SELECT DISTINCT nombre_ordenador_del_gasto, tipo_de_documento_ordenador_del_gasto,
       n_mero_de_documento_ordenador_del_gasto, nombre_supervisor,
       tipo_de_documento_supervisor, n_mero_de_documento_supervisor,
       nombre_ordenador_de_pago, tipo_de_documento_ordenador_de_pago,
       n_mero_de_documento_ordenador_de_pago, nombre_representante_legal,
       tipo_de_identificaci_n_representante_legal, identificaci_n_representante_legal,
       nacionalidad_representante_legal, domicilio_representante_legal, g_nero_representante_legal
"""
results = client.get("jbjy-vk9h", query=query)

dim_responsables = pd.DataFrame.from_records(results)

dim_responsables = dim_responsables[[
    "nombre_ordenador_del_gasto",
    "tipo_de_documento_ordenador_del_gasto", "n_mero_de_documento_ordenador_del_gasto",
    "nombre_supervisor", "tipo_de_documento_supervisor", "n_mero_de_documento_supervisor",
    "nombre_ordenador_de_pago", "tipo_de_documento_ordenador_de_pago", "n_mero_de_documento_ordenador_de_pago",
    "nombre_representante_legal", "tipo_de_identificaci_n_representante_legal",
    "identificaci_n_representante_legal", "nacionalidad_representante_legal",
    "domicilio_representante_legal", "g_nero_representante_legal"
]]

dim_responsables.head()


query = """
SELECT DISTINCT nombre_del_banco, tipo_de_cuenta, n_mero_de_cuenta
"""
results = client.get("jbjy-vk9h", query=query)

dim_cuentas = pd.DataFrame.from_records(results)

dim_cuentas = dim_cuentas[[
    "nombre_del_banco", "tipo_de_cuenta", "n_mero_de_cuenta"
]]

dim_cuentas.head(50)


query = """
SELECT DISTINCT proceso_de_compra, descripcion_del_proceso, objeto_del_contrato,
       condiciones_de_entrega, urlproceso, referencia_del_contrato
"""
results = client.get("jbjy-vk9h", query=query)

dim_proceso = pd.DataFrame.from_records(results)

dim_proceso = dim_proceso[[
     "proceso_de_compra", "descripcion_del_proceso",
    "objeto_del_contrato", "condiciones_de_entrega", "referencia_del_contrato"
]]

dim_proceso.head()
