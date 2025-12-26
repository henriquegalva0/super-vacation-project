import yfinance as yf

def getPrice(ticker):
    stock = yf.Ticker(ticker)
    try:
        return stock.fast_info["last_price"]
    except Exception:
        return None


if __name__ == "__main__":
    ticker = input("Digite o Ticker da ação: ")
    ticker = ticker.strip().upper()
    price = getPrice(ticker)
    
    if price:
        print(f"Preço atual de {ticker}: {price}")
    else:
        print("ERRO: Ação não encontrada ou sem dados disponíveis!")  