class Texto:
    @staticmethod
    def arreglar_texto(texto):
        '''Recibe un texto y lo formatea para que tenga el primer caracter 
        en mayúscula y añade puntos y saltos de línea.'''

        partes = texto.split('#')
        
        texto_formateado = partes[0].capitalize() + "..."
        
        for parte in partes[1:]:
            texto_formateado += "\n" + parte.strip().capitalize() + "."
        
        return texto_formateado