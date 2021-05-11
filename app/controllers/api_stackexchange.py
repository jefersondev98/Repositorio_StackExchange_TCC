import requests
import json
class StackExchange():
    def __init__(self, page_size, max_pages):
        self.url_base = "https://api.stackexchange.com/2.2/"
        self.key = "&key=4rU2hllG6ydwRrC23RuHjA(("
        self.page = 1
        self.page_size = page_size
        self.max_pages = max_pages if max_pages != None else 100000
        self.current_url = ""
    
    #formatador de rotas
    def format_url(self, params_api):
        self.current_url = f"{self.url_base}{params_api}{self.key}"
    
    #rota que retorna todos os sites da stackexchage
    def sites(self):
        self.format_url(f"sites?page={self.page}&pagesize={self.page_size}&filter=!)5Go40vq3hW-*WORcvj5wWMiOVbI") #formata a url para essa rota
        response = requests.get(self.current_url)
        page_items = response.json()
        all_page_items = []
        all_page_items.append(page_items)
        while page_items["has_more"] == True and self.page < self.max_pages: #loop para pegar todos os itens da resposta, serve para respostam que tem mais de uma pagina
            self.page += 1
            current_url = self.format_url(f"sites?page={self.page}&pagesize={self.page_size}&filter=!)5Go40vq3hW-*WORcvj5wWMiOVbI")
            response = requests.get(self.current_url)
            page_items = response.json()
            all_page_items.append(page_items)
        return all_page_items
    
    def search(self, title_parameter, site_parameter):
        self.format_url(f"search/advanced?page={self.page}&pagesize={self.page_size}&order=desc&sort=votes&accepted=True&title={title_parameter}&site={site_parameter}&filter=!)E0fBjq-AsnarVKlARBxRcJDFDX8j60oDmcDl3M9iAJhKYBIq")
        print(self.current_url)
        response = requests.get(self.current_url)
        page_items = response.json()
        all_page_items = []
        all_page_items.append(page_items)
        while page_items["has_more"] == True and self.page < self.max_pages: #loop para pegar todos os itens da resposta, serve para respostam que tem mais de uma pagina
            self.page += 1
            current_url = self.format_url(f"search/advanced?page={self.page}&pagesize={self.page_size}&order=desc&sort=votes&accepted=True&title={title_parameter}&site={site_parameter}&filter=!)E0fBjq-AsnarVKlARBxRcJDFDX8j60oDmcDl3M9iAJhKYBIq")
            response = requests.get(self.current_url)
            page_items = response.json()
            all_page_items.append(page_items)
        return all_page_items#pegar o resto da divisão por 100

    def question(self):
        pass