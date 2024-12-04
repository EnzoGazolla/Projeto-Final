from urllib.request import urlopen
from urllib.parse import urlencode
import json

class WeatherData:
    def _init_(self, cidade, temperatura, sensacao, umidade, descricao, vento):
        self.cidade = cidade
        self.temperatura = temperatura
        self.sensacao = sensacao
        self.umidade = umidade
        self.descricao = descricao
        self.vento = vento

    def mostrar(self):
        print(f"""
=== Clima em {self.cidade.title()} ===
Temperatura: {self.temperatura}°C
Sensação: {self.sensacao}°C
Umidade: {self.umidade}%
Condição: {self.descricao}
Vento: {self.vento} m/s
""")

class WeatherService:
    def _init_(self, api_key):
        self.api_key = api_key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def buscar_clima(self, cidade):
        try:
            # Monta a URL com os parâmetros
            params = {
                "q": cidade,
                "appid": self.api_key,
                "units": "metric",
                "lang": "pt_br"
            }
            url_completa = f"{self.url}?{urlencode(params)}"
            
            # Faz a requisição e processa a resposta
            with urlopen(url_completa) as response:
                dados = json.loads(response.read())
                
                return WeatherData(
                    cidade=cidade,
                    temperatura=dados['main']['temp'],
                    sensacao=dados['main']['feels_like'],
                    umidade=dados['main']['humidity'],
                    descricao=dados['weather'][0]['description'],
                    vento=dados['wind']['speed']
                )
        except Exception as erro:
            print(f"Erro ao buscar dados do clima: {erro}")
            return None

def main():
    API_KEY = "b8ea07460f524688ba0b082e8064d1c3"
    servico = WeatherService(API_KEY)

    while True:
        cidade = input("\nDigite o nome da cidade (ou 'sair' para encerrar): ")
        
        if cidade.lower() == 'sair':
            print("Até logo!")
            break
        
        clima = servico.buscar_clima(cidade)
        if clima:
            clima.mostrar()

if _name_ == "_main_":
    main()