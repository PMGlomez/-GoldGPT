tracked = []

def track_trade(data):
    tracked.append(data)
    return {"message": "Trade tracked", "total_tracked": len(tracked)}

def get_trade_status():
    return {"tracked": tracked}