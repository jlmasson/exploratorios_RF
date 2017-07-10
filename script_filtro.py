validacionMAC = "^(([0-9A-Fa-f]{2}:){5})([0-9A-Fa-f]{2})$"


dateparse = lambda x: pd.datetime.strptime(x,'%Y-%m-%d %h:%m:%s')
data = pd.read_csv('./rp_conexion.csv',sep=';',index_col=False, parse_dates={'datetime':['fecha','hora']}, usecols=["codigo","pauta_id","sitio_id","mac_usr","fecha","hora","ip_local","ip_usr","so","navegador","url_ref","tiempo_espera"])

data["filtroMAC"] = data['mac_usr'].str.contains(validacionMAC)
# data = data[filter]

# print(data)

data = data[data["filtroMAC"] == True]

# print(nuevoData)

del data["filtroMAC"]
