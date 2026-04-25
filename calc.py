
# Idris Trader Calculator
print("--- IDRIS TRADER RISK CALCULATOR NA ---")

balance = float(input("Nawa ne jarinka (Balance)? "))
risk = float(input("Kashi nawa kake son kashewa (Risk %)? "))
sl_pips = float(input("Pips nawa ne Stop Loss dinka? "))

# Lissafi
amount_to_risk = balance * (risk / 100)
lot_size = amount_to_risk / sl_pips

print("\n--- SAKAMAKO ---")
print(f"Kudin da za ka iya asara (Risk): ${amount_to_risk}")
print(f"Lot Size din da ya kamata ka bude: {lot_size:.2f}")

print("Kada ka manta ka saka Stop Loss dinka a MetaTrader!")
