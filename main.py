"""
if isinstance(candles[0], dict) and "close" in candles[0]:
for c in candles:
rows.append({
"time": int(c.get("epoch")),
"open": float(c.get("open")),
"high": float(c.get("high")),
"low": float(c.get("low")),
"close": float(c.get("close"))
})
else:
# fallback: assume [epoch, open, high, low, close]
for c in candles:
t, o, h, l, cl = c
rows.append({"time": int(t), "open": float(o), "high": float(h), "low": float(l), "close": float(cl)})


df = pd.DataFrame(rows).sort_values("time").reset_index(drop=True)
analyze_and_print(df)


if "error" in data:
print("[!] Error:", data["error"])




def on_close(ws, code, reason):
print(f"[-] Connection closed: {code} {reason}")


# ------------------------
# Analyze
# ------------------------


def analyze_and_print(df):
sig = generate_signal(df)
ts = int(df["time"].iloc[-1])
timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ts))
close = df["close"].iloc[-1]
print(f"[{timestr}] {SYMBOL} close={close:.6f} | Signal={sig}")


# ------------------------
# Runner
# ------------------------


def run_bot():
if not API_TOKEN:
print("[!] DERIV_API_TOKEN not found. Set DERIV_API_TOKEN in .env.")
return


ws = websocket.WebSocketApp(
DERIV_WS,
on_open=on_open,
on_message=on_message,
on_close=on_close
)


# run forever (reconnect is minimal; you can add backoff/retry)
while True:
try:
ws.run_forever()
except KeyboardInterrupt:
print("Exiting by user")
break
except Exception as e:
print("[!] WS error, reconnecting in 5s:", e)
time.sleep(5)




if __name__ == '__main__':
print("Deriv Signal-Only Bot starting...")
run_bot()
