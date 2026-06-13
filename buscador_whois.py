import whois
import json

def investigar_site(dominio):
    print("--- INICIANDO BUSCA OSINT (NÍVEL 1) ---")
    print(f"[*] Investigando o domínio público: {dominio}...\n")
    
    try:
        # Faz a consulta pública nos servidores de registro de domínios
        informacoes = whois.whois(dominio)
        
        print("[🔓 DADOS PÚBLICOS ENCONTRADOS]")
        print("---------------------------------")
        # Exibe as informações principais de forma limpa na tela
        print(f"🏢 Empresa/Registrante: {informacoes.registrar}")
        print(f"🇧🇷 País de Origem: {informacoes.country}")
        print(f"📅 Data de Criação: {informacoes.creation_date}")
        print(f"🔒 Servidores de Nome (DNS): {informacoes.name_servers}")
        print(f"📧 E-mail de Contato: {informacoes.emails}")
        print("---------------------------------")
        
        # --- CAMINHO AVANÇADO ANTECIPADO: Salvando o relatório automaticamente ---
        with open("05_osint/relatorio_osint.json", "w") as f:
            # Converte as datas e objetos em texto comum para salvar sem erros
            json.dump(str(informacoes), f, indent=4)
        print("\n[+] Relatório de investigação salvo em '05_osint/relatorio_osint.json'!")
        
    except Exception as e:
        print(f"[❌ ERRO] Não foi possível obter dados para o domínio {dominio}.")
        print(f"Detalhe do erro: {e}")

if __name__ == "__main__":
    # Teste inicial com o site do Google (mude para qualquer site que quiser testar!)
    investigar_site("google.com")
