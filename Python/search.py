'''
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch() #create a localhost server connection, or Elasticsearch("ip")
es.create(index="test-index", doc_type="test-type", id=1,
          body={"any": "data", "timestamp": datetime.now()})
'''
'''
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print res['create']

res = es.get(index="test-index", doc_type='tweet', id=1)
print res['_source']

es.indices.refresh(index="test-index")

res = es.get(index="test-index", body={"query": {"match_all": {}}})
print "Got %d Hits:" % res['hits']['total']
for hit in res['hits']['hits']:
    print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]
from elasticsearch import Elasticsearch

# by default we don't sniff ever
es = Elasticsearch()

# you can specify to sniff on startup to inspect the cluster and load
# balance across all node:
es = Elasticsearch(["seed1", "seed2"], sniff_on_start=True)

# you can also sniff periodically and/or after failure:
es = Elasticsearch(["seed1", "seed2"], sniff_on_start=True,
                   sniff_on_connection_fail=True, sniff_timeout=60)
''''''
from elasticsearch import Elasticsearch

# you can use RFC-1738 to specify the url
es = Elasticsearch(['https://user:secret@localhost:443'])

# ... or specify common 
'''
'''
import urllib2
import urllib
import json

url = 'http://vim.xiaorui.cc:9200/ceshi/rui'
data = {
    'title': 'jones',
    'amount': 5.7,
    }
data = json.dumps(data)

req = urllib2.Request(url, data, headers)
out = urllib2.urlopen(req)
print out.read()
'''
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("10.18.13.3")
j = 0
df = [['aa', 'bb'], ['cc', 'dd'], ['ee', 'ff'], ['gg', 'hh']]
print df[0]
count = int(df[0].count())
print count
actions = []
while(j < count):
    action = {
        "_index": "tickets-index",
        "_type": "tickets",
        "_id": j + 1,
        "_source": {
            "crawaldate": df[0][j],
            "flight": df[1][j],
            "price": float(df[2][j]),
            "discount": float(df[3][j]),
            "date": df[4][j],
            "takeoff": df[5][j],
            "land": df[6][j],
            "source": df[7][j],
            "timestamp": datetime.now()}
    }
    actions.append(action)
    j += 1

    if(len(actions) == 500000):
        helpers.bulk(es, actions)
        del actions[0:len(actions)]

if(len(actions) > 0):
    helpers.bulk(es, actions)
    del actions[0:len(actions)]

#helpers.py source code
def streaming_bulk(client, actions, chunk_size=500, raise_on_error=False,
        expand_action_callback=expand_action, **kwargs):
    actions = map(expand_action_callback, actions)

    # if raise on error is set, we need to collect errors per chunk before raising them
    errors = []

    while True:
        chunk = islice(actions, chunk_size)
        bulk_actions = []
        for action, data in chunk:
            bulk_actions.append(action)
            if data is not None:
                bulk_actions.append(data)

        if not bulk_actions:
            return

def bulk(client, actions, stats_only=False, **kwargs):
    success, failed = 0, 0

    # list of errors to be collected is not stats_only
    errors = []

    for ok, item in streaming_bulk(client, actions, **kwargs):
        # go through request-response pairs and detect failures
        if not ok:
            if not stats_only:
                errors.append(item)
            failed += 1
        else:
            success += 1

    return success, failed if stats_only else errors
