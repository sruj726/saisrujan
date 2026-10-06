from score import ideas, W
V={1:"BUILD",3:"VALIDATE",11:"VALIDATE",7:"TOO COMPETITIVE",12:"FEATURE, NOT COMPANY",28:"VALIDATE",22:"TOO HARD",
13:"FEATURE, NOT COMPANY",10:"TOO HARD",8:"TOO COMPETITIVE",14:"TOO HARD",34:"VALIDATE",40:"NICHE OPPORTUNITY",39:"VALIDATE",
2:"TOO COMPETITIVE",17:"TOO HARD",38:"NICHE OPPORTUNITY",4:"FEATURE, NOT COMPANY",9:"TOO COMPETITIVE",24:"NICHE OPPORTUNITY",
29:"NICHE OPPORTUNITY",31:"NICHE OPPORTUNITY",18:"TOO COMPETITIVE",32:"FEATURE, NOT COMPANY",23:"NICHE OPPORTUNITY",
27:"TOO COMPETITIVE",36:"NICHE OPPORTUNITY",35:"NICHE OPPORTUNITY",19:"NICHE OPPORTUNITY",25:"FEATURE, NOT COMPANY",
26:"TOO COMPETITIVE",16:"TOO COMPETITIVE",37:"AVOID",5:"TOO COMPETITIVE",33:"AVOID",21:"AVOID",6:"AVOID",20:"FEATURE, NOT COMPANY",30:"AVOID",15:"AVOID"}
assert len(V)==40 and set(V)==set(i['id'] for i in ideas)
SC={1:"Commercial GCs $5–50M",2:"GCs with 20+ subs/month",3:"Public-works subcontractors",4:"Trade contractors 15–150 techs",5:"GCs $20M+",6:"High-hazard employers",7:"Carriers 3–50 trucks",8:"Small interstate carriers",9:"Fleets 5–100 vehicles",10:"Freight brokers",11:"Group practices 5–40 clinicians",12:"Healthcare employers",13:"Home care agencies",14:"Dental practices",15:"Landlords/PMs, multi-city",16:"PMs 200+ units",17:"Affordable housing PMs",18:"Bookkeeping firms",19:"STR managers 10–300 listings",20:"SMBs & bookkeepers",21:"Law firms 10–100 attorneys",22:"Litigation firms",23:"ISO shops & labs",24:"Small food manufacturers",25:"Warehouses",26:"Chemical-using businesses",27:"Insurance agencies",28:"Independent P&C agencies",29:"Childcare centers",30:"Nonprofits",31:"Backflow testers",32:"Franchisors 20–300 units",33:"Restaurants",34:"Healthcare staffing agencies",35:"A/E firms",36:"Independent used-car dealers",37:"Small GovCons",38:"Multi-site facilities teams",39:"Small 3PLs",40:"Independent vet clinics"}
CATN={"A":"A — already knows they need it","B":"B — knows the problem, not the software category","C":"C — tolerates it ('how we've always done it')","D":"D — needs education"}
def short_problem(i): 
    p=i['problem']; return p if len(p)<=90 else p[:87].rsplit(' ',1)[0]+'…'
out=["# Part 2 — All 40 Opportunities, Analyzed\n",
"Ideas are numbered by ID (the ranking is in `02-ranking.md`). Scores come from `_build/` data, so the arithmetic is reproducible.",
"Competitor pricing marked *(via search Oct 2026)* was checked with a live web search; everything else is approximate from prior knowledge, so verify it before relying on it.\n"]
for i in sorted(ideas,key=lambda x:x['id']):
    s=i['s']; i['verdict']=V[i['id']]
    out+=[f"---\n\n## {i['id']}. {i['name']}",
f"*{i['ind']}* · **Score {i['score']}/100** · **Verdict: {V[i['id']]}** · Boring-business test: {i['tests']}\n",
f"1. **Product concept:** {i['concept']}",
f"2. **Target customer:** {i['customer']}",
f"3. **Buyer:** {i['buyer']}",
f"4. **Problem:** {i['problem']}",
f"5. **Current manual process:** {i['manual']}",
f"6. **Why it sucks:** {i['sucks']}",
f"7. **Frequency:** {i['freq']}",
f"8. **Consequence of ignoring it:** {i['consequence']}",
f"9. **Existing software category:** {i['swcat']}",
f"10. **Major competitors:** {i['competitors']}",
f"11. **Typical competitor pricing:** {i['comp_pricing']}",
f"12. **Market gaps:** {i['gaps']}",
f"13. **Awareness category:** {CATN[i['cat']]}",
f"14. **Awareness:** {s['aware']}/10 · 15. **Customer attraction:** {s['attr']}/10 · 16. **Education required:** {s['edu']}/10 (lower is better)",
f"17. **Domain knowledge:** {i['domain']} · 18. **Build difficulty:** {s['build']}/10 · 19. **MVP estimate:** {i['mvp']}",
f"20. **Willingness to pay:** {s['wtp']}/10 · 21. **Price:** {i['price']}/mo · 22. **Retention:** {s['ret']}/10 · 23. **Competition opportunity:** {s['comp']}/10 (10 = little competition)",
f"24. **Market size:** {s['market']}/10 · 25. **First 10 reachable:** {s['f10']}/10 · 26. **First 100 reachable:** {s['f100']}/10 · 27. **Expansion:** {s['expand']}/10",
f"28. **Primary acquisition channel:** {i['channel']}",
f"29. **Best starting niche:** {i['niche']}",
f"30. **Biggest reason NOT to build it:** {i['why_not']}\n",
f"| Boring | Excel replacement | Must-have | Solo feasibility | Pain | Recurring |",
f"|---|---|---|---|---|---|",
f"| {s['boring']}/10 | {s['excel']}/10 | {i['must']} | {s['feas']}/10 | {s['pain']}/10 | {s['rec']}/10 |\n",
f"- **Customer value:** {i['value']}",
f"- **First-customer test (100 prospects tonight?):** **{i['first_test']}**. {i['first_where']}",
f"- **Payment test:** {i['payment']}",
f"- **Recurring test:** Month 1: {i['m1']} · Month 6: {i['m6']} · Year 2: {i['y2']}\n"]
open('../01-all-40-ideas.md','w').write("\n".join(out))
# ranking
r=["# Part 3 — Ranking & Final Table\n","## Weights\n","| Factor | Weight |","|---|---|"]
names={"pain":"Customer pain","wtp":"Willingness to pay","rec":"Recurring need","attr":"Customer attraction","aware":"Existing awareness","edu":"Low education requirement (11 − education)","feas":"Solo-founder feasibility","build":"Build simplicity (11 − difficulty)","ret":"Retention","comp":"Competition opportunity","expand":"Expansion potential","boring":"Boring score"}
for k,w in W.items(): r.append(f"| {names[k]} | {w}% |")
r+=["\n**No idea reached 80.** The highest is 79.4. That's intended: every idea has at least one real weakness.\n",
"**Important caveat:** competition carries only 5% in your weighting, so some high scorers are crowded or need a big team (docketing, broker vetting, IFTA, dental verification). The **Verdict** column is my investor judgment and overrides the raw score where they disagree.\n",
"| Rank | Product | Customer | Problem | Awareness | Customer Attraction | Education Needed | Boring Score | Build Difficulty | Monthly Price | Score | Verdict |",
"|---|---|---|---|---|---|---|---|---|---|---|---|"]
for n,i in enumerate(ideas,1):
    s=i['s']
    r.append(f"| {n} | {i['id']}. {i['name'].split(' — ')[0] if ' — ' in i['name'] else i['name']} | {SC[i['id']]} | {short_problem(i)} | {i['cat']} ({s['aware']}) | {s['attr']} | {s['edu']} | {s['boring']} | {s['build']} | {i['price']} | **{i['score']}** | {V[i['id']]} |")
from collections import Counter
c=Counter(V.values())
r+=["\n### Verdict distribution",", ".join(f"{k}: {v}" for k,v in c.most_common())]
open('../02-ranking.md','w').write("\n".join(r)+"\n")
print(c)
