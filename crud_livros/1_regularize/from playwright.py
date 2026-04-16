from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth  

with sync_playwright() as pw:
   navegador = pw.chromium.launch( headless=False)#trocar para true dps
#    navegador = pw.chromium.launch_persistent_context(
#       user_data_dir=r'C:\Temp\pw_profile',
#       headless=False,
#       channel="chrome",  # usa o Chrome instalado, não o Chromium do Playwright
#       args=[
#             "--disable-blink-features=AutomationControlled",
#             "--disable-infobars",
#             "--start-maximized",
#             "--no-sandbox",
#         ]
# )
   
   pagina = navegador.new_page()
   # Stealth().use_sync(pagina)  

   pagina.goto('https://www.listadevedores.pgfn.gov.br/')
   #pagina.wait_for_load_state("load")
   #pagina.wait_for_selector('input[placeholder="CPF/CNPJ"]')
   
   # input(">>> Pressione ENTER aqui: ")
   print( pagina.title())
   pagina.wait_for_timeout(3000)
   pagina.get_by_role("textbox", name="CPF/CNPJ").fill('11462916988')
   pagina.wait_for_timeout(3000)
   pagina.get_by_role("textbox", name="Nome").fill('Murilo Varoto')
   pagina.wait_for_timeout(3000)
   pagina.get_by_role("textbox", name="Valor mínimo").fill('0,00')
   pagina.wait_for_timeout(3000)
   pagina.get_by_role("textbox", name="Valor máximo").fill('1.000.000,00') 
   pagina.wait_for_timeout(3000)
   pagina.get_by_role("button" , name="Consultar").click()
   
   pagina.wait_for_load_state("networkidle")
   input("Pressione ENTER para fechar...")
   
   navegador.close()
