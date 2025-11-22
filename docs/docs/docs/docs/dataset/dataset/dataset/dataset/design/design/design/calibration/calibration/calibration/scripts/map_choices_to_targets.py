import json, re

def likert_to_unit(x): 
    return (x-1)/4

def map_ids(ids):
    axes={"sinceridad":3,"suavidad":3,"firmeza":3,"empatia":3,"proximidad":3}
    for cid in ids:
        m=re.match(r"(.+?)_(\d)",cid)
        if not m: continue
        k,v=m.group(1),int(m.group(2))
        if k.startswith("proximidad"): k="proximidad"
        axes[k]=v
    return {k:likert_to_unit(v) for k,v in axes.items()}

print(map_ids(["sinceridad_4","empatia_5"]))
