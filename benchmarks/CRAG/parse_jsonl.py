import sys,json,os

os.mkdir("snippets")

for i,line in enumerate(sys.stdin):
    if len(line) < 3: continue
    j = json.loads(line.rstrip())
    print('line:\t' + str(i))
    print('query:\t' + str(j['query']))
    print('answer:\t' + str(j['answer']))
    print('urls:\t' + '\t'.join(r['page_url'] for r in j['search_results']))
    dir = "snippets/%04d" % i
    os.mkdir(dir)
    for jj,r in enumerate(j['search_results']):
        with open(dir + '/%04d.html' % jj, "w") as fd:
            print(r['page_snippet'], file=fd)

    
    
