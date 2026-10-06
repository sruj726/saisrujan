from ideas_a import IDEAS_A
from ideas_b import IDEAS_B, IDEA_19
ideas=[i for i in IDEAS_A if i['id']!=19]+[IDEA_19]+IDEAS_B
W=dict(pain=15,wtp=12,rec=12,attr=10,aware=8,edu=8,feas=10,build=7,ret=7,comp=5,expand=3,boring=3)
def score(s):
    v=dict(s); v['edu']=11-s['edu']; v['build']=11-s['build']
    return round(sum(v[k]*w for k,w in W.items())/10,1)
for i in ideas: i['score']=score(i['s'])
ideas.sort(key=lambda i:-i['score'])
