#My Solution -----------------------------------------
def format_duration(seconds):
    if seconds == 0:
         return "now"
    
    years, seconds = divmod(seconds, 60*60*24*365)
    days, seconds = divmod(seconds, 60*60*24)
    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)

    timestamp = {"year": years, "day" : days, "hour":hours, "minute":minutes, "second" : seconds}

    result = {k: v for k,v in timestamp.items() if v != 0}

    unit = [f"{v} {k}{'s' if v>1 else ''}" for k, v in result.items()]

    if (len(unit) == 1):
        return "".join(unit)
    else:
        final = ", ".join(unit[:-1])
        return f"{final} and {unit[-1]}"

  #Best Practice ------------------------------------------
  times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
